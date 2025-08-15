# cdl-airflow2

When the target platform is CDL, you always import from the `cdl` package, e.g. `from cdl.artifacts import Artifact`.

The most important building blocks are but are not limited to:
- Env
- Tenant (>=3.0.0)
- CdlSparkSubmitOperator and its flavor for python
- Tables (Hive and Impala sync)
- Retention
- Stream- and SourcePipelines
- Stream ingestion (put files into HDFS/raw)

## Proxies
At Telia for external communication (e.g. internet or other systems) proxies are often used.
Each cluster within CDL may or may not have different settings. Especially important here are `NO_PROXY` settings.

## Env
`from cdl.env import Env` allows you to get help with standard paths, localisation, time zones, users, environment and queues.
Please check out the comments in the code for more details description.

## Tenant
From version 3.0.0 the framework supports multi tenants using `from cdl.tenant import Tenant`. Before any
operations towards CDL, you must define for which tenant you aim to work with. This is done using the `with Tenant` 
statement. There are three ways to declare a DAG. If you use a context manager,`with DAG(..) as dag`, or a decorator,
`@dag(..)`, it will add the DAG to the `Tenant` or any operators implicitly. This example shows how to create a DAG 
using the context manager:
```python
with DAG(..):
   with Tenant("swe"):
       SFTPSensor(..)  # This will be performed using the "swe" tenant
```
Or if you prefer the decorator way:
```python
@dag(..)
def my_dag():
   with Tenant("swe"):
       SFTPSensor(..)  # This will be performed using the "swe" tenant

my_dag()
```
Or, you can use a standard constructor, passing the dag into any operators you use:
```python

dag = DAG(..)

with Tenant("swe", dag):
   SFTPSensor(.., dag)  # This will be performed using the "swe" tenant
```

It is even possible to have a multi tenant DAG, e.g. perform operations for different tenants inside the same DAG.
```python
with Tenant("swe"):
    SFTPSensor(..)  # This will be performed using the "swe" tenant
with Tenant("nor"):
    DistcpOperator(..)  # This will be performed using the "nor" tenant
```
You can even stack the usage:
```python
with Tenant("swe"):
    SFTPSensor(..)  # This will be performed using the "swe" tenant
    with Tenant("nor"):
        DistcpOperator(..)  # This will be performed using the "nor" tenant
    CdlSparkSubmitOperator(..)  # This will again be performed using the "swe" tenant
```

## DistcpOperator
This operator is build to upload, using Hadoop [distcp](https://hadoop.apache.org/docs/stable/hadoop-distcp/DistCp.html), data from HDFS to S3.
It requires a connection of type S3. The parameter for connection `distcp_conn_id` is optional.  The default `distcp_conn_id` used is `s3`.
In that connection you need to specify host (proxy either for internet access or direct connect), port (proxy port), password (secret key) and login (access key).
Those values will populate the configuration parameters for [hadoop-aws](https://hadoop.apache.org/docs/current2/hadoop-aws/tools/hadoop-aws/index.html): `-Dfs.s3a.proxy.host`, `-Dfs.s3a.proxy.port`, `-Dfs.s3a.access.key`, `-Dfs.s3a.secret.key`.
In addition `-Dmapred.job.queue.name` will be set according to the default queue for your tenant.

The required parameters are: `source_folder` and `bucket`. `source_folder` may be a file or a folder. `bucket` is the name of the destination bucket.

Any additional parameters for hadoop-aws must be set in the extras json object that connection has. The key-value-pairs will be set as is on the Hadoop distcp command.
If you want to change the region of a bucket `landsat-pds`, the distcp command argument should be `hadoop distcp [options] -Dfs.s3a.bucket.landsat-pds.endpoint="${oregon.endpoint}"`.
The extra json object must be like this then:
```json
{
   "-Dfs.s3a.bucket.landsat-pds.endpoint": "${oregon.endpoint}"
}
```

Check the [code](src/cdl/hadoop/operators/distcp_operator.py) for additional configuration.

## CdlSparkSubmitOperator
`from cdl.spark.operators.cdl_spark_submit_operator import CdlSparkSubmitOperator` allows you to the use the very heart of our framework. There is very few components that does not use it.
It does the same thing as the official Airflow `SparkSubmitOperator` but has extended functionality. It does a ssh hop to one of our "spark edge nodes" and submits a spark application. After it is submitted it terminates the connection and polls in an interval (min 30 secs) after the status (_status_poll_interval).
It contains logic to handle kerberos tickets (principal and keytab), sets application name or adds tenant and squad name to it, adds yarn tags, scheduler metadata and handles additional files.

### CdlPySparkSubmitOperator
`from cdl.spark.operators.cdl_py_spark_submit_operator import CdlPySparkSubmitOperator` allows you to run python application from a python egg file. It does the same things as `CdlSparkSubmitOperator` but has additional logic for python environments and has requirements on your egg file. In your egg file there needs to be a special entry point to the application.
This entrypoint must live in the root of your project and be called "entry_point.py". This file must have a function called execute. The spark session is created for you. From within `entry_point` you may do any application logic typical to python.
```python
def execute(spark_session):
   # do things with spark
```
This function could also be used to run your unit tests with. In that case provide a spark session in your code.
To use conda environments with your spark app there is a parameter called `environment`. Give it the same name as you configure it in your build. It will be extracted and will be available to driver and executors.
All necessary configuration will be put into place for you. Note: this only works in cluster mode.

## Tables
`from cdl.table import Tables` allows you to refresh hive and impala tables.
It will create a spark operator for you with the necessary configuration like table names and connection strings.
Please check out the comments in the code for more details description.

## Retention
`from cdl.retention import Retention` allows you to execute cdl retention component.
It will create a spark operator for you with the necessary configuration from the environment and the proper jar.
This also is the base for the system dag: retention.

## StreamPipeline and SourcePipeline
The stream and source pipelines contain an understanding of what a default pipeline in CDL is. Try to stick to it as much as possible to reduce your own effort and increase delivery speed.
Any of the implementations can be customised with configuration. The default configuration is date. This will map `spark.cdl.date` parameter. For more details see [cdl-commons](https://github.com/telia-company/cdl-devx-commons-maven) documentation.

### StreamPipeline
Stream pipelines contains logic to create parts of a DAG. It implements the default understanding of a pipeline in hdfs.
It allows you to generate a sequence of operators which do (raw to base) => [ (sync cdl base tables), (base to access) => [ (sync cdl access tables), (access to abts) => (sync cdl abts tables) ].
You may skip table operations by setting optional constructor argument `skip_table_operations=True` (default false).
All these steps may be consumed only up to a certain layer. You may generate a pipeline up to base, access or abts. You do it like this:

```python
from cdl.artifacts import Artifact
from cdl.stream_pipeline import ScalaStreamPipeline
from cdl.tenant import Tenant

from airflow.models import DAG


with DAG(..) as dag:
    with Tenant("swe"):   

        my_ingestion_artifact = Artifact("<maven artifact descriptor>")

        # ingest to base only, with required arguments
        ScalaStreamPipeline(dag, "my_source", "my_stream_to_base_only", my_ingestion_artifact).ingest_to_base(start_from=get_my_data_to_hdfs_raw_layer_operator, continue_with=do_this_after_base_is_ready_operator)

        # ingest to access only (via base), with required arguments
        ScalaStreamPipeline(dag, "my_source", "my_stream_to_access_only", my_ingestion_artifact).ingest_to_access(start_from=get_my_data_to_hdfs_raw_layer_operator, continue_with=do_this_after_access_is_ready_operator)

        # ingest to abts (via base and access), with required arguments
        ScalaStreamPipeline(dag, "my_source", "my_stream_to_abts", my_ingestion_artifact).ingest_to_abts(start_from=get_my_data_to_hdfs_raw_layer_operator, continue_with=do_this_after_abts_is_ready_operator)
```
It comes in three flavors. All three have the same contract to the outside. The `ScalaStreamPipeline` executes your own Spark application (compatible with Java 1.8). It must have classes in package `com.teliacompany.cdl.<source name>` (from above examples `com.teliacompany.cdl.my_source`) which contains one application for each step you want to do.
The name is <from layer capitalized>To<to layer capitalized>. For second example above you need `com.teliacompany.cdl.my_source.RawToBase` and `com.teliacompany.cdl.my_source.BaseToAccess`.
The `CdlStreamPipeline` uses cdl-pipelines applications.
The `PyStreamPipeline` executes an egg file. There is no logic to call different applications for spark. You must handle this in your code. (see configuration)
All the constructors takes an argument of which configuration class to use and its overrides and configuration_source (see below documentation about configuration).

### SourcePipeline
The source pipeline is a wrapper around the stream pipelines. You may use it to create multiple stream ingestions. It comes in the same flavors as the stream pipeline. They wrap the corresponding stream pipeline flavor.
Each call to `ingest_stream_to_X` creates a chain of operators.
All the constructors takes an argument of which configuration class to use and its overrides and configuration_source (see below documentation about configuration).
```python
from cdl.artifacts import Artifact
from cdl.source_pipeline import ScalaSourcePipeline
from cdl.tenant import Tenant

from airflow.models import DAG


with DAG(..) as dag:
    with Tenant("swe"):   
      my_transformation_artifact = Artifact("<maven artifact descriptor>")
      
      ScalaSourcePipeline(dag, "my_source", my_transformation_artifact)\
         .ingest_stream_to_access("stream_from_raw_to_access")\
         .ingest_stream_to_base("stream_from_raw_to_base")\
         .ingest_stream_to_abts("stream_from_raw_to_abts")
```

### Configuration
The configuration holder class `from cdl.stream_configuration import StreamConfiguration` will create a new configuration dictionary.
That dictionary will contain all the default values our applications are configured with (see [spark-commons](https://github.com/telia-company/cdl-devx-spark-commons-maven) and [cdl-commons](https://github.com/telia-company/cdl-devx-commons-maven) for more details).
These values include:
- cdl.environment
- cdl.tenant
- cdl.layer
- cdl.layer.from
- cdl.source
- cdl.source.from
- cdl.stream
- cdl.stream.from
- cdl.configurationSource

The parameter `cdl.configurationSource` is merged with the overrides by target layer and key `configuration_source` (see class docs for example).
Spark parameters may be added into `application_context` key. This is what this could look like in overrides.
```json
{
   "base": {
      "application_context": {
         "spark.executor.instances": 20
      },
      "configuration_source": {
         "path": "/some/path"
      }
   },
   "abts": {
      "application_context": {
         "spark.executor.instances": 100
      },
      "configuration_source": {
         "path": "/some/different/path"
      }
   }
}
```
This will result in the following configuration for base (default keys like tenant etc are redacted) for spark:
- spark.executor.instances: 20
- spark.configurationSource: { "path": "/some/path" }

Similar example can be made for abts:
- spark.executor.instances: 100
- spark.configurationSource: { "path": "/some/different/path" }

Most pipelines are build around a certain schedule. By default, it is assumed it is a daily schedule. That will add `cdl.date` parameter (taken form Airflow schedule date).
If a different behavior is required, you may choose other flavors to set other parameters. All of them get the actual values from Airflow.
- `DynamicDateStreamConfiguration` (sets `cdl.year`, `cdl.month` and `cdl.day`)
- `YearStreamConfiguration` (sets `cdl.year`)
- `MonthStreamConfiguration` (sets `cdl.month`)
- `YearMonthStreamConfiguration` (sets `cdl.year` and `cdl.month`)
- `DayStreamConfiguration` (sets `cdl.day`)
- `TimestampStreamConfiguration` (sets `cdl.timestamp`)

Please refer to documentation in [cdl-commons](https://github.com/telia-company/cdl-devx-commons-maven) and [spark-commons](https://github.com/telia-company/cdl-devx-spark-commons-maven) how these values may be consumed and applied in your application.
The configuration may easily be transformed to a spark config (`to_spark_configuration` or `get_spark_configuration_for_layer`)
or environment variable config (`to_environment_variables` or `get_environment_variables_for_layer`).
```python
# this is how you would get configuration ready for spark from those classes
from cdl.stream_configuration import YearStreamConfiguration
from cdl.source_pipeline import ScalaSourcePipeline
from cdl.tenant import Tenant

from airflow.models import DAG


with DAG(..) as dag:
    with Tenant("swe"):   
        configuration_source = {
            "path": "/any/path"
        }
        overrides = {
            "abts": {
                "configuration_source": {
                    "format": "JSON"
                },
                "application_context": {
                    "driver.memory": "500MB"
                }
            }
        }
        spark_configuration = YearStreamConfiguration("source", "stream", configuration_source=configuration_source)\
            .get_spark_configuration_for_layer("abts")

        # and this is how this is used in source/stream pipelines

        my_transfomration_artifact = Artifact("<maven artifact descriptor>")
        source_pipeline = ScalaSourcePipeline(dag, "my_source", my_transformation_artifact, stream_configuration_class=YearStreamConfiguration)
```

## Stream ingestion
Stream ingestion contains one helper method that allows to put files from an endge node into raw layer. It is used similar to the source and stream pipelines and can handle the same configuration classes.
```python
from cdl.artifacts import Artifact
from cdl.stream_ingestion import StreamIngestion
from cdl.tenant import Tenant

from airflow.models import DAG


with DAG(..) as dag:
    with Tenant("swe"):   
        my_ingestion_artifact = Artifact("<maven artifact descriptor>")
        StreamIngestion(dag, "my_source", "my_stream", my_ingestion_artifact).get_local_file_to_raw_operator()
```
Note if overrides are used, the target layer is always raw. It integrates nicely with `start_from` (see stream and source pipelines).

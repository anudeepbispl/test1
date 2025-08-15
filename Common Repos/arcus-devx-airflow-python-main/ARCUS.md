# Airflow running in Arcus

When the target platform is Arcus, you always import from the `arcus` package, e.g. `from arcus.artifacts import Artifact`.

## Proxies
There is a config map that may be consumed to make proxy configuration painless.
There are helpers to read the correct config map and populate correct environment variables for the containers.
Those are located in `arcus.kubernetes`. Using custom settings from config maps or secrets is also supported.
In that case the `NO_PROXY` settings will be merged with the cluster one but `HTTP_PROXY` and `HTTPS_PROXY` will be 
taken from the customised one.

## Uploading to S3
In Arcus we use [rclone](https://rclone.org/). It is a tool that can copy between many file storage solutions.
There are many functions at different abstraction levels. They all are in package `arcus.operators.rclone`.
The rclone operator allows you to copy any *remote* data source. It is completely up to the user to configure rclone. 
Check out the readme of the [container](https://github.com/telia-company/arcus-popsicle-rclone-docker) used for rclone.
From there you may use `arcus.operators.rclone.s3_to_s3` to interact between two S3 buckets. It helps to pre-populate default settings used to do S3 to S3.
Furthermore, building on top of `s3_to_s3` there is `minio_to_s3`. That function pre populates default settings to copy from local Minio to any S3.
Last but not least there is `minio_to_cirrus`. Those helpers are explicitly created to make integration towards Cirrus as easy as possible.
Here is a minimal example on how this could look like:
```python
from arcus.operators.rclone.minio_to_cirrus import get_rclone_operator_for_stream_config_and_cirrus_data_set
from arcus.stream_configuration import StreamConfiguration

stream_configuration=StreamConfiguration("a-source", "a-stream")
get_rclone_operator_for_stream_config_and_cirrus_data_set(
   stream_configuration,
   "a-cirrus-data-source"
)
```

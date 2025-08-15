# Internal Developer Platform

## Overview

The Arcus Internal Developer Platform (IDP) provides a unified environment for building, deploying, and operating data workflows and pipelines across Telia's CDL and Arcus platforms. It leverages Airflow for orchestration, supports multi-tenant operations, and integrates with cloud-native storage and compute resources.

## Key Components

- **Airflow**: Central workflow engine for authoring, scheduling, and monitoring DAGs.
- **CDL & Arcus Frameworks**: Python packages (`cdl-airflow2`, `arcus-popsicle-airflow-python`) with helper functions, operators, and sensors for CDL and Arcus.
- **Multi-Tenant Support**: Use the `Tenant` abstraction to scope resources and operations.
- **Proxies & Networking**: Built-in helpers for proxy configuration, supporting secure connectivity.
- **Data Pipelines**: Stream and source pipelines for ingesting, transforming, and syncing data across layers (raw, base, access, abts).
- **S3 & Minio Integration**: Rclone-based operators for moving data between storage backends.

## Developer Experience

- **Local Development**: Install dependencies from `requirements.txt` and use the provided Python framework to develop and test DAGs.
- **Deployment**: DAGs and supporting code are deployed into Airflow instances running inside Arcus or CDL environments.
- **Configuration**: Use YAML files to manage environment-specific settings, service accounts, and registry endpoints.
- **Extensibility**: Add new operators, sensors, or pipeline steps by extending the framework.

## Getting Started

1. Clone the relevant repo (e.g., `arcus-devx-airflow-python-main`).
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Author DAGs using the provided framework, referencing CDL or Arcus operators as needed.
4. Use the `Tenant` abstraction to scope your DAGs.
5. Configure environment and service accounts via YAML files in the configuration repo.
6. Deploy your DAGs to the target Airflow instance.

## Example: Multi-Tenant DAG

```python
from airflow.models import DAG
from cdl.tenant import Tenant
from cdl.spark.operators.cdl_spark_submit_operator import CdlSparkSubmitOperator

with DAG(..) as dag:
    with Tenant("swe"):
        CdlSparkSubmitOperator(..)
    with Tenant("nor"):
        CdlSparkSubmitOperator(..)
```

## Platform Integrations

- **S3/Minio**: Use rclone operators for data movement.
- **Spark**: Submit jobs via custom Spark operators.
- **Hive/Impala**: Table refresh and sync via framework helpers.

## Configuration Management

- Environment-specific YAML files (`dev.yaml`, `prod.yaml`, etc.)
- Service account and registry settings in `base.yaml`
- Import/export stream configuration in dedicated YAML files

## Change Management

- Track changes and releases in `CHANGELOG.md`
- Use CODEOWNERS for repository access control

## References

- [Arcus Framework Documentation](ARCUS.md)
- [CDL Framework Documentation](CDL.md)
- [Airflow](https://airflow.apache.org/)
- [Rclone](https://rclone.org/)

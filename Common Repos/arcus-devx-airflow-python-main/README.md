# arcus-popsicle-airflow-python
Airflow is a platform created by the community to programmatically author, schedule and monitor workflows. This python 
framework provides helper functions, operators and sensors to be used when developing DAGs aimed for CDL and/or Arcus.

To run operations towards CDL, this framework can be used in any Airflow instance having network connectivity towards 
CDL. However, when interacting with Arcus, the Airflow instance must run inside the Arcus platform. This means that if
the Airflow instance is running inside Arcus, you can use this framework to build pipelines against both CDL and Arcus.

More information how to use the framework with the two platforms can be found here:
- [CDL](CDL.md)
- [Arcus](ARCUS.md)

This package requires certain Airflow providers. We rely on the providers that Airflow has in their official docker image. Those that are not part of it, will be installed together with this package (`setup.py`).
Any addition libraries will be installed in our docker image that inherits from Airflow. To develop this locally and run tests, please install `requirements.txt`.
from setuptools import setup, find_packages

setup(
    name="cdl-airflow2",
    package_dir={"": "src"},
    version="5.3.1",
    packages=find_packages(exclude=["*tests*"], where="src"),
    maintainer="CDL DevX",
    maintainer_email="DL-CDL-DevX@teliacompany.com",
    url="https://github.com/telia-company/arcus-devx-airflow-python",
    description="This is the python framework used in Airflow running in Arcus.",
    long_description="This is the python framework used in Airflow running in Arcus. "
                     "This framework holds lots of knowledge about CDL and Arcus.",
    platforms=["CDL", "ARCUS"],
    license="Telia Company",
    install_requires=[
        "apache-airflow==2.10.5",
        "apache-airflow-providers-apache-hive==9.0.2",
        "apache-airflow-providers-apache-spark==5.0.1",
        "apache-airflow-providers-atlassian-jira==1.1.0",
        "apache-airflow-providers-jdbc==5.0.1",
        "apache-airflow-providers-trino==6.1.0",
        # "apache-airflow-providers-amazon", this is determined by airflows docker image we inherit from and install our package into
        # "apache-airflow-providers-cncf-kubernetes", this is determined by airflows docker image we inherit from and install our package into
        # "apache-airflow-providers-elasticsearch", this is determined by airflows docker image we inherit from and install our package into
        # "apache-airflow-providers-ftp, this is determined by airflows docker image we inherit from and install our package into
        # "apache-airflow-providers-http", this is determined by airflows docker image we inherit from and install our package into
        # "apache-airflow-providers-sftp", this is determined by airflows docker image we inherit from and install our package into
        # "apache-airflow-providers-snowflake", this is determined by airflows docker image we inherit from and install our package into
        # "apache-airflow-providers-ssh", this is determined by airflows docker image we inherit from and install our package into
    ]
)

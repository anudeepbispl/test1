# Changelog

## [5.3.1](https://github.com/telia-company/arcus-devx-airflow-python/compare/v5.3.0...v5.3.1) (2025-03-25)


### Bug Fixes

* Avoid using typing ([#106](https://github.com/telia-company/arcus-devx-airflow-python/issues/106)) ([971e4bb](https://github.com/telia-company/arcus-devx-airflow-python/commit/971e4bbba83bac56e253b78b3ab3b1bf88217466))
* Upgrade java-scala-hadoop to 1.0.3 and set default resources in ArcusKubernetesPodOperator ([#107](https://github.com/telia-company/arcus-devx-airflow-python/issues/107)) ([2ca8945](https://github.com/telia-company/arcus-devx-airflow-python/commit/2ca894567a5e1de349e7559f972b8dcf19b3e2ff))
* upgrade providers ([745b850](https://github.com/telia-company/arcus-devx-airflow-python/commit/745b8504c49d8bd99887e9d15488abd5ed956389))

## [5.3.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v5.2.0...v5.3.0) (2025-03-11)


### Features

* Lot of improvements ([9b038ad](https://github.com/telia-company/arcus-devx-airflow-python/commit/9b038ad9c3ec2ce1220885e6aabf8e0d9ed8973b))


### Bug Fixes

* Airflow 2.10.5, improvements and deprecations ([5244ec1](https://github.com/telia-company/arcus-devx-airflow-python/commit/5244ec1b9e07f3d0d29961bb4d1d041bc3cf8a53))
* General improvements including deprecation of get_kubernetes_operator and ArcusKubernetesOperator ([5285ea2](https://github.com/telia-company/arcus-devx-airflow-python/commit/5285ea23d53b2a71ef828eb5e029da09eb254bcd))

## [5.2.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v5.1.1...v5.2.0) (2025-02-09)


### Features

* Airflow 2.10.4 ([#102](https://github.com/telia-company/arcus-devx-airflow-python/issues/102)) ([7dd27a0](https://github.com/telia-company/arcus-devx-airflow-python/commit/7dd27a0a8db99e9496beca55ab211f2f4d4ac374))

## [5.1.1](https://github.com/telia-company/arcus-devx-airflow-python/compare/v5.1.0...v5.1.1) (2024-11-11)


### Bug Fixes

* Mask GCS credentials ([#100](https://github.com/telia-company/arcus-devx-airflow-python/issues/100)) ([5c20864](https://github.com/telia-company/arcus-devx-airflow-python/commit/5c20864484e121ffa989c5fe0b21c18dca388721))
* Template rclone operator fields ([#99](https://github.com/telia-company/arcus-devx-airflow-python/issues/99)) ([b08833b](https://github.com/telia-company/arcus-devx-airflow-python/commit/b08833bf30a3a3593f0bac0d5f80e9a8e8490c8e))

## [5.1.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v5.0.0...v5.1.0) (2024-10-17)


### Features

* CDLM-99110 - helper function for gcs rclone target
* add MNC team credentials
* made stream config in spark operators optional
* dependency management reworked

## [5.0.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v4.1.0...v5.0.0) (2024-08-13)


### ⚠ BREAKING CHANGES

* Airflow 2.9.3 ([#88](https://github.com/telia-company/arcus-devx-airflow-python/issues/88))

### Features

* Airflow 2.9.3 ([#88](https://github.com/telia-company/arcus-devx-airflow-python/issues/88)) ([180b0d9](https://github.com/telia-company/arcus-devx-airflow-python/commit/180b0d95718a67655c5e1ff283361dd666a8f4d1))


### Bug Fixes

* Return None variable instead of raising NotImplementedError ([#86](https://github.com/telia-company/arcus-devx-airflow-python/issues/86)) ([6d5dacc](https://github.com/telia-company/arcus-devx-airflow-python/commit/6d5daccaef3c58a41a5a942e2f98894f5ffb9345))

## [4.1.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v4.0.0...v4.1.0) (2024-06-18)


### Features

* ANFOT-5061: gateway to cirrus/minio operators ([#84](https://github.com/telia-company/arcus-devx-airflow-python/issues/84)) ([5db437c](https://github.com/telia-company/arcus-devx-airflow-python/commit/5db437c01fdc80b658e20d2c026d3894d102a99d))

## [4.0.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.14.0...v4.0.0) (2024-06-13)


### ⚠ BREAKING CHANGES

* ANFOT-4533 - new data schema on cirrus

### Bug Fixes

* ANFOT-4533 - new data schema on cirrus ([d5c6546](https://github.com/telia-company/arcus-devx-airflow-python/commit/d5c6546c883e8f72d7657435f9f614eb92af4470))

## [3.14.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.13.1...v3.14.0) (2024-05-28)


### Features

* Add KubernetesSecretsBackend ([#77](https://github.com/telia-company/arcus-devx-airflow-python/issues/77)) ([dd6a61a](https://github.com/telia-company/arcus-devx-airflow-python/commit/dd6a61a6afab4b31d349cde2559f048aa6fa0f68))


### Bug Fixes

* Add kerberos settings for python.get_spark_submit_operator ([#78](https://github.com/telia-company/arcus-devx-airflow-python/issues/78)) ([523c90d](https://github.com/telia-company/arcus-devx-airflow-python/commit/523c90db01b5b590334a00cddc06f08b35851632))
* Make secret name configurable ([#80](https://github.com/telia-company/arcus-devx-airflow-python/issues/80)) ([fd1a7de](https://github.com/telia-company/arcus-devx-airflow-python/commit/fd1a7dec63be0b196b7f06f7200350d9900a0a83))

## [3.13.1](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.13.0...v3.13.1) (2024-05-21)


### Bug Fixes

* add-setter to hook property ([#75](https://github.com/telia-company/arcus-devx-airflow-python/issues/75)) ([a2986e8](https://github.com/telia-company/arcus-devx-airflow-python/commit/a2986e8341c955aaa9a29d4213fb6ad5af953f3f))
* Upgrade rclone to 1.66.0 ([#73](https://github.com/telia-company/arcus-devx-airflow-python/issues/73)) ([05c1e9d](https://github.com/telia-company/arcus-devx-airflow-python/commit/05c1e9d2927fcb7ecbbcc2b9aa0b62927e5497a3))

## [3.13.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.12.4...v3.13.0) (2024-03-13)


### Features

* Airflow 2.8.3 ([#70](https://github.com/telia-company/arcus-devx-airflow-python/issues/70)) ([a0b9056](https://github.com/telia-company/arcus-devx-airflow-python/commit/a0b905621c29c4d8fc884d8159db3357d9b20d01))

## [3.12.4](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.12.3...v3.12.4) (2024-02-27)


### Bug Fixes

* Update astronomer-cosmos==1.3.2 ([#68](https://github.com/telia-company/arcus-devx-airflow-python/issues/68)) ([2ed2a0e](https://github.com/telia-company/arcus-devx-airflow-python/commit/2ed2a0ec832090e08feddd3859672cd3a8be21fe))

## [3.12.3](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.12.2...v3.12.3) (2024-01-24)


### Bug Fixes

* having folder and file with name 'utils' raises exception on FlexyPexy class import ([88fd138](https://github.com/telia-company/arcus-devx-airflow-python/commit/88fd138360b4642dda09d904938cec84501b4e46))
* having folder and file with name 'utils' raises exception on FlexyPexy class import ([5363d22](https://github.com/telia-company/arcus-devx-airflow-python/commit/5363d225be3b268bda19004770cf01f541492197))
* Replace deprecated execution_date with dag_run.logical_date ([#66](https://github.com/telia-company/arcus-devx-airflow-python/issues/66)) ([35d2320](https://github.com/telia-company/arcus-devx-airflow-python/commit/35d232086c077e55cb120a8d7bdb7fa65f4d9a77))

## [3.12.2](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.12.1...v3.12.2) (2024-01-15)


### Bug Fixes

* Bump applications to latest versions ([#63](https://github.com/telia-company/arcus-devx-airflow-python/issues/63)) ([87b4785](https://github.com/telia-company/arcus-devx-airflow-python/commit/87b478559ea1db5efc5e32d58d23c4360b4e3b16))

## [3.12.1](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.12.0...v3.12.1) (2023-12-21)


### Bug Fixes

* NoneType when killing task using cdl_ssh_wrapper ([#61](https://github.com/telia-company/arcus-devx-airflow-python/issues/61)) ([e528a7c](https://github.com/telia-company/arcus-devx-airflow-python/commit/e528a7ca9fe61110559a2cb65ca2828ea070a167))

## [3.12.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.11.0...v3.12.0) (2023-12-12)


### Features

* JiraNoTicket class ([067bacc](https://github.com/telia-company/arcus-devx-airflow-python/commit/067baccfb81f979c228e6f726748f104a5804b02))

## [3.11.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.10.0...v3.11.0) (2023-11-13)


### Features

* Airflow 2.7.3 ([#56](https://github.com/telia-company/arcus-devx-airflow-python/issues/56)) ([4e9fc9c](https://github.com/telia-company/arcus-devx-airflow-python/commit/4e9fc9c0ea2dccbd34f67bcab29d7e6ef448bfc1))

## [3.10.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.9.0...v3.10.0) (2023-11-09)


### Features

* Cast 2850 ms teams operator ([#53](https://github.com/telia-company/arcus-devx-airflow-python/issues/53)) ([7a10a83](https://github.com/telia-company/arcus-devx-airflow-python/commit/7a10a831d4b213167fc9d3b639c1f4c1b9119668))

## [3.9.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.8.0...v3.9.0) (2023-10-18)


### Features

* creating new ticket after 24h ([#51](https://github.com/telia-company/arcus-devx-airflow-python/issues/51)) ([b4030c4](https://github.com/telia-company/arcus-devx-airflow-python/commit/b4030c45408982290753c2a75bb7f7bb4b894a52))

## [3.8.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.7.0...v3.8.0) (2023-10-06)


### Features

* upgrade to airflow 2.6.3 ([#48](https://github.com/telia-company/arcus-devx-airflow-python/issues/48)) ([072566f](https://github.com/telia-company/arcus-devx-airflow-python/commit/072566f2e63bee15dbab8fc0d0f3096fed7e2ec4))


### Bug Fixes

* Update CODEOWNERS with new teamowner ([#49](https://github.com/telia-company/arcus-devx-airflow-python/issues/49)) ([6f68299](https://github.com/telia-company/arcus-devx-airflow-python/commit/6f68299eb2464ce4ef70e4be0691c9cd48aafd81))

## [3.7.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.6.0...v3.7.0) (2023-08-31)


### Features

* target_key_location ([#46](https://github.com/telia-company/arcus-devx-airflow-python/issues/46)) ([863d564](https://github.com/telia-company/arcus-devx-airflow-python/commit/863d564ea6f0eedceb6fb335e75fa2a61abac664))

## [3.6.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.5.0...v3.6.0) (2023-05-02)


### Features

* **error_handler:** jira interface ([#43](https://github.com/telia-company/arcus-devx-airflow-python/issues/43)) ([fb67f22](https://github.com/telia-company/arcus-devx-airflow-python/commit/fb67f22deb9cd3b922af9043caed3a3aea8d6f51))

## [3.5.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.4.3...v3.5.0) (2023-02-21)


### Features

* GDF-2780 - auto enable keytab ([0e9a3e5](https://github.com/telia-company/arcus-devx-airflow-python/commit/0e9a3e59e49a7ebeaba86e666439df24516a1dac))

## [3.4.3](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.4.2...v3.4.3) (2023-01-11)


### Bug Fixes

* check self._conf before using it ([#39](https://github.com/telia-company/arcus-devx-airflow-python/issues/39)) ([76e56f9](https://github.com/telia-company/arcus-devx-airflow-python/commit/76e56f9030347e3b087ff232a00ca1e9a869fc1d))

## [3.4.2](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.4.1...v3.4.2) (2023-01-10)


### Bug Fixes

* CDLDEVX-156 - less naive string replace for json passed as yarn … ([#33](https://github.com/telia-company/arcus-devx-airflow-python/issues/33)) ([b3d8417](https://github.com/telia-company/arcus-devx-airflow-python/commit/b3d841706e4730a5305de0173d25f110305ac0d2))
* Updating version of the Transformation Aritifact used by  table.py ([#37](https://github.com/telia-company/arcus-devx-airflow-python/issues/37)) ([ce0f897](https://github.com/telia-company/arcus-devx-airflow-python/commit/ce0f8977083791c7cf783b8b3dcbe4b321f17ed7))

## [3.4.1](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.4.0...v3.4.1) (2023-01-09)


### Bug Fixes

* SFTPMultiSensor must return the list with all dictionary keys with values ([#34](https://github.com/telia-company/arcus-devx-airflow-python/issues/34)) ([cd9b479](https://github.com/telia-company/arcus-devx-airflow-python/commit/cd9b479556c5f46fd0df1fc630bbb380dea30e41))

## [3.4.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.3.3...v3.4.0) (2022-12-07)


### Features

* GDF-2622 - allow image override from env variables ([96fba40](https://github.com/telia-company/arcus-devx-airflow-python/commit/96fba40933f92c3f6d9ad6700ba117fccc3e5fa1))
* upgrade dependencies for Airflow 2.5.0 ([#31](https://github.com/telia-company/arcus-devx-airflow-python/issues/31)) ([a9cca11](https://github.com/telia-company/arcus-devx-airflow-python/commit/a9cca114705f9ddf288db3f32b70198aaf7b185a))

## [3.3.3](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.3.2...v3.3.3) (2022-11-18)


### Bug Fixes

* Arcus Airflow improvements ([df9d014](https://github.com/telia-company/arcus-devx-airflow-python/commit/df9d014876f56bc8685c0e07c9fab8118e9192f9))

## [3.3.2](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.3.1...v3.3.2) (2022-10-12)


### Bug Fixes

* remove tic tenant (GDF-2464) ([397289a](https://github.com/telia-company/arcus-devx-airflow-python/commit/397289ab79b940a906be866c2a48136e7bb4d138))

## [3.3.1](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.3.0...v3.3.1) (2022-09-20)


### Bug Fixes

* Allow ErrorHandler without Tenant context ([#22](https://github.com/telia-company/arcus-devx-airflow-python/issues/22)) ([8fe5c61](https://github.com/telia-company/arcus-devx-airflow-python/commit/8fe5c6175635949170457bc912e570f3b08a8ddb))
* fetching CDL private keys from CDL specific directory ([#23](https://github.com/telia-company/arcus-devx-airflow-python/issues/23)) ([1d356b9](https://github.com/telia-company/arcus-devx-airflow-python/commit/1d356b9b74d9ed134bdf1cd1db3354fb4768aeee))
* Prioritize downstream tasks for retention ([#21](https://github.com/telia-company/arcus-devx-airflow-python/issues/21)) ([a2bb0c1](https://github.com/telia-company/arcus-devx-airflow-python/commit/a2bb0c1ab7791b4b54981c946daa33cf4c2d5c14))

## [3.3.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.2.5...v3.3.0) (2022-09-12)


### Features

* Arcus ([289799d](https://github.com/telia-company/arcus-devx-airflow-python/commit/289799db508485081b70155ce8e2e07fb45f35e7))
* Arcus ([#19](https://github.com/telia-company/arcus-devx-airflow-python/issues/19)) ([289799d](https://github.com/telia-company/arcus-devx-airflow-python/commit/289799db508485081b70155ce8e2e07fb45f35e7))

## [3.2.5](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.2.4...v3.2.5) (2022-09-12)


### Bug Fixes

* upgrade providers ([#17](https://github.com/telia-company/arcus-devx-airflow-python/issues/17)) ([f6bae71](https://github.com/telia-company/arcus-devx-airflow-python/commit/f6bae71104cfb4ff76c75c466251f4ab7bcd8f32))
* use devx workflows and secrets ([f75159b](https://github.com/telia-company/arcus-devx-airflow-python/commit/f75159b3b4b58a1400753b1762e18d7e7c842365))

## [3.2.4](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.2.3...v3.2.4) (2022-08-16)


### Bug Fixes

* Retention does not work with multiple tenants ([#15](https://github.com/telia-company/arcus-devx-airflow-python/issues/15)) ([2935ed2](https://github.com/telia-company/arcus-devx-airflow-python/commit/2935ed2fa973c9b28e50d547e938ebb6af39f997))

## [3.2.3](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.2.2...v3.2.3) (2022-08-12)


### Bug Fixes

* Upgrade providers needed for Airflow 2.3.3 ([a34dceb](https://github.com/telia-company/arcus-devx-airflow-python/commit/a34dceb009d14cd776595057c179f039d3a5692a))

## [3.2.2](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.2.1...v3.2.2) (2022-06-30)


### Bug Fixes

* pass tenant from context to JiraCDLM ([53bd765](https://github.com/telia-company/arcus-devx-airflow-python/commit/53bd765256e1d2ca48b940726aa108db83525976))
* remove unusable host from Jira ticket ([6152320](https://github.com/telia-company/arcus-devx-airflow-python/commit/6152320b81bfa09272eb007c00deb1cb01175133))

## [3.2.1](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.2.0...v3.2.1) (2022-06-30)


### Bug Fixes

* Use TaskInstance.execution_date ([1790a2c](https://github.com/telia-company/arcus-devx-airflow-python/commit/1790a2c2b4bb0eec18cd1bb242023015d8aba98f))

## [3.2.0](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.1.4...v3.2.0) (2022-06-29)


### Features

* Support for Airflow 2.3.x ([13352ab](https://github.com/telia-company/arcus-devx-airflow-python/commit/13352ab02e254bd8ea74cad3fce1a86f5f65d7bc))


### Bug Fixes

* Update Pipfile using python 3.9 ([bf4cb43](https://github.com/telia-company/arcus-devx-airflow-python/commit/bf4cb43c0f4cd63e81f054925068ca69a425c428))

### [3.1.4](https://github.com/telia-company/arcus-devx-airflow-python/compare/v3.1.3...v3.1.4) (2022-05-12)


### Bug Fixes

* CDLM-44297 - Error handler issue in AF2 ([#2](https://github.com/telia-company/arcus-devx-airflow-python/issues/2)) ([7fa3fee](https://github.com/telia-company/arcus-devx-airflow-python/commit/7fa3fee530a79f5e42d4fc3acb98cc3e15cc9ac8))

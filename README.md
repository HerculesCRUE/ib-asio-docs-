![](./images/logos_feder.png)

# Almacenamiento y entrega de documentación

[1. Entregables oficiales](#1-entregables-oficiales)

[2. Otros entregables](#2-otros-entregables)

[3. Repositorios](#3-repositorios)

## 1. Entregables oficiales

Relación de entregables oficiales del proyecto en su estado actual.

| Documentación                                                | Pruebas                                                      | Repositorios                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [01-Red de Ontologías Hércules](./01-Red_de_Ontologías_Hércules/ASIO_Red_de_Ontologias_Hercules.md) |                                                              | [ib-hercules-ontology](https://github.com/HerculesCRUE/ib-hercules-ontology) |
| [02 y 14-Especificación Ontologías Hércules](./02-Especificación_Ontologías_Hércules/ASIO_Izertis_EspecificacionOntologiasHercules.md) | N/A                                                          | [ib-hercules-ontology](https://github.com/HerculesCRUE/ib-hercules-ontology) |
| [03-Conversión de recursos a OWL](./03-Conversión_de_recursos_a_OWL/ASIO_Izertis_ConversionDeRecursosAOWL.md) |                                                              | -                                                            |
| [04-Modelo multilingüismo](./04-Modelo_multilingüismo/ASIO_Izertis_ModeloMultilinguismo.md) | N/A                                                          | -                                                            |
| [05-Análisis de métodos FAIR](./05-Análisis_de_métodos_FAIR/ASIO_Izertis_AnalisisDeMetodosFAIR.md) | N/A                                                          | -                                                            |
| [06-Métricas FAIR](./06-Métricas_FAIR/README.md)             | [test-fair](./06-M%C3%A9tricas_FAIR/manual_tecnico.md#pruebas-unitarias) | -                                                            |
| [07-Control de versiones OWL](./07-Control_de_versiones_OWL/ASIO_Izertis_ControlDeVersionesOWL.md) |                                                              | [ib-hercules-sync](https://github.com/HerculesCRUE/ib-hercules-sync) |
| [08 y 19-Esquema de URIs Hércules](./08-Esquema_de_URIs_Hércules/ASIO_Izertis_ArquitecturaDeURIs.md) | N/A                                                          | -                                                            |
| [09-Buenas prácticas para URIs Hércules](./09-Buenas_prácticas_para_URIs_Hércules/ASIO_Izertis_BuenasPracticasParaURIsHercules.md) | N/A                                                          | -                                                            |
| [10-Librería Factoría de URIs](https://github.com/HerculesCRUE/ib-uris-generator) | [Testing TDD](https://reports.herculesasioizertis.desa.um.es/uris-generator/surefire/surefire-report.html)<br/>[Cobertura TDD](https://reports.herculesasioizertis.desa.um.es/uris-generator/jacoco/)<br/>[Testing BDD](https://github.com/HerculesCRUE/ib-uris-generator/blob/master/docs/testing.md) | [ib-uris-generator](https://github.com/HerculesCRUE/ib-uris-generator) |
| [11-Benchmark con criterios adicionales y resultados](https://github.com/HerculesCRUE/ib-benchmarks) | [Test Unitarios](https://github.com/HerculesCRUE/ib-benchmarks/blob/master/test.md) | [ib-benchmarks](https://github.com/HerculesCRUE/ib-benchmarks) |
| [12-Análisis sobre necesidad de cumplimiento LDP](./12-Análisis_sobre_necesidad_de_cumplimiento_LDP/Analisis_sobre_la_necesidad_de_cumplimiento_LDP.md) | N/A                                                          | -                                                            |
| 13 y 16-Backend SGI Software<br />[Arquitectura](./00-Arquitectura/architecture.md),<br /> [Importador](https://github.com/HerculesCRUE/ib-dataset-importer), [Procesador](https://github.com/HerculesCRUE/ib-input-processor),<br /> [Sistema de gestión](https://github.com/HerculesCRUE/ib-management-system),<br /> [Procesador de eventos](https://github.com/HerculesCRUE/ib-event-processor),<br /> [Servicio de publicación web](https://github.com/HerculesCRUE/ib-web-publication-backend),<br /> [Librería de conexión con Triple Store](https://github.com/HerculesCRUE/ib-triples-storage-adapter),<br /> [Librería de descubrimiento](https://github.com/HerculesCRUE/ib-discovery),<br /> [Modelo de dominio](https://github.com/HerculesCRUE/ib-dataset-domain-model),<br /> [Proyecto ETL](https://github.com/HerculesCRUE/ib-dataset-etl),<br /> [Docker Pentaho](https://github.com/HerculesCRUE/ib-pentaho-docker),<br /> [Plataforma Linked Data](https://github.com/HerculesCRUE/ib-asio-ldp), <br />[Documentación despliegue en entorno de desarrollo](https://github.com/HerculesCRUE/ib-asio-composeset/blob/master/README.md)<br /> | <br />[Testing dataset importer](https://reports.herculesasioizertis.desa.um.es/dataset-importer/surefire/surefire-report.html),<br />[Cobertura dataset importer](https://reports.herculesasioizertis.desa.um.es/dataset-importer/jacoco/),<br /><br />[Testing input processor](https://reports.herculesasioizertis.desa.um.es/input-processor/surefire/surefire-report.html)<br />[Cobertura input processor](https://reports.herculesasioizertis.desa.um.es/input-processor/jacoco/)<br /><br />[Testing event processor](https://reports.herculesasioizertis.desa.um.es/event-processor/surefire/surefire-report.html)<br />[Cobertura event processor](https://reports.herculesasioizertis.desa.um.es/event-processor/jacoco/)<br /><br />[Testing triples storage adapter](https://reports.herculesasioizertis.desa.um.es/triples-storage-adapter/surefire/surefire-report.html)<br />[Cobertura triples storage adapter](https://reports.herculesasioizertis.desa.um.es/triples-storage-adapter/jacoco/)<br /><br />[Testing management system](https://reports.herculesasioizertis.desa.um.es/management-system/surefire/surefire-report.html)<br />[Cobertura management system](https://reports.herculesasioizertis.desa.um.es/management-system/jacoco/)<br /><br />[Testing web-publication-service](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-web-publication-service&metric=coverage&view=list)<br />[Testing web-publication-backend](https://reports.herculesasioizertis.desa.um.es/web-publication-backend/surefire/surefire-report.html)<br />[Cobertura web-publication-backend](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-web-publication-backend&metric=coverage&view=list)<br /><br /> | [ib-asio-ldp](https://github.com/HerculesCRUE/ib-asio-ldp),<br />[ib-dataset-importer](https://github.com/HerculesCRUE/ib-dataset-importer),<br /> [ib-dataset-domain-model](https://github.com/HerculesCRUE/ib-dataset-domain-model), <br />[ib-input-processor](https://github.com/HerculesCRUE/ib-input-processor), <br />[ib-domain-model](https://github.com/HerculesCRUE/ib-domain-model), <br />[ib-event-processor](https://github.com/HerculesCRUE/ib-event-processor), <br />[ib-triples-storage-adapter](https://github.com/HerculesCRUE/ib-triples-storage-adapter), <br />[ib-management-system](https://github.com/HerculesCRUE/ib-management-system), <br />[ib-pentaho-docker](https://github.com/HerculesCRUE/ib-pentaho-docker), <br />[ib-fuseki-docker](https://github.com/HerculesCRUE/ib-fuseki-docker), <br />[ib-wikibase-docker](https://github.com/HerculesCRUE/ib-wikibase-docker),<br /> [ib-web-publication-service](https://github.com/HerculesCRUE/ib-web-publication-service),<br /> [ib-web-publication-backend](https://github.com/HerculesCRUE/ib-web-publication-backend), <br />[ib-simulator-importer](https://github.com/HerculesCRUE/ib-simulator-importer),<br /> [ib-dataset-etl](https://github.com/HerculesCRUE/ib-dataset-etl), <br />[ib-asio-abstractions](https://github.com/HerculesCRUE/ib-asio-abstractions), <br />[ib-asio-composeset](https://github.com/HerculesCRUE/ib-asio-composeset)<br />[ib-api-exchange](https://github.com/HerculesCRUE/ib-api-exchange) |
| [15-Ejemplos reales de aplicación de razonamiento automático](./15-Ejemplos_reales_de_aplicación_de_razonamiento_automático/README.md) |                                                              | -                                                            |
| [17-Manual de uso Backend SGI](./00-Análisis/Manual%20de%20usuario/Manual%20de%20usuario.md) |                                                              | -                                                            |
| 18-Imágenes Docker de Backend SGI                            |                                                              | [ib-pentaho-docker](https://github.com/HerculesCRUE/ib-pentaho-docker), <br />[ib-wikibase-docker](https://github.com/HerculesCRUE/ib-wikibase-docker),<br />[ib-fuseki-docker](https://github.com/HerculesCRUE/ib-fuseki-docker),<br />[ib-web-publication-service](https://hub.docker.com/r/herculescrue/web-publication-service), <br />[ib-web-publication-backend](https://hub.docker.com/r/herculescrue/web-publication-backend), <br />[ib-discovery](https://hub.docker.com/r/herculescrue/discovery), <br />[ib-federation](https://hub.docker.com/r/herculescrue/federation), <br />[ib-uris-generator](https://hub.docker.com/r/herculescrue/uris-generator), <br />[ib-asio-ldp](https://hub.docker.com/r/herculescrue/asio-ldp), <br />[ib-dataset-importer](https://hub.docker.com/r/herculescrue/dataset-importer), <br />[ib-triples-storage-adapter](https://hub.docker.com/r/herculescrue/triples-storage-adapter), <br />[ib-service-discovery](https://hub.docker.com/r/herculescrue/service-discovery), <br />[ib-event-processor](https://hub.docker.com/r/herculescrue/event-processor), <br />[ib-input-processor](https://hub.docker.com/r/herculescrue/input-processor), <br />[ib-management-system](https://hub.docker.com/r/herculescrue/management-system), <br />[ib-api-exchange](https://hub.docker.com/r/herculescrue/api-exchange), <br />[ib-pdi](https://hub.docker.com/r/herculescrue/pdi), <br />[ib-simulator-importer](https://hub.docker.com/r/herculescrue/simulator-importer) |
| 20-Resultados Benchmark                                      | N/A                                                          | [ib-benchmarks](https://github.com/HerculesCRUE/ib-benchmarks) |
| [21-Librería de conexión a Triple Store](https://github.com/HerculesCRUE/ib-triples-storage-adapter/blob/master/README.md) |                                                              | [ib-triples-storage-adapter](https://github.com/HerculesCRUE/ib-triples-storage-adapter) |
| [22-Librería de conversión a RDF](https://github.com/HerculesCRUE/ib-management-system) | [Testing](https://reports.herculesasioizertis.desa.um.es/management-system/surefire/surefire-report.html)<br />[Cobertura](https://reports.herculesasioizertis.desa.um.es/management-system/jacoco/)<br /> | [ib-management-system](https://github.com/HerculesCRUE/ib-management-system) |
| [23-Librería de validación de RDF](./23-Librer%C3%ADa_de_validación_de_RDF/README.md) |                                                              | [https://github.com/HerculesCRUE/ib-hercules-rdf-validator-back](https://github.com/HerculesCRUE/ib-hercules-rdf-validator-back) [https://github.com/HerculesCRUE/ib-hercules-rdf-validator-client](https://github.com/HerculesCRUE/ib-hercules-rdf-validator-client) |
| [24-Librería de descubrimiento](./24-Librería_de_descubrimiento/README.md) | [Testing](https://reports.herculesasioizertis.desa.um.es/discovery/surefire/surefire-report.html)<br />[Cobertura](https://reports.herculesasioizertis.desa.um.es/discovery/jacoco/) | [ib-discovery](https://github.com/HerculesCRUE/ib-discovery) |
| [25-Librería de publicación](https://github.com/HerculesCRUE/ib-web-publication-backend/blob/master/README.md) | [Testing](https://reports.herculesasioizertis.desa.um.es/web-publication-backend/surefire/surefire-report.html)<br />[Cobertura](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-web-publication-backend&metric=coverage&view=list)<br /> | [ib-web-publication-backend](https://github.com/HerculesCRUE/ib-web-publication-backend) |
| [26-Test suite para publicación de datos](./26-Test_suite_para_publicación_de_datos/README.md) |                                                              | -                                                            |
| [27 Manual Test Suite para publicación de datos](./27_Manual_Test_Suite_para_publicación_de_datos/README.md) | N/A                                                          | -                                                            |
| [28-Material de formación](./28-Material_de_formación/README.md) | N/A                                                          | [Sesiones de Formacion](https://www.um.es/web/hercules/proyectos/asio/formacion/izertis) |

## 2. Otros entregables

Relación de entregables adicionales del proyecto.

| Documentación                                                | Pruebas | Repositorios |
| ------------------------------------------------------------ | ------- | ------------ |
| [00-Análisis](./00-An%C3%A1lisis)                            | N/A     | Actual       |
| [00-Arquitectura](./00-Arquitectura/architecture.md)         | N/A     | Actual       |
| [00-Testing](./00-Testing/testing.md)                        | N/A     | Actual       |
| [00-Pruebas Rendimiento](./00-Testing/Pruebas%20De%20Rendimiento.md) | N/A     | Actual       |
| [00-Memoria de publicaciones](./00-Difusión_de_contenidos/Resumen_de_publicaciones.md) | N/A     | Actual       |
| [00-Manual de despliegue](./00-Arquitectura/Manual_de_despliegue/manual_de_despliegue.md) | N/A     | Actual       |

## 3. Repositorios

Relación de repositorios del proyecto y versiones (tags o releases) asociadas.

| Repositorio                                                  | Descripción                                                  | **Hito 1** (05/2020)                                         | **Hito 1.1** (09/2020)                                       | **Hito 1.2** (12/2020)                                       | Hito 2 (05/2020) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------- |
| [ib-asio-docs-](https://github.com/HerculesCRUE/ib-asio-docs-) | Almacenamiento y entrega de documentación                    | [v1.0](https://github.com/HerculesCRUE/ib-asio-docs-/tree/v1.0) |                                                              | -                                                            | - |
| [ib-hercules-ontology](https://github.com/HerculesCRUE/ib-hercules-ontology) | Development of the ontology for the Hercules project         | [v1.0.1](https://github.com/HerculesCRUE/ib-hercules-ontology/releases/tag/v1.0.1) | -                                                            | -                                                            | - |
| [ib-shex-lite](https://github.com/HerculesCRUE/ib-shex-lite) | Shape Expression Lite Language                               | -                                                            | [v1.1](https://github.com/HerculesCRUE/ib-shex-lite/tree/v1.1) | -                                                            | - |
| [ib-hercules-sync](https://github.com/HerculesCRUE/ib-hercules-sync) | Tools to synchronise data between the ontology files and Wikibase instance | -                                                            | [v1.0](https://github.com/HerculesCRUE/ib-hercules-sync/tree/v1.0) | -                                                            | - |
| [ib-benchmarks](https://github.com/HerculesCRUE/ib-benchmarks) | Benchmark propio para evaluar el mejor sistema de almacenamiento | [v1.0.0](https://github.com/HerculesCRUE/ib-benchmarks/tree/v1.0.0) | -                                                            | -                                                            | - |
| [ib-asio-ldp](https://github.com/HerculesCRUE/ib-asio-ldp)   | Plataforma Linked Data basada en Trellis LDP                 | [1.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-asio-ldp/tree/1.0-SNAPSHOT) | -                                                            | -                                                            | [2.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-asio-ldp/tree/2.0-SNAPSHOT) |
| [ib-dataset-importer](https://github.com/HerculesCRUE/ib-dataset-importer) | Importador de datos del Dataset de Universidad de Murcia     | [1.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-dataset-importer/tree/1.0-SNAPSHOT) | -                                                            | [1.2-SNAPSHOT](https://github.com/HerculesCRUE/ib-dataset-importer/tree/1.2-SNAPSHOT) | [2.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-asio-abstractions/tree/2.0-SNAPSHOT) |
| [ib-dataset-domain-model](https://github.com/HerculesCRUE/ib-dataset-domain-model) | Modelo de dominio del Data set de Universidad de Murcia      | [1.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-dataset-domain-model/tree/1.0-SNAPSHOT) | -                                                            | [1.2-SNAPSHOT](https://github.com/HerculesCRUE/ib-dataset-domain-model/tree/1.2-SNAPSHOT) | [2.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-dataset-domain-model/tree/2.0-SNAPSHOT) |
| [ib-input-processor](https://github.com/HerculesCRUE/ib-input-processor) | Procesador de datos del módulo de entrada                    | [1.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-input-processor/tree/1.0-SNAPSHOT) | -                                                            | [1.2-SNAPSHOT](https://github.com/HerculesCRUE/ib-input-processor/tree/1.2-SNAPSHOT) | [2.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-input-processor/tree/2.0-SNAPSHOT) |
| [ib-domain-model](https://github.com/HerculesCRUE/ib-domain-model) | Modelo de dominio                                            | [1.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-domain-model/tree/1.0-SNAPSHOT) | -                                                            | [1.2-SNAPSHOT](https://github.com/HerculesCRUE/ib-domain-model/tree/1.2-SNAPSHOT) | [2.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-domain-model/tree/2.0-SNAPSHOT) |
| [ib-event-processor](https://github.com/HerculesCRUE/ib-event-processor) | Procesador de eventos del módulo de procesamiento            | [1.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-event-processor/tree/1.0-SNAPSHOT	) | [1.1-SNAPSHOT](https://github.com/HerculesCRUE/ib-event-processor/tree/1.1-SNAPSHOT) | [1.2-SNAPSHOT](https://github.com/HerculesCRUE/ib-event-processor/tree/1.2-SNAPSHOT) | [2.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-event-processor/tree/2.0-SNAPSHOT) |
| [ib-federation](https://github.com/HerculesCRUE/ib-federation) |  |  |  |  | [2.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-federation/tree/2.0-SNAPSHOT) |
| [ib-triples-storage-adapter](https://github.com/HerculesCRUE/ib-triples-storage-adapter) | Storage adapter para el almacenamiento de tripletas          | [1.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-triples-storage-adapter/tree/1.0-SNAPSHOT) | [1.1-SNAPSHOT](https://github.com/HerculesCRUE/ib-triples-storage-adapter/tree/1.1-SNAPSHOT) | [1.2-SNAPSHOT](https://github.com/HerculesCRUE/ib-triples-storage-adapter/tree/1.2-SNAPSHOT) | - |
| [ib-management-system](https://github.com/HerculesCRUE/ib-management-system) | Sistema de gestión de datos del módulo de procesamiento      | [1.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-management-system/tree/1.0-SNAPSHOT) | [1.1-SNAPSHOT](https://github.com/HerculesCRUE/ib-management-system/tree/1.1-SNAPSHOT) | [1.2-SNAPSHOT](https://github.com/HerculesCRUE/ib-management-system/tree/1.2-SNAPSHOT) | [2.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-management-system/tree/2.0-SNAPSHOT) |
| [ib-pentaho-docker](https://github.com/HerculesCRUE/ib-pentaho-docker) | Generación de imagen de Docker para Pentaho Data Integration versión 9.0 | [1.0](https://github.com/HerculesCRUE/ib-pentaho-docker/tree/1.0) | -                                                            | -                                                            | - |
| [ib-fuseki-docker](https://github.com/HerculesCRUE/ib-fuseki-docker) | Servidor SPARQL 1.1                                          | [1.0](https://github.com/HerculesCRUE/ib-fuseki-docker/tree/1.0) | -                                                            | -                                                            | - |
| [ib-discovery](https://github.com/HerculesCRUE/ib-discovery) | Librería de descubrimiento                                   | [1.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-discovery/tree/1.0-SNAPSHOT) | [v1.1-SNAPSHOT](https://github.com/HerculesCRUE/ib-discovery/tree/v1.1-SNAPSHOT) | [v1.2.0](https://github.com/HerculesCRUE/ib-discovery/tree/v1.2.0) | [2.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-discovery/tree/2.0-SNAPSHOT) |
| [ib-wikibase-docker](https://github.com/HerculesCRUE/ib-wikibase-docker) | Generación de imagen Docker para Wikibase                    | [1.0](https://github.com/HerculesCRUE/ib-wikibase-docker/tree/1.0) | -                                                            | -                                                            | - |
| [ib-web-publication-service](https://github.com/HerculesCRUE/ib-web-publication-service) | Arquetipo para el Front desarrollado en Angular              | -                                                            | [1.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-web-publication-service/tree/1.0-SNAPSHOT) | [1.2-SNAPSHOT](https://github.com/HerculesCRUE/ib-web-publication-service/tree/1.2-SNAPSHOT) | [2.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-web-publication-service/tree/2.0-SNAPSHOT) |
| [ib-web-publication-backend](https://github.com/HerculesCRUE/ib-web-publication-backend) | Arquetipo Java para API Rest con base de datos relacional    | -                                                            | -                                                            | [1.2-SNAPSHOT](https://github.com/HerculesCRUE/ib-web-publication-backend/tree/1.2-SNAPSHOT) | [2.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-web-publication-backend/tree/2.0-SNAPSHOT) |
| [ib-simulator-importer](https://github.com/HerculesCRUE/ib-simulator-importer) | Importador de datos simulados                                | [1.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-simulator-importer/tree/1.0-SNAPSHOT) | -                                                            | [1.2-SNAPSHOT](https://github.com/HerculesCRUE/ib-simulator-importer/tree/1.2-SNAPSHOT) | [2.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-simulator-importer/tree/2.0-SNAPSHOT) |
| [ib-dataset-etl](https://github.com/HerculesCRUE/ib-dataset-etl) | Proyecto ETL                                                 | [1.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-dataset-etl/releases/tag/1.0-SNAPSHOT) | -                                                            | [v1.2.0](https://github.com/HerculesCRUE/ib-dataset-etl/releases/tag/v1.2.0) | [2.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-dataset-etl/tree/2.0-SNAPSHOT) |
| [ib-uris-generator](https://github.com/HerculesCRUE/ib-uris-generator) | Factoría de URIs                                             | [v.1.0.0](https://github.com/HerculesCRUE/ib-uris-generator/releases/tag/v1.0.0) | [v.1.1.0](https://github.com/HerculesCRUE/ib-uris-generator/tree/v1.1.0) | -                                                            | [2.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-uris-generator/tree/2.0-SNAPSHOT) |
| [ib-asio-abstractions](https://github.com/HerculesCRUE/ib-asio-abstractions) | Definición de clases y constantes comunes                    | [1.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-asio-abstractions/tree/1.0-SNAPSHOT	) | [1.1-SNAPSHOT](https://github.com/HerculesCRUE/ib-asio-abstractions/tree/1.1-SNAPSHOT) | [1.2-SNAPSHOT](https://github.com/HerculesCRUE/ib-asio-abstractions/tree/1.2-SNAPSHOT) | [2.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-asio-abstractions/tree/2.0-SNAPSHOT) |
| [ib-asio-composeset](https://github.com/HerculesCRUE/ib-asio-composeset) | Despliegue en entorno de desarrollo para la Universidad de Murcia | -                                                            | -                                                            | -                                                            | - |
| [ib-api-exchange](https://github.com/HerculesCRUE/ib-api-exchange) | Sistema de gestión de datos del módulo de procesamiento para el proyecto Backend SGI (ASIO) | -                                                            | -                                                            | [1.2-SNAPSHOT](https://github.com/HerculesCRUE/ib-api-exchange/tree/1.2-SNAPSHOT) | [2.0-SNAPSHOT](https://github.com/HerculesCRUE/ib-api-exchange/tree/2.0-SNAPSHOT) |
| [ib-hercules-rdf-validator-back](https://github.com/HerculesCRUE/ib-hercules-rdf-validator-back) | Librería de validación de RDF | -                                                            | -                                                            | - | - |
| [ib-hercules-rdf-validator-client](https://github.com/HerculesCRUE/ib-hercules-rdf-validator-client) | Cliente web de la librería de validación de RDF | -                                                            | -                                                            | - | - |


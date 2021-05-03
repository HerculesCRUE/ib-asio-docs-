![](../images/logos_feder.png)

# Hito 1.2. Diciembre 2020

| Entregable                                                   | Descripción                                                  | Pruebas                                                      | Repositorios                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [24-Librería de descubrimiento](../../24-Librer%C3%ADa_de_descubrimiento/README.md) | Congelada versión [v1.2.0](https://github.com/HerculesCRUE/ib-discovery/releases/tag/v1.2.0) de la librería de descubrimiento. | [Testing](https://reports.herculesasioizertis.desa.um.es/discovery/surefire/surefire-report.html)<br/>[Cobertura](https://reports.herculesasioizertis.desa.um.es/discovery/jacoco/) | [ib-discovery](https://github.com/HerculesCRUE/ib-discovery) |
| 13 y 16-Backend SGI Software                                 | **Evolución ETL**. Versión 1.2-SNAPSHOT del Importador de datos del dataset de Murcia. | [Testing](https://reports.herculesasioizertis.desa.um.es/dataset-importer/surefire/surefire-report.html)<br/>[Cobertura](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-dataset-importer&metric=coverage&view=list) | [ib-dataset-importer](https://github.com/HerculesCRUE/ib-dataset-importer) |
| 13 y 16-Backend SGI Software                                 | **Evolución ETL**. Versión 1.2-SNAPSHOT del Procesador de datos del módulo de entrada. | [Testing](https://reports.herculesasioizertis.desa.um.es/input-processor/surefire/surefire-report.html)<br/>[Cobertura](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-input-processor&metric=coverage&view=list) | [ib-input-processor](https://github.com/HerculesCRUE/ib-input-processor) |
| 13 y 16-Backend SGI Software                                 | **Evolución ETL**. Versión 1.2-SNAPSHOT del Procesador de eventos del módulo de procesamiento. | [Testing TDD](https://reports.herculesasioizertis.desa.um.es/event-processor/surefire/surefire-report.html)<br/>[Cobertura TDD](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-event-processor&metric=coverage&view=list)<br/>[Testing BDD](https://github.com/HerculesCRUE/ib-event-processor/blob/master/docs/testing.md) | [ib-event-processor](https://github.com/HerculesCRUE/ib-event-processor) |
| 13 y 16-Backend SGI Software                                 | **Evolución del frontal**. Versión 1.2-SNAPSHOT del Front desarrollado en Angular.<br/>[Estructuras de investigación](http://herc-iz-front-desa.atica.um.es:81/main/categories/researchmentStructures): Datos mockeados<br/>[Detalle de estructuras de investigación](http://herc-iz-front-desa.atica.um.es:81/main/categories/researchmentStructures/Universidad%20Pompeu%20Fabra): Se muestran datos reales en las tablas de Producción científica, Proyectos y Patentes.<br/>[Acciones de investigación](http://herc-iz-front-desa.atica.um.es:81/main/categories/investigation-actions): Se muestran datos reales en las tablas.<br/>[Detalle de proyecto:](http://herc-iz-front-desa.atica.um.es:81/main/categories/investigation-actions/project/172) Se muestran datos mockeados, aunque algún dato del detalle es real.<br/>[Personal investigador](http://herc-iz-front-desa.atica.um.es:81/main/categories/scientist): Se muestran datos mockeados.<br /><br />`El acceso a las páginas desarrolladas, se debe realizar a través del navegador Firefox debido a una ausencia de certificado en el servidor.` | [Testing](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-web-publication-service&metric=coverage&view=list) | [ib-web-publication-service](https://github.com/HerculesCRUE/ib-web-publication-service) |
| 13 y 16-Backend SGI Software                                 | **Evolución del frontal**. Versión 1.2-SNAPSHOT del API Rest con base de datos relacional. | [Testing](https://reports.herculesasioizertis.desa.um.es/web-publication-backend/surefire/surefire-report.html)<br/>[Cobertura](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-web-publication-backend&metric=coverage&view=list)<br/>[Testing BDD](https://github.com/HerculesCRUE/ib-web-publication-backend/blob/master/docs/testing.md) | [ib-web-publication-backend](https://github.com/HerculesCRUE/ib-web-publication-backend) |
| 13 y 16-Backend SGI Software                                 | **Ampliación operaciones CRUD**. Versión 1.2-SNAPSHOT del Storage adapter para el almacenamiento de tripletas. | [Testing](https://reports.herculesasioizertis.desa.um.es/triples-storage-adapter/surefire/surefire-report.html)<br/>[Cobertura](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-triples-storage-adapter&metric=coverage&view=list) | [ib-triples-storage-adapter](https://github.com/HerculesCRUE/ib-triples-storage-adapter) |
| 13 y 16-Backend SGI Software                                 | **Ampliación operaciones CRUD**. Versión 1.2-SNAPSHOT del Sistema de gestión de datos del módulo de procesamiento. | [Testing TDD](https://reports.herculesasioizertis.desa.um.es/management-system/surefire/surefire-report.html)<br/>[Cobertura TDD](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-management-system&metric=coverage&view=list)<br/>[Testing BDD](https://github.com/HerculesCRUE/ib-management-system/blob/master/docs/testing.md) | [ib-management-system](https://github.com/HerculesCRUE/ib-management-system) |
| 13 y 16-Backend SGI Software                                 | **Sincronización entre AS e IO**. Sistema de gestión entre Infraestructura Ontológica y Arquitectura Semántica. | [Testing](https://reports.herculesasioizertis.desa.um.es/api-exchange/surefire/surefire-report.html)<br/>[Cobertura](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-api-exchange&metric=coverage&view=list)<br/>[Testing BDD](https://github.com/HerculesCRUE/ib-api-exchange/blob/master/docs/testing.md) | [ib-api-exchange](https://github.com/HerculesCRUE/ib-api-exchange) |
| [07-Control de versiones OWL](../../07-Control_de_versiones_OWL/01_ontology_continuous_integration) | **Integración continua Shapes**. [Control de versiones sobre ontologías OWL](../../07-Control_de_versiones_OWL/01_ontology_continuous_integration/ontoloci.md). Métodos de integración continua de ontologías y su integración con el sistema de control de versiones GitHub. | En proceso                                                   | [ontology-ci](https://github.com/HerculesCRUE/ontology-ci)   |
| [00-Arquitectura](../../00-Arquitectura/architecture.md)     | **Integración con SIR**. [Autenticación y Autorización](../../00-Arquitectura/Autenticacion_autorizacion/README.md). Elección de infraestructura y diseño de la solución. | -                                                            | -                                                            |
| [00-Arquitectura](../../00-Arquitectura/architecture.md)     | [Diseño/solución federación de entidades](../../00-Arquitectura/Federaci%C3%B3n/ASIO_Izertis_Federaci%C3%B3n.md). Análisis de alternativas para la federación de consultas sobre una arquitectura de nodos distribuidos en la red HERCULES | -                                                            | -                                                            |
| [00-Arquitectura](../../00-Arquitectura/architecture.md)     | [Auditoría de calidad de código](https://github.com/HerculesCRUE/ib-asio-docs-/tree/master/00-Arquitectura/Auditoria_de_codigo). Análisis de la situación actual y siguientes pasos. | -                                                            | -                                                            |

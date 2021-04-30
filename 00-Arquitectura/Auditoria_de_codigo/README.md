![](./resources/logos_feder.png)



| Fecha        | 29/04/2021                                                   |
| ------------ | :----------------------------------------------------------- |
| Revisado por | Paloma Terán Pérez                                           |
| Módulo       | Auditoría de calidad de código                               |
| Tipo         | Documento                                                    |
| Objetivo     | Documento con información sobre la auditoría de calidad de código |



# Auditoría de calidad de código

## Introducción

Uno de los puntos principales para alcanzar los objetivos que marca DevOps, es la coordinación del trabajo realizado por el equipo de desarrolladores. Es en este momento cuando entra en juego el concepto de integración continua cuyo objetivo principal es coordinar e integrar el trabajo de todo el equipo de desarrollo de software de cada proyecto de forma frecuente, para así poder detectar los posibles fallos del software en una fase muy temprana, lo cual permite reducir drásticamente el número de posibles bugs que pueda contener la aplicación.

Con la integración continua, se evitan los problemas derivados de que un equipo de desarrolladores trabaje de forma simultánea sobre un mismo proyecto. Para ello es estrictamente necesario definir las tareas de forma concisa e intentando fraccionar y encapsular los cambios para que estos puedan ser integrados de forma regular, que permita ejecutar una serie de tareas de compilación, calidad y testeo para asegurar la calidad del producto.

Una vez los desarrolladores han terminado una nueva versión de la aplicación, pueden revisar todos los tests realizados, así como ver de forma detallada los puntos débiles del proyecto como errores potenciales en el código, escasez de comentarios, clases demasiado complejas, escasez de cobertura de las pruebas unitarias, etc. 

## Proceso de adaptación

Actualmente el análisis estático se está llevando utilizando herramientas propias de cada uno de los equipos. Esto puede implicar que en algunas ocasiones estas herramientas no tengan un acceso público para poder visualizar los resultados del análisis y por otro que no exista una homogeneización de las herramientas utilizadas. 

Se propone un proceso de adaptación para que todos los proyectos/repositorios utilicen las mismas herramientas, pasando por las siguientes fases:

1. Planificación y diseño de las herramientas a utilizar
2. Hacer públicos los resultados que se encuentran en herramientas privadas 
3. Estudio sobre unificación de herramientas  entre diferentes proyectos, ampliando las indicadas en este documento si es necesario
4. Implementación final

## Evidencias auditoría

| Proyecto                                                                                | Evidencias |
| --------------------------------------------------------------------------------------- | ---------- |
| [dataset-importer](https://github.com/HerculesCRUE/ib-dataset-importer)                 | [Análisis estático](https://sonarcloud.io/dashboard?id=HerculesCRUE_ib-dataset-importer)<br />[Testing](https://reports.herculesasioizertis.desa.um.es/dataset-importer/surefire/surefire-report.html)<br />[Cobertura](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-dataset-importer&metric=coverage&view=list) |
| [discovery](https://github.com/HerculesCRUE/ib-discovery)                               | [Análisis estático](https://sonarcloud.io/dashboard?id=HerculesCRUE_ib-discovery)<br />[Testing](https://reports.herculesasioizertis.desa.um.es/discovery/surefire/surefire-report.html)<br />[Cobertura](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-discovery&metric=coverage&view=list) |
| [event-processor](https://github.com/HerculesCRUE/ib-event-processor)                   | [Análisis estático](https://sonarcloud.io/dashboard?id=HerculesCRUE_ib-event-processor)<br />[Testing](https://reports.herculesasioizertis.desa.um.es/event-processor/surefire/surefire-report.html)<br />[Cobertura](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-event-processor&metric=coverage&view=list)<br />[BDD](https://reports.herculesasioizertis.desa.um.es/event-processor/cucumber/overview-features.html) |
| [input-processor](https://github.com/HerculesCRUE/ib-input-processor)                   | [Análisis estático](https://sonarcloud.io/dashboard?id=HerculesCRUE_ib-input-processor)<br />[Testing](https://reports.herculesasioizertis.desa.um.es/input-processor/surefire/surefire-report.html)<br />[Cobertura](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-input-processor&metric=coverage&view=list)<br />[BDD](https://reports.herculesasioizertis.desa.um.es/input-processor/cucumber/overview-features.html) |
| [management-system](https://github.com/HerculesCRUE/ib-management-system)               | [Análisis estático](https://sonarcloud.io/dashboard?id=HerculesCRUE_ib-management-system)<br />[Testing](https://reports.herculesasioizertis.desa.um.es/management-system/surefire/surefire-report.html)<br />[Cobertura](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-management-system&metric=coverage&view=list)<br />[BDD](https://reports.herculesasioizertis.desa.um.es/management-system/cucumber/overview-features.html) |
| [triples-storage-adapter](https://github.com/HerculesCRUE/ib-triples-storage-adapter)   | [Análisis estático](https://sonarcloud.io/dashboard?id=HerculesCRUE_ib-triples-storage-adapter)<br />[Testing](https://reports.herculesasioizertis.desa.um.es/triples-storage-adapter/surefire/surefire-report.html)<br />[Cobertura](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-triples-storage-adapter&metric=coverage&view=list)<br />[BDD](https://reports.herculesasioizertis.desa.um.es/triples-storage-adapter/cucumber/overview-features.html) |
| [uris-generator](https://github.com/HerculesCRUE/ib-uris-generator)                     | [Análisis estático](https://sonarcloud.io/dashboard?id=HerculesCRUE_ib-uris-generator)<br />[Testing](https://reports.herculesasioizertis.desa.um.es/uris-generator/surefire/surefire-report.html)<br />[Cobertura](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-uris-generator&metric=coverage&view=list) |
| [api-exchange](https://github.com/HerculesCRUE/ib-api-exchange)                         | [Análisis estático](https://sonarcloud.io/dashboard?id=HerculesCRUE_ib-api-exchange)<br />[Testing](https://reports.herculesasioizertis.desa.um.es/api-exchange/surefire/surefire-report.html)<br />[Cobertura](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-api-exchange&metric=coverage&view=list)<br />[BDD](https://reports.herculesasioizertis.desa.um.es/api-exchange/cucumber/overview-features.html) |
| [web-publication-backend](https://github.com/HerculesCRUE/ib-web-publication-backend)   | [Análisis estático](https://sonarcloud.io/dashboard?id=HerculesCRUE_ib-web-publication-backend  )<br />[Testing](https://reports.herculesasioizertis.desa.um.es/web-publication-backend/surefire/surefire-report.html)<br />[Cobertura](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-web-publication-backend&metric=coverage&view=list)<br />[BDD](https://reports.herculesasioizertis.desa.um.es/web-publication-backend/cucumber/overview-features.html) |
| [web-publication-service](https://github.com/HerculesCRUE/ib-web-publication-service)   | [Análisis estático](https://sonarcloud.io/dashboard?id=HerculesCRUE_ib-web-publication-service)<br />[Cobertura](https://sonarcloud.io/component_measures?id=HerculesCRUE_ib-web-publication-service&metric=coverage&view=list) |

\* Para poder acceder a los servicios alojados bajo `https://reports.herculesasioizertis.desa.um.es` se recomienda el uso de Firefox para evitar problemas con el certificado SSL. Esta circunstancia se solucionará cuando se configura SSL en el servidor.

## Estudio de herramientas

Se ha confeccionado un documento incluyendo el [estudio de las herramientas a utilizar](./tooling.md).
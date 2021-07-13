![](./images/logos_feder.png)

# Manual de usuario



| Entregable     | Manual de usuario                                            |
| -------------- | ------------------------------------------------------------ |
| Fecha          | 13/07/2021                                                  |
| Revisado por   | Hugo Pintado Pérez                                           |
| Proyecto       | [ASIO](https://www.um.es/web/hercules/proyectos/asio) (Arquitectura Semántica e Infraestructura Ontológica) en el marco de la iniciativa [Hércules](https://www.um.es/web/hercules/) para la Semántica de Datos de Investigación de Universidades que forma parte de [CRUE-TIC](https://tic.crue.org/hercules/) |
| Módulo         | Manual de usuario                                            |
| Tipo           | Documento                                                    |
| Objetivo       | Documento destiando a dar asistencia a las personas que utilcen el sistema ASIO. |
| Estado         | **100%**                                                     |
| Próximos pasos |                                                              |



# ÍNDICE


[1. Introducción](#introduccion)

[2. Acceso a la aplicación](#acceso)

[3. Acceso Público](#accesopublico)

[3.1. Estructuras de investigación](#estructurasinvestigacion)

[3.2. Personal investigador](#personalinvestigador)

[3.3.  Áreas](#areas)

[3.4.  Producción científica](#produccioncientifica)

[3.5.  Acciones de investigación](#accionesinvestigacion)

[3.6.  Estadísticas](#estadisticas)

[3.7. Consultas Sparql](#consultassparql)

[3.8. Linked Data Graph](#linkeddata)

[3.9. Instalador](#instalador)

[3.10. Enlaces](#enlaces)

[3.11. Información](#informacion)

[4. Acceso Privado](#accesoprivado)

[4.1. Consultas Sparql](#consultassparqlprivado)

[4.2. Libreria descubrimiento](#libreriadescubrimiento)

[4.3. Factoría de URIs](#factoriauris)

[4.4. Monitor Backends](#monitorbackends)

[4.5. Importador de datos](#importador)

[4.6. Borrado de datos](#borrado)

[4.7. Validadores](#validadores)

[4. Trellis](#trellis)

[5. Wikibase](#wikibase)

[6. Pantallas](#pantallas)


<a name="introduccion"></a>
# 1. Introducción

Este documento, pretende ser el manual de ayuda para los usuarios que utilicen el sistema ASIO. En este documento se explicarán todas las funcionalidades que se encuentran en la interfaz web, desde el punto de vista del usuario que entra en la aplicación.

Desde este sitio web, se podrán consultar los resultados del proyecto Hércules ASIO. En esta interfaz existe una parte pública, que podrá ser accesible para cualquier usuario y podrá consultar la información almacenada en el sistema. Y una parte privada, a la que accederá solamente el personal autorizado, con un usuario y contraseña.

<a name="acceso"></a>
# 2. Acceso a la aplicación

La aplicación se ejecuta en un entorno web. Los requisitos para poder utilizarla son: disponer de un equipo con conexión a Internet, un navegador web de última generación (Chrome, Firefox, Edge, etc.). No es necesario que el usuario realice la instalación de ningún otro software.
Para acceder a la aplicación basta con introducir la siguiente dirección en el navegador:
- Entorno de desarrollo: https://linkeddata1desa.um.es/
- Entorno de preproducción: https://linkeddata1.um.es/

Desde la pantalla de inicio se podrán acceder a todas las secciones de la aplicación. 

Se podrá acceder desde las secciones centrales, como desde las diferentes entradas del menú.

A continuación se detallan las diferentes secciones a las que se puede acceder desde la parte pública, es decir cualquier usuario podría acceder a ellas:

- Estructuras de investigación
- Personal investigador
- Áreas
- Producción científica
- Acciones de investigación
- Estadísticas
- Consultas SPARQL
- Instalador
- Enlaces
- Información

(./images/iniciopublica.png)

Y las secciones a las que se podrá acceder desde la parte privada, además de las anteriores, es decir una vez logueado con un usuario y contraseña, son las siguientes:

- Gestión de usuarios
- Importador de datos
- Borrado de datos
- Factoría de URIs
- Librería de descubrimiento
- Monitor de Backends


A continuación, se explica cada una de las secciones, agrupadas por acceso público y privado

<a name="accesopublico"></a>
# 3. Acceso Público

Cualquier usuario, sin necesidad de loguearse en el sistema podrá acceder a la información pública del sistema.
A continuación, se detallan las secciones que podrá consultar:

<a name="estructurasinvestigacion"></a>
## 3.1. Estructura de investigación

En esta sección, podremos ver información general sobre las diferentes estructuras de investigación. Las estructuras de investigación, pueden ser de los siguientes tipos:

- Centros

- Universidades

- Fundaciones

- Empresa

- etc

Como se ha explicado en el punto anterior, se podrá acceder a ella a través de la pantalla de inicio o desde el menú de la parte izquierda.

La pantalla dispondrá de una serie de filtros:

- Las diferentes opciones que hay dentro de las estructuras de organización: Universidad, centro, etc. Si se selecciona una de estas sub-opciones, mostrará la información filtrada por ese tipo de estructura en la tabla.
- Un buscador general por nombre de centro.

![Captura de estructuras de investigación](./images/screenshots/estructuras.png)



La información que se muestra en esta página tratará de responder, entre otras, a las siguientes preguntas de competencia:

| Pregunta de competencia                                      |
| ------------------------------------------------------------ |
| CQ01. Como usuario requiero obtener un listado de los centros/estructuras de investigación que trabajan en un área/disciplina específica |
| CQ04. Como usuario requiero obtener el Top 10 (o el número que se considere relevante pues será parametrizable) de centros/estructuras de investigación que posean sellos de calidad asociados, por ejemplo: el sello Severo Ochoa. |
| CQ05. Como usuario requiero obtener un listado de los centros/estructuras de investigación que hayan realizado proyectos H2020 y/o proyectos del Plan Estatal. |
| CQ12. Como usuario necesito conocer el porcentaje de participación de un centro/estructura de investigación en proyectos nacionales o europeos. |


### Detalle de una estructura de investigación

Pulsando sobre un centro de investigación en el listado, la web redirigirá a la información de esa estrutura de investigación.
De cada estructura de investigación, se podrá consultar el listado de los investigadores y patentes asociados a dicha estructura.

- **Personal investigador**

![Captura de detalle de una estructuras de investigación - tab personal investigador](./images/screenshots/detalle-estructuras-personal.png)


- **Patentes**

![Captura de detalle de una estructuras de investigación - tab patentes](./images/screenshots/detalle-estructuras-patentes.png)



En esta pantalla se responde a las siguientes preguntas de competencia:

| Pregunta de competencia                                      |
| ------------------------------------------------------------ |
| CQ02. Como usuario requiero obtener un listado de los investigadores de un centro/estructura de investigación de un área/disciplina específica. Este listado podrá filtrarse según el tipo de investigador ya sea docente, personal investigador en formación, etc. |
| CQ03. Como usuario requiero obtener el Top 10 (o el número que se considere relevante pues será parametrizable) de los investigadores de un centro/estructura de investigación ordenados por el número de citas, número de publicaciones, h-index, etc. en un área/disciplina específica. |
| CQ06. Como usuario requiero obtener un listado de la producción científica en un determinado rango de fechas de un centro/estructura de investigación en un área/disciplina. Para cada resultado se incluirán algunos metadatos importantes de la producción como, por ejemplo, DOI, año de publicación, etc. |
| CQ09. Como usuario requiero obtener un listado de patentes, diseños industriales, etc. de un centro/estructura de investigación en un área/disciplina. |
| CQ10. Como investigador y personal no investigador de la universidad requiero obtener un listado de los proyectos adjudicados/desarrollados, de un centro/estructura de investigación, de un área/disciplina. |
| CQ12. Como usuario necesito conocer el porcentaje de participación de un centro/estructura de investigación en proyectos nacionales o europeos. |
| CQ17. Como usuario necesito obtener el listado de indicadores con su respectivo valor y unidad de medida (porcentaje, número, etc.) calculados en un periodo de tiempo, ya sea para toda la universidad o para cada centro/estructura de investigación de cada universidad. |

<a name="personalinvestigador"></a>
## 3.2. Personal investigador


Se muestra el personal investigador filtrado por áreas y tipo, se podrá ordenar, cambiar el número de resultados, etc.

![Captura de personal investigador](./images/screenshots/personal-investigador.png)


Se utilizan las siguientes preguntas de competencia para el diseño de la pantalla:

| Pregunta de competencia                                      |
| ------------------------------------------------------------ |
| CQ02. Como usuario requiero obtener un listado de los investigadores de un centro/estructura de investigación de un área/disciplina específica. Este listado podrá filtrarse según el tipo de investigador ya sea docente, personal investigador en formación, etc. |
| CQ03. Como usuario requiero obtener el Top 10 (o el número que se considere relevante pues será parametrizable) de los investigadores de un centro/estructura de investigación ordenados por el número de citas, número de publicaciones, h-index, etc. en un área/disciplina específica. [As a user I would like to obtain the Top 10 (or any relevant number, as this would be a parameter) research centers/strutures who have quality seals associated, such as the Severo Ochoa seal.] |
| CQ45. Investigadores que dirigen tesis en programas de doctorado diferentes a los de su Universidad, y cuántas de esas tesis dirigidas han obtenido mención cum laude. |
|                                                              |



### Detalle de personal investigador


- **Acciones de investigación**

![Captura de personal investigador](./images/screenshots/detalle-personal-investigador-acciones.png)


- **Publicaciones científicas**

![Captura de personal investigador](./images/screenshots/detalle-personal-investigador-publicaciones-cientificas.png)


- **Publicaciones académicas**

![Captura de personal investigador](./images/screenshots/detalle-personal-investigador-publicaciones-academicas.png)


- **Eventos**

![Captura de personal investigador](./images/screenshots/detalle-personal-investigador-eventos.png)



<a name="areas"></a>
# 3.3. Áreas



En esta pantalla se muestra información sobre los datos del módulo vertical "áreas de conocimiento".



![Captura áreas](./images/screenshots/areas.png)



<a name="produccioncientifica"></a>
# 3.4. Producción científica


En esta pantalla, se muestran las publicaciones y los eventos de investigaciones.



## Publicaciones científicas



![Publicaciones científicas](./images/screenshots/produccion-cientifica-publicaciones-cientificas.png)

Se podrá acceder al detalle de cada publicación científica pulsando en cada item del listado.


## Publicaciones académicas


![Publicaciones académicas](./images/screenshots/produccion-cientifica-publicaciones-academicas.png)

Se podrá acceder al detalle de cada publicación académica pulsando en cada item del listado.

## Otras publicaciones


![Otros publicaciones](./images/screenshots/produccion-cientifica-otros-documentos.png)

Se podrá acceder al detalle de cada publicación pulsando en cada item del listado.

## Eventos

![Eventos](./images/screenshots/produccion-cientifica-eventos.png)

Se podrá acceder al detalle de cada evento pulsando en cada item del listado.


<a name="accionesinvestigacion"></a>
# 3.5. Acciones de investigación



Se divide en dos secciones: Patentes y Proyectos


## Patentes

En esta sección de acciones de investigación se podrán ver las patentes filtradas por nombre y por ámbito.

![Captura de acciones de investigación - tab proyectos](./images/screenshots/acciones-investigacion-patentes.png)

Se podrá acceder al detalle de cada patente pulsando en cada item del listado.

## Proyectos


La tabla podrá ser filtrada por año y por nombre.


![Captura de acciones de investigación - tab documentos](./images/screenshots/acciones-investigacion-proyectos.png)

Se podrá acceder al detalle de cada proyecto, pulsando en cada item del listado. En dicho detalle, se podrá consultar la información general del proyecto y los participantes del mismo.

En esta página se muestra la información de las preguntas de competencia relacionadas con proyectos. 

| Pregunta de competencia                                      |
| ------------------------------------------------------------ |
| CQ10. Como investigador y personal no investigador de la universidad requiero obtener un listado de los proyectos adjudicados/desarrollados, de un centro/estructura de investigación, de un área/disciplina, en un determinado año de búsqueda en los que se tenga acceso al detalle de al menos:<br/>○	Nombre del proyecto<br/>○	Palabras claves<br/>○	Tipo de participación: coordinador o participante<br/>○	Tipo de proyecto: competitivo o no competitivo<br/>○	Tipo de financiamiento: público o privado.<br/>○	Tipo de convocatoria: nacional, H2020, etc.<br/>○	Número y listado de personas involucradas en el proyecto<br/>○	Nombre(s) del investigador(s) principal<br/>○	Entregables/memoria del proyecto<br/>○	Producción científica relacionada con el proyecto<br/>○	Entidades colaboradoras/participantes<br/>○	Cuantía<br/>○	etc. |
| CQ46. Estado del arte: ¿puedo ver los resultados de proyectos por temática concreta de proyectos desarrollados en la red, diferenciando a nivel regional, nacional, europeo? |
| CQ13. Como investigador, personal no investigador de la universidad requiero insertar/modificar los datos relacionados con los proyectos de investigación, incluyendo los entregables que se hayan generado en la fase de propuesta. El usuario tendrá acceso a esta información según el nivel de acceso que se le haya proporcionado previamente según su rol, según niveles de confidencialidad de ser el caso. Entre los datos que se proporcionarán por cada proyecto se tendrá al menos:<br/>○	Nombre del proyecto<br/>○	Palabras claves<br/>○	Tipo de participación de la entidad: coordinador o participante<br/>○	Tipo de proyecto: competitivo o no competitivo<br/>○	Tipo de financiamiento: público o privado<br/>○	Tipo de convocatoria: nacional, H2020, etc.<br/>○	Número y listado de personas involucradas en el proyecto<br/>○	Nombre(s) del investigador(s) principal<br/>○	Entregables/memoria del proyecto<br/>○	Producción científica relacionada con el proyecto<br/>○	Entidades colaboradoras/participantes<br/>○	Cuantía<br/> |
| CQ14. Como usuario necesito una visualización [filtering] que me permita explorar la información de cada proyecto según los filtros que haya elegido, por ejemplo, por años, por tipo de convocatoria, por cuantía mayor a determinado valor, según un área/disciplina, según la ubicación geográfica, etc. |

<a name="estadisticas"></a>
# 3.6. Estadísticas

El objetivo de esta sección es que se muestren estadísticas, en base a los datos del sistema.

![Estadisticas](./images/screenshots/estadisticas.png)

En este documento, se explica como poder añadir un nuevo gráfico de estadísticas.


<a name="consultassparql"></a>
# 3.7. Consultas SparQL

A través de esta sección, se podrán visualizar, ejecutar y mantener las consultas de competencia y/o consultas SPARQL predefinidas.
Esta sección, a diferencia de las anteriores, varía si se accede de forma pública o privada. A continuación, se explican las funcionades de la parte pública, y en el apartado 4.1 las funcionalidades que pueden realizarse por un usuario logueado.

- No se podrán guardar consultas
- No se podrán consultas federadas

Al entrar en la pantalla, veremos que está dividida en dos partes
![SparQL](./images/screenshots/sparqlpublica.png)
Una parte superior donde se podrán lanzar consultas sparql y ver los resultados y una parte inferior donde se podrán consultar las consultas predefinidas.


<a name="linkeddata"></a>
# 3.8. Linked Data Graph

<a name="instalador"></a>
# 3.9. Instalador


<a name="enlaces"></a>
# 3.10. Enlaces

<a name="informacion"></a>
# 3.11. Información

<a name="accesoprivado"></a>
# 4. Acceso privado
Para loguearse en el sistema, deberá accederse a la parte superior derecha y pulsar en "Acceder", ahí deberá introducir el nombre de usuario y contraseña.
Cuando el usuario introduzca estos datos y pulse el botón "Log In", la aplicación comprobará si los datos introducidos son correctos. Si estos datos son correctos entonces se mostrarán más secciones en el menu y en la pantalla de inicio.

<a name="consultassparqlprivado"></a>
# 4.1. Consultas SparQL

Además de tener las mismas funcionalidades comentadas en el apartado 3.7, si el usuario está logueado, podrá además:
- Guardar consultas
- Lanzar consultas federadas. 

![SparQL](./images/screenshots/sparqlprivada.png)
Se tiene la posibilidad de ejecutar una consulta sparQL y guardar dicha consulta que ha diseñado pulsando el botón “Guardar”, al pulsarlo se le solicitará un nombre identificativo de la consulta:

![Guardar SparQL](./images/screenshots/guardarconsulta.png)

En la mitad inferior de la pantalla se cuenta con un panel para la administración y uso de las consultas sparQL almacenadas. Desde él podrá filtrar las consultas, tanto las propias como las predefinidas en el sistema.
Una vez localizada la consulta que le interese utilizar, se podrá cargar en el formulario sparQL para su posterior uso pulsando sobre el botón “Usar”.
Para las consultas propias, existe la opción de borrar, no así para las predefinidas del sistema.

![Consultas guardadas](./images/screenshots/consultas guardadas.png)

<a name="libreriadescubrimiento"></a>
# 4.2. Librería de descubrimiento

<a name="factoriauris"></a>
# 4.3. Factoría de URIs

<a name="monitorbackends"></a>
# 4.4. Monitor Backends

<a name="importador"></a>
# 4.5. Importador de datos


Se dispone de dos importadores diferentes, unos para jobs y otro para CVNs. Para ambos hay que lanzar un proceso, diferente para cada uno, desde el servidor, en el lugar en el que se encuentre el fichero .jar del proyecto dataset-importer. Para más información, mirar el documento [README.md](https://github.com/HerculesCRUE/ib-dataset-importer/blob/master/README.md) del proyecto.

Al lanzar cualquiera de los dos procesos, se inicializa la importación tanto en Trellis como en Wikibase, ambos procesos pueden llevar algo de tiempo por lo que los resultados de la importación pueden tardar en verse en ambos.



Importador de Datasets
---------------------------

El importador de Datasets, importa los datos a partir de los ficheros XML proporcionados por la UM. El proceso que hay que lanzar para iniciar el procesado de estos ficheros es: 

```
java -jar -Dspring.batch.job.names=importDataSetJob {jar-name}.jar
```



## Importador de CVNs

El importador de CVNs, importa los datos a partir de los servicios mockeados proporcionados por la UM. El proceso que hay que lanzar para iniciar el procesado de estos ficheros es: 

```
java -jar -Dspring.batch.job.names=importCvnJob {jar-name}.jar
```



## Importador SGI

El importador de SGI importa los datos a partir de unos servicios implementados por el protocolo OAI-PMH.

El repositorio de este servicio se puede consultar en [oah-pmh](https://github.com/HerculesCRUE/oai-pmh). El proceso que hay que lanzar para iniciar el procesado de estos ficheros es: 

```
java -jar -Dspring.batch.job.names=importOaipmhJob {jar-name}.jar
```

<a name="borrado"></a>
# 4.6. Borrado de datos

<a name="validadores"></a>
# 4.7. Validadores


<a name="trellis"></a>
# 5. Trellis

Para acceder a la máquina de Trellis se necesita usuario y contraseña de la UM y se accede a través de la siguiente dirección:

- Entorno de desarrollo: https://ldpld1desa.um.es
- Entorno de preproducción: https://ldpld1.um.es


Al acceder a Trellis se nos muestra una pantalla con el listado de datos que tenemos en el Triplestore, como se puede ver en la siguiente imagen:

![arquitectura](./images/listado-trellis.png)

Al pulsar sobre cualquiera de las entradas, se muestra el detalle:

![arquitectura](./images/detalle-trellis.png)


<a name="wikibase"></a>
# 6. Wikibase

A través de la plataforma de Wikibase podemos acceder también a los datos importados:
`http://wb.herculesasioizertis.desa.um.es/`



Desde la opción de "Cambios Recientes" se pueden consultar los últimos cambios en los datos y acceder a ellos.

![arquitectura](./images/cambios-wikibase.png)



Se pueden ver los detalles pulsando sobre estos datos, o sobre los resultados de una consulta SparQL.

![arquitectura](./images/detalles-wikibase.png)



A través de las consultas SparQL también se podrán obtener los datos que nos interesen:

`http://wbquery.herculesasioizertis.desa.um.es/`

![arquitectura](./images/consulta-wikibase.png)



### Ejemplos de consultas de Wikibase:

```
#Proyectos y su grupo de investigación
SELECT ?nombreProyecto ?descripcionGrupoInvestigacion
WHERE
{
   ?proyecto wdt:P3 "http://hercules.org/um/es-ES/rec/Proyecto/".
   OPTIONAL { ?proyecto wdt:P13/wdt:P4 ?descripcionGrupoInvestigacion }
   ?proyecto wdt:P11 ?nombreProyecto.
}
```

```
#Proyectos con y sin grupo de investigacion
SELECT ?proyectoLabel ?grupoInvestigacionLabel
WHERE
{
   ?proyecto wdt:P3 "http://hercules.org/um/es-ES/rec/Proyecto/".
   OPTIONAL { ?proyecto wdt:P13 ?grupoInvestigacion }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
}
```

```
#Número de proyectos por grupo de investigacion (incluye desconocidos)
#defaultView:BubbleChart
SELECT ?grupoInvestigacion (COUNT(?proyecto) AS ?count)
WHERE
{
   ?proyecto wdt:P3 "http://hercules.org/um/es-ES/rec/Proyecto/";
   OPTIONAL { ?proyecto wdt:P13/wdt:P4 ?grupoInvestigacion }.
   BIND(IF(BOUND(?grupoInvestigacion),?grupoInvestigacion,"Desconocido") AS ?grupoInvestigacion).
}
GROUP BY ?grupoInvestigacion
```

```
#Proyectos con grupo de investigacion
SELECT ?proyectoLabel ?grupoInvestigacionLabel
WHERE
{
   ?proyecto wdt:P3 "http://hercules.org/um/es-ES/rec/Proyecto/".
   ?proyecto wdt:P13 ?grupoInvestigacion
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
}
```





Para más información sobre como manejar Wikibase se puede consultar la guía de [Wikidata](https://www.wikidata.org/wiki/Help:Contents).



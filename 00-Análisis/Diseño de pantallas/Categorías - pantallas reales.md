![](./images/logos_feder.png)



| Fecha        | 29/04/2021                                                   |
| ------------ | ------------------------------------------------------------ |
| Revisado por | Paloma Terán Pérez                                           |
| Módulo       | Pantallas reales                                             |
| Tipo         | Documento                                                    |
| Objetivo     | Documento con las pantallas reales realizadas a partir de los análisis |



# Pantallas reales



**Índice**

[1. Introducción](#1.-introducción)

[2. Home](#home)

[3. Categorías](#categorías)

[3.1. Estructura de investigación](#estructura-de-investigación)

[3.1.1. Detalle de una estructura de investigación](#detalle-de-una-estructura-de-investigación)

[3.2. Acciones de investigación](#acciones-de-investigación)

[3.2.1. Detalle de una acción de investigación](#detalle-de-una-acción-de-investigación)

[3.3. Personal investigador](#personal-investigador)

[3.3.1  Detalle de personal investigador](#detalle-de-personal-investigador)

[3.4.  Áreas](#areas)

[3.5.  Producción científica](#producción-científica)

[3.5.1.  Detalle de producción científica](#detalle-de-producción-científica)

[3.6.  Estadísticas](#estadísticas)



# 1. Introducción

En este documento se pueden encontrar capturas de pantalla realizadas de la parte frontal de la aplicación, a partir del [análissis](./Categorías y buscador.md) realizado previamente. Es importante recalcar que estas pantallas han ido evolucionándo acorde a la ontolología fusionada, y no tienen por qué coincidir con los mocks de pantallas realizados en el analisis.



El enlace al frontal lo tenemos aquí: [https://app.herculesasioizertis.desa.um.es/](https://app.herculesasioizertis.desa.um.es/)




2. Home
============

El home de la web dispone de un menú superior con los accesos a las diferentes categorías y a la pantalla de consultas SparQL. También se mostrarán los iconos de login/acceso o la imagen del usuario identificado. Las opciones que no estén funcionando, se mostrarán desactivadas en gris, tanto en el home como en el menú lateral.



Dentro del propio Home se podrán ver:

- Las categorías, que serían:
  - Estructuras de investigación
  - Personal investigador
  - Áreas
  - Producción científica
  - Acciones de investigación
  - Estadísticas e indicadores
- Al final de la página se mostrarán los enlaces a información del proyecto en general:
  - Repositorios
  - Validadores
  - Información del contrato de URIs
  - Backends SGI
  - Renderización de metadatos de Named Graphs
  - Información sobre el proyecto Hércules+
  - Datos de contacto







![home - front](./images/screenshots/home.png)



Una vez el usuario se logee, se mostrarán dos opciones más en el home:

- Los servicios de los que dispone la web, como las consultas SparQL y gestiones propias de usuarios administradores. Por ejemplo la gestión de usuarios, que sólo sería visible para usuarios de tipo Gestor Asio.

  

![home - front](./images/screenshots/home-login.png)





# 3. Categorías



En cada categoría se mostrarán una serie de filtros, algunos comunes para varias categorías.

Para el filtro por áreas, se utilizará un componente para mostrar un árbol y se utilizará el módulo vertical "[subject áreas](https://github.com/weso/hercules-ontology/blob/master/src/asio-module-subjectareas.ttl)":



![](./images/areas.png)



## 3.1. Estructura de investigación



En la categoría de estructura de investigación, podremos ver información general sobre las diferentes estructuras de investigación:

- Centros

- Universidades

- Fundaciones

- Empresa

- etc

  

Se podrá acceder a ella a través de la pantalla home, o del menú superior.

La pantalla dispondrá de una serie de filtros:

- Las diferentes opciones que hay dentro de las estructuras de organización: Universidad, centro, etc. Si se selecciona una de estas sub-opciones, mostrará la información filtrada por ese tipo de estructura en la tabla.
- Un buscador general por nombre de centro.



![Captura de estructuras de investigación](./images/screenshots/estructuras.png)



La información que se mostrará en esta página tratará de responder, entre otras, a las siguientes preguntas de competencia:

| Pregunta de competencia                                      |
| ------------------------------------------------------------ |
| CQ01. Como usuario requiero obtener un listado de los centros/estructuras de investigación que trabajan en un área/disciplina específica |
| CQ04. Como usuario requiero obtener el Top 10 (o el número que se considere relevante pues será parametrizable) de centros/estructuras de investigación que posean sellos de calidad asociados, por ejemplo: el sello Severo Ochoa. |
| CQ05. Como usuario requiero obtener un listado de los centros/estructuras de investigación que hayan realizado proyectos H2020 y/o proyectos del Plan Estatal. |
| CQ12. Como usuario necesito conocer el porcentaje de participación de un centro/estructura de investigación en proyectos nacionales o europeos. |



## 3.1.1. Detalle de una estructura de investigación

Pulsando sobre un centro de investigación en la pantalla de esta categoría, la web nos redirigirá a la información de esa estrutura de investigación. Para facilitar la visualización de los datos sobre la estructura de investigación, la información se mostrará agrupada por [tabs](https://getbootstrap.com/docs/4.0/components/navs/).



### Sección de personal investigador



![Captura de detalle de una estructuras de investigación - tab personal investigador](./images/screenshots/detalle-estructuras-personal.png)





### Sección de publicaciones científicas



![Captura de detalle de una estructuras de investigación - tab publicaciones científicas](./images/screenshots/detalle-estructuras-publicaciones-cientificas.png)





### Sección de publicaciones académicas



![Captura de detalle de una estructuras de investigación - tab publicaciones académicas](./images/screenshots/detalle-estructuras-publicaciones-academicas.png)



### Sección de proyectos

![Captura de detalle de una estructuras de investigación - tab proyectos](./images/screenshots/detalle-estructuras-proyecto.png)



### Sección de patentes

![Captura de detalle de una estructuras de investigación - tab patentes](./images/screenshots/detalle-estructuras-patentes.png)





En esta pantalla se responderá a las siguientes preguntas de competencia:

| Pregunta de competencia                                      |
| ------------------------------------------------------------ |
| CQ02. Como usuario requiero obtener un listado de los investigadores de un centro/estructura de investigación de un área/disciplina específica. Este listado podrá filtrarse según el tipo de investigador ya sea docente, personal investigador en formación, etc. |
| CQ03. Como usuario requiero obtener el Top 10 (o el número que se considere relevante pues será parametrizable) de los investigadores de un centro/estructura de investigación ordenados por el número de citas, número de publicaciones, h-index, etc. en un área/disciplina específica. |
| CQ06. Como usuario requiero obtener un listado de la producción científica en un determinado rango de fechas de un centro/estructura de investigación en un área/disciplina. Para cada resultado se incluirán algunos metadatos importantes de la producción como, por ejemplo, DOI, año de publicación, etc. |
| CQ09. Como usuario requiero obtener un listado de patentes, diseños industriales, etc. de un centro/estructura de investigación en un área/disciplina. |
| CQ10. Como investigador y personal no investigador de la universidad requiero obtener un listado de los proyectos adjudicados/desarrollados, de un centro/estructura de investigación, de un área/disciplina. |
| CQ12. Como usuario necesito conocer el porcentaje de participación de un centro/estructura de investigación en proyectos nacionales o europeos. |
| CQ17. Como usuario necesito obtener el listado de indicadores con su respectivo valor y unidad de medida (porcentaje, número, etc.) calculados en un periodo de tiempo, ya sea para toda la universidad o para cada centro/estructura de investigación de cada universidad. |
|                                                              |





## 3.2. Acciones de investigación



Se divide en dos secciones, una para patentes y otra para proyectos.



### Acciones de investigación proyectos



La tabla podrá ser filtrada por año y por nombre.



![Captura de acciones de investigación - tab documentos](./images/screenshots/acciones-investigacion-proyectos.png)



### Acciones de investigación - patentes

En esta sección de acciones de investigación se podrán ver las patentes filtradas por nombre y por ámbito.

![Captura de acciones de investigación - tab proyectos](./images/screenshots/acciones-investigacion-patentes.png)



En esta página se trata de mostrar la información de las preguntas de competencia relacionadas con proyectos. 

| Pregunta de competencia                                      |
| ------------------------------------------------------------ |
| CQ10. Como investigador y personal no investigador de la universidad requiero obtener un listado de los proyectos adjudicados/desarrollados, de un centro/estructura de investigación, de un área/disciplina, en un determinado año de búsqueda en los que se tenga acceso al detalle de al menos:<br/>○	Nombre del proyecto<br/>○	Palabras claves<br/>○	Tipo de participación: coordinador o participante<br/>○	Tipo de proyecto: competitivo o no competitivo<br/>○	Tipo de financiamiento: público o privado.<br/>○	Tipo de convocatoria: nacional, H2020, etc.<br/>○	Número y listado de personas involucradas en el proyecto<br/>○	Nombre(s) del investigador(s) principal<br/>○	Entregables/memoria del proyecto<br/>○	Producción científica relacionada con el proyecto<br/>○	Entidades colaboradoras/participantes<br/>○	Cuantía<br/>○	etc. |
| CQ46. Estado del arte: ¿puedo ver los resultados de proyectos por temática concreta de proyectos desarrollados en la red, diferenciando a nivel regional, nacional, europeo? |
|                                                              |
|                                                              |



## 3.2.1. Detalle de una acción de investigación

La información se muestra agrupada en tres secciones (tabs) :

- Información general del proyecto

- Participantes

- Entregables

  

### Información general -patentes



![Captura de detalle de acciones de investigación - tab información](./images/screenshots/detalle-acciones-investigacion-patentes.png)



### Información general -proyectos

![Captura de detalle de acciones de investigación - tab información](./images/screenshots/detalle-acciones-investigacion-proyecto.png)



### Información general -participantes en un proyecto



![Captura de detalle de acciones de investigación - tab participantes](./images/screenshots/detalle-acciones-investigacion-participantes-proyecto.png)



### Información general - entregables en un proyecto



![Captura de detalle de acciones de investigación - tab entregables](./images/screenshots/detalle-acciones-investigacion-entregables-proyecto.png)





Se responden a las siguientes preguntas de competencia, a modo consulta:

| Pregunta de competencia                                      |
| ------------------------------------------------------------ |
| CQ13. Como investigador, personal no investigador de la universidad requiero insertar/modificar los datos relacionados con los proyectos de investigación, incluyendo los entregables que se hayan generado en la fase de propuesta. El usuario tendrá acceso a esta información según el nivel de acceso que se le haya proporcionado previamente según su rol, según niveles de confidencialidad de ser el caso. Entre los datos que se proporcionarán por cada proyecto se tendrá al menos:<br/>○	Nombre del proyecto<br/>○	Palabras claves<br/>○	Tipo de participación de la entidad: coordinador o participante<br/>○	Tipo de proyecto: competitivo o no competitivo<br/>○	Tipo de financiamiento: público o privado<br/>○	Tipo de convocatoria: nacional, H2020, etc.<br/>○	Número y listado de personas involucradas en el proyecto<br/>○	Nombre(s) del investigador(s) principal<br/>○	Entregables/memoria del proyecto<br/>○	Producción científica relacionada con el proyecto<br/>○	Entidades colaboradoras/participantes<br/>○	Cuantía<br/> |
| CQ14. Como usuario necesito una visualización [filtering] que me permita explorar la información de cada proyecto según los filtros que haya elegido, por ejemplo, por años, por tipo de convocatoria, por cuantía mayor a determinado valor, según un área/disciplina, según la ubicación geográfica, etc. |
|                                                              |
|                                                              |



## 3.3. Personal investigador



Se muestra el personal investigador filtrado por áreas y tipo, se podrá ordenar, cambiar el número de resultados, etc.

![Captura de personal investigador](./images/screenshots/personal-investigador.png)





Se utilizan las siguientes preguntas de competencia para el diseño de la pantalla:

| Pregunta de competencia                                      |
| ------------------------------------------------------------ |
| CQ02. Como usuario requiero obtener un listado de los investigadores de un centro/estructura de investigación de un área/disciplina específica. Este listado podrá filtrarse según el tipo de investigador ya sea docente, personal investigador en formación, etc. |
| CQ03. Como usuario requiero obtener el Top 10 (o el número que se considere relevante pues será parametrizable) de los investigadores de un centro/estructura de investigación ordenados por el número de citas, número de publicaciones, h-index, etc. en un área/disciplina específica. [As a user I would like to obtain the Top 10 (or any relevant number, as this would be a parameter) research centers/strutures who have quality seals associated, such as the Severo Ochoa seal.] |
| CQ45. Investigadores que dirigen tesis en programas de doctorado diferentes a los de su Universidad, y cuántas de esas tesis dirigidas han obtenido mención cum laude. |
|                                                              |



## 3.3.1. Detalle de personal investigador



### Detalle de personal investigador - acciones de investigación



![Captura de personal investigador](./images/screenshots/detalle-personal-investigador-acciones.png)



### Detalle de personal investigador - eventos

![Captura de personal investigador](./images/screenshots/detalle-personal-investigador-eventos.png)



### Detalle de personal investigador - actividad empresarial



![Captura de personal investigador](./images/screenshots/detalle-personal-investigador-actividad.png)



### Detalle de personal investigador - trayectoria



![Captura de personal investigador](./images/screenshots/detalle-personal-investigador-trayectoria.png)





## 3.4. Áreas



En esta pantalla se muestra información sobre los datos del módulo vertical "áreas de conocimiento".



![Captura áreas](./images/screenshots/areas.png)



## 3.5. Producción científica



Se muestran los documentos y los eventos de investigaciones.



### Producción científica - publicaciones científicas



![Publicaciones científicas](./images/screenshots/produccion-cientifica-publicaciones-cientificas.png)





### Producción científica - publicaciones académicas



![Publicaciones académicas](./images/screenshots/produccion-cientifica-publicaciones-academicas.png)





### Producción científica - otras publicaciones



![Otros publicaciones](./images/screenshots/produccion-cientifica-otros-documentos.png)





### Producción científica - eventos



![Eventos](./images/screenshots/produccion-cientifica-eventos.png)



## 3.5.1. Detalle de producción científica



### Detalle de producción científica - documentos



![Captura de personal investigador](./images/screenshots/detalle-produccion-cientifica-documentos.png)



### Detalle de producción científica - eventos



![Captura de personal investigador](./images/screenshots/detalle-produccion-cientifica-eventos.png)



## 3.6. Estadísticas



![Estadisticas](./images/screenshots/estadisticas.png)
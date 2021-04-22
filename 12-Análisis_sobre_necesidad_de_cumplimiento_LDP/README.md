![](./images/logos_feder.png)

| Entregable     | Documentación de la librería factoría de URIs                |
| -------------- | ------------------------------------------------------------ |
| Fecha          | 25/05/2020                                                   |
| Proyecto       | [ASIO](https://www.um.es/web/hercules/proyectos/asio) (Arquitectura Semántica e Infraestructura Ontológica) en el marco de la iniciativa [Hércules](https://www.um.es/web/hercules/) para la Semántica de Datos de Investigación de Universidades que forma parte de [CRUE-TIC](https://tic.crue.org/hercules/) |
| Módulo         | Arquitectura Semántica                                       |
| Tipo           | Documentación                                                |
| Objetivo       | El presente documento intenta determinar la idoneidad  de la aplicación del conjunto de reglas establecidas por la [LDP](https://www.w3.org/TR/ldp/), sobre las operaciones HTTP, sobre recursos semánticos basados en grafos RDF. En definitiva, el documento trata de analizar, pros y contras de su uso, ya sea de forma global o parcial, desde el punto de vista del proyecto ASIO. |
| Estado         | **100%**                                                    |
| Próximos pasos |                                                              |
| Documentación  | [Requisitos funcionales para API REST LDP en proyecto ASIO de la UM](https://github.com/HerculesCRUE/ib-asio-docs-/blob/master/12-An%C3%A1lisis_sobre_necesidad_de_cumplimiento_LDP/Requisitos%20LDP%20Server/Requisitos%20funcionales%20para%20API%20REST%20LDP%20en%20proyecto%20ASIO%20de%20la%20UM.md)  [Propuesta de diseño API LDP y EndPoint SPARQL](../00-Análisis/Requisitos%20LDP%20Server/Propuesta%20de%20dise%C3%B1o%20API%20LDP%20y%20EndPoint%20SPARQL.md) |

# Análisis sobre la necesidad de cumplimiento LDP

## Contexto y planteamiento del problema

El presente documento intenta determinar la idoneidad  de la aplicación del conjunto de reglas establecidas por la [LDP](https://www.w3.org/TR/ldp/), sobre las operaciones HTTP, sobre recursos semánticos basados en grafos RDF.

En definitiva, el documento trata de analizar, pros y contras de su uso, ya sea de forma global o parcial, desde el punto de vista del proyecto ASIO.

Para ello, este documento se basara en los principios y conclusiones expuestas en los documentos previos [Requisitos funcionales para API REST LDP en proyecto ASIO de la UM](./Requisitos%20LDP%20Server/Requisitos%20funcionales%20para%20API%20REST%20LDP%20en%20proyecto%20ASIO%20de%20la%20UM.md) y [Propuesta de diseño API LDP y EndPoint SPARQL](../00-Análisis/Requisitos%20LDP%20Server/Propuesta%20de%20dise%C3%B1o%20API%20LDP%20y%20EndPoint%20SPARQL.md)

## Drivers de decisión

- Encaje en la arquitectura global.
- Cumplimiento de requisitos expresados en el pliego.
- Proporcionar patrones de uso y comportamiento a los clientes que puedan consumir el API.
- Amplia adopción por parte de la comunidad.

## Que es la LDP

Básicamente la LDP define un conjunto de estándares  impuestos por la [Linked Data Platform](https://www.w3.org/TR/ldp/), sobre la base de los estándares del protocolo [HTTP](https://www.w3.org/Protocols/rfc2616/rfc2616.html), para establecer normativa especifica para las operaciones sobre recursos semánticos (consulta, edición, modificación y borrado), definidos por medio de grafos RDF, de forma que un cliente (máquina o humano) agnóstico del contenido o de la arquitectura de la implementación, pueda interactuar con dichos recursos de de una forma sencilla y predecible.

## Aplicación de la LDP dentro de la arquitectura del proyecto ASIO

Desde el punto de vista de la arquitectura de la solución diseñada es importante para establecer la necesidad de el grado de cumplimiento de la LDP, introducir algunos aspectos de la arquitectura y de la finalidad que persigue en su diseño.

Como característica general de la arquitectura, diseñada para el proyecto ASIO, podemos decir que el diseño de la misma, busca el objetivo de maximizar el desacoplamiento de sus componentes, es decir, poder sustituir, cualquiera de sus componentes, por otro que realice la misma función, minimizando el impacto  en el resto de componentes.

En este punto es conveniente tener una visión global de la arquitectura prevista para el proyecto ASIO, y definir aquellas partes de la misma, que previsiblemente tendrán contacto con aquellos otros que puedan estar diseñados, siguiendo (o no) los principios de la LDP, ya que dichos componentes, sufrirán el mayor grado de acoplamiento y por lo tanto se verán más afectados por esta decisión.

![architecture](./images/architecture.png)



Tal y como se puede apreciar en la imagen, el API LDP es un componente central de la arquitectura, y el único punto de contacto con los datos almacenados en el el Triple Store.

Previsiblemente y siguiendo el diseño de la arquitectura, los componentes de la misma que tienen contacto directo con el API LDP, son el **procesador de eventos** (en la capa de Back-end),  **el servicio de publicación web** (en la capa de Front-end) y como capa de abstracción que permite el contacto agnóstico entre el API LPD y el Triple Store el **Endpoint SPARQL**,por lo tanto dichos componentes serán los que sufran un mayor grado de acoplamiento a el servidor LDP, y por lo tanto serán aquellos que *"sufran"* las restricciones impuestas por la LDP.

Es conveniente profundizar un poco en la función de componentes, dentro de la arquitectura, para mejorar la comprensión del presente documento:

- Por un lado los componentes que actúan como clientes del API LDP son:
  - Procesador de eventos: Recibe a partir de la cola kafka, los datos ingestados, en formato POJO, y a priori, (junto con el Store Adapter) realiza la conversión a RDF, para invocar a el API LDP, para realizar sobre el triple store la operación requerida sobre el dato (inserción, modificación o borrado).
  - Servicio de publicación Web: Básicamente es una aplicación Front-end, que permite a un usuario, interactuar con los datos RDF, almacenados en el triple store, haciendo uso de las operaciones definidas en el API LDP, y permitiendo a su vez la negociación de contenidos.

* Por otro, el componente que permite interactuar con el triple store es:
  * EndPoint SPARQL: Proporciona una capa de abstracción con el triple store que permite por un lado un acceso homogéneo al dato, por medio del protocolo SPARQL 1.1, y por otro, hacer agnóstico a cualquier componente que requiera acceso al dato (en ese caso el API LDP), del triple store usado.



## Requisitos afectados por la decisión presentes en el del pliego

Para determinar cual es la necesidad de seguir el conjunto de reglas impuestas por la LDP, es conveniente tener en cuenta aquellos requisitos expresados en el pliego, que podrían de algún modo verse afectados y posibles respuestas que el API LDP puede (o no ) dar a los mismos.



| Requisito                                                    | Descripción                                                  | Pag.  Pliego | Bloque  Funcional                   | Implicación en el API LDP                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------ | ----------------------------------- | ------------------------------------------------------------ |
| **REQ 5.1.8** Gestión de  dataset                            | Permisos,   carga masiva, borrado, metadatos, etc. De este requisito se infiere la   necesidad proporcionar permisos de acceso a datos, de manera granular, y por   lo el cumplimiento del requisito de Autorización y autentificación | 65           | Seguridad                           | El API debe proporcionar  mecanismos suficientes para establecer ese control de acceso, aunque la LDP, no define ninguna implementación, si **define el protocolo de notificación al usuario de dichas restricciones de seguridad** (Requisito RF_01_01_06 (4.2.1.6 LDP): Advertir de restricciones). La forma en que el API LDP cubra o no el requisito, dependerá de la implementación, pero a priori, tanto el protocolo HTTP, como la extensión LDP, **prevén la respuesta del servidor  ante la interacción con el cliente**. |
| **REQ 7.1** Conexión con el  Triple Store                    | El adjudicatario creará el código necesario  para la conexión del Backend SGI con la Triple Store, siempre teniendo en  cuenta que el Backend SGI tiene que ser lo más  independiente posible de la Triple Store de modo  que si otra Universidad decide usar otra Triple Store, puede hacerlo con la  menor fricción posible. | 67           | Triple Store                        | Este requisito expresa la necesidad de poder intercambiar un triple store por otro de la forma mas trasparente posible. Aunque la LDP, obviamente no realiza mención alguna a ello, el hecho de seguir protocolos estándar (el que propone la LDP lo es), hace que **sea posible sustituir cualquier API LDP por otro**, sin que el cliente a priori tuviese que verse afectado, ya que en principio, ambas cumplirán el estándar propuesto por la LDP, y por lo tanto, la interacción del cliente con el API, no debería de verse afectada. Por otro lado , como se menciona en el apartado anterior, el diseño de la arquitectura, maximiza el grado de desacoplamiento entre los componentes, de forma que solo el EndPoint SPARQL, debería de verse afectado por un cambio de triple store. **El cumplimiento de estándares, facilita el intercambio de componentes**, por lo que en este sentido, también **el cumplimiento de LDP, facilita el cumplimiento del requisito** |
| **REQ 7.2** Benchmark para  evaluar Triple Store candidatas, | El adjudicatario creará un Benchmark para evaluar las Triple Stores candidatas  y así facilitar a los técnicos de la UM la elección  de la Triple Store adecuada. El Benchmark  consistirá en una serie de criterios con un peso específico, y el resultado  será una media ponderada de la puntuación obtenida en cada criterio. El  adjudicatario creará el Benchmark y proveerá un primer resultado proponiendo  un ranking de Triple Stores, pero los criterios, pesos específicos y las puntuaciones  dadas a cada Triple Store podrán ser modificadas por la UM y el Benchmark  ejecutado de nuevo. | 67           | Triple Store                        | En la línea la argumentación del punto anterior, **el uso de LDP, facilita el cambio del Triple Store**, en otro caso, no tendría sentido evaluar distintos Triple Stores, si la elección de uno u otro, estuviese limitada por la solución elegida (por ejemplo Wikibase, en principio, limita al uso de BlazeGraph como Triple Store). |
| **REQ 7.3** Memoria  Científico-Técnica sobre la elección del Triple Store | La empresa deberá especificar los siguientes  extremos en la Memoria Científico-Técnica: Licencia, Acceso programático  mediante Eclipse RDF4J, API REST, Dependencias, Rendimiento, Clustering y  alta disponibilidad, Transacciones, Documentación adecuada, Facilidad de uso  y administración, Existencia de una comunidad amplia de usuarios,  Cumplimiento de estándares W3C (LDP, SPARQL 1.1), razonamiento automático,  Soporte de SHACL u otras funcionalidades de tipo Closed World Assumption para  analizar RDF, Búsquedas por texto con servicios como Apache SOLR y Apache  Lucene, Funciones de reconciliación de entidades como NER, Funciones para  datos de tipo Property Graph, Funciones de ingesta de datos no-RDF | 67           | Triple Store                        | Misma línea argumental que en el punto anterior.             |
| **REQ 7.8** Implementación de  sistema para consultas federadas | Una vez consensuada la estrategia con UM.                    | 67           | Triple Store                        | Probablemente, sea necesario realizar un Merge de las respuestas individuales de cada una de los Backend. Para ello, es importante, que tanto los mecanismos para realizar las peticiones, como el formato de las respuestas,  **sigan un protocolo estándar y la LDP lo proporciona** |
| **REQ 8.2.1** Cumplimiento de  buenas prácticas Linked Data: | Buenas prácticas Linked Data (Heath 2011 ,  Dodds 2012). Por ejemplo, que todas las entidades tengan predicados rdf:type  y rdfs:label, predicados rdfs:isDefinedBy, que no haya nodos anónimos, etc.. | 70           | API Linked Data                     | Obviamente este requisito indica claramente la **necesidad de cumplimiento de buenas practicas LDP** |
| **REQ 9.2.1**  Cliente de la API Rest                        | La interface Web Es un cliente de la API Rest                | 72,73        | API Linked Data                     | Como se comento en la sección de arquitectura, la interface Web, actúa como un cliente REST, seguir el **protocolo LPD**, hace que pueda sustituirse un API por otro sin un gran efecto. Por otro lado la LDP da directrices útiles para la interface Web, en algunos aspectos tales como la **negociación de contenidos, documentos No-RDF, etc...** |
| **REQ 10.1** Servidor Linked  Data                           | Servidor Linked Data                                         | 74           | API Linked Data                     | Este requisito es el mas claro, ya que **expresa claramente la necesidad de implementar un servidor linked data** y la LDP prevé específicamente esto. |
| **REQ 10.1.1** Resolución  directa de URIs                   | Obtener datos o metadatos almacenados en el  Triple Store. De sólo lectura. | 74           | API Linked Data                     | Aplicación de Método **GET definido por la LDP**             |
| **REQ 10.1.10** Redirección de  peticiones HTTP del exterior | A los servicios correspondientes.                            | 74           | API Linked Data                     | **Redirecciones previstas por la LPD**, mediante la cabecera link |
| **REQ 10.1.2** Respuesta a  peticiones HTTP GET:             | Devolviendo los datos del Triple Store.                      | 74           | API Linked Data                     | Aplicación de Método **GET definido por la LDP**             |
| **REQ 10.1.3** Negociación de  contenido                     | Negociación de contenido con gran  granularidad: Por ejemplo será capaz de gestionar una petición con la  cabecera “Accept: text/rdf+n3;q=0.5”, es decir con un valor “q” para un  formato concreto. | 74-76        | API Linked Data                     | La negociación de contenidos esta **prevista por la LDP**, mediante el uso de la cabecera Accept |
| **REQ 10.1.6** JSON-LD para  datos anotados mediante Schema  | Al renderizar los datos RDF en  HTML, si éstos incluyen datos anotados mediante Schema, se incluirán en la  página Web resultante mediante el uso de JSON-LD, facilitando así la  indexación estructurada por los buscadores que soportan Schema | 74-76        | API Linked Data                     | **Previsto por la LDP**, que impone el soporte a JSON-LD     |
| **REQ 10.1.8** HTTP Range 14                                 | Análisis sobre qué estrategia seguir de las  descritas en el Documento W3C Cool URIs for the Semantic Web, Hash URIs o  Slash URIs, y para qué recursos. Implementación de la misma. | 74           | API Linked Data                     | Las Hash URIs o Slash URIs están **soportadas por la LDP**   |
| **REQ 10.1.9** Análisis de  cumplimiento LDP                 | El adjudicatario creará un análisis sobre  hasta qué punto el Servidor Linked Data tiene que cumplir la recomendación  Linked Data Platform del W3C y para qué recursos, teniendo en cuenta la  adopción de dicho estándar por parte de la comunidad, utilidad, beneficios a  largo plazo, y dificultad de implementación, entre otros. La decisión que  tomen los técnicos de la UM basándose en ese análisis se verá reflejada en el  diseño e implementación del Servidor Linked Data. Este análisis también se  tendrá en cuenta en el Benchmark de Triple Stores, determinando el peso del  criterio Linked Data Platform del mismo. | 74-76        | API Linked Data                     | Es la función del presente documento                         |
| **REQ 10.2.2** Interfaz  gráfico                             | Basado en Wikidata para obtener datos o  metadatos almacenados en el Triple Store. De sólo lectura | 75           | EndPoint SPARQL / Interface Gráfica | El interface gráfico usara el **API Rest**, como se ha comentado anteriormente, si este sigue el protocolo LDP, podrá intercambiarse un API pro otro sin un gran cambio en el cliente. |
| **REQ 10.4.3** Pruebas  cabeceras HTTP                       | Negociación de contenidos, LDP                               | 74-76        | API Linked Data                     | La negociación de contenidos esta **prevista por la LDP**, mediante el uso de la cabecera Accept |

## Conclusiones 

### Basadas en la arquitectura

Como se ha comentado en la sección de arquitectura, la filosofía de diseño de la plataforma, pretende maximizar el desacoplamiento entre componentes y minimizar las dependencias entre ellos.

Seguir el conjunto de reglas propuestas por la LPD, permite que el acoplamiento de los componentes que interactúen con el API (procesador de eventos y el servicio de publicación web) sea únicamente con el **protocolo** que propone la LDP, nunca hacia el propio servidor que lo implementa, de forma que sustituir el servidor propiamente dicho, no debería de suponer un problema, siempre que este implemente de manera similar el protocolo. 

![protocolos](./images/protocolos.png)

Por otra parte el cliente que use el servidor LDP, no requerirá de un conocimiento expreso de su implementación (Requisito RF_01_03_02  [(4.2.4.2 LDP)](https://www.w3.org/TR/ldp/#ldpr-resource): Permitir realizar una actualización, sin un conocimiento profundo de las restricciones del Servidor ).

### Basadas en los requisitos del proyecto

Tal como se enuncia en las sección [Requisitos afectados por la decisión presentes en el del pliego](# Requisitos afectados por la decisión presentes en el del pliego), todas las requisitos enumerados en dicha sección, son implementados, o se favorece su cumplimiento (mirar documento [Requisitos funcionales para API REST LDP en proyecto ASIO de la UM](https://github.com/HerculesCRUE/ib-asio-docs-/blob/master/12-An%C3%A1lisis_sobre_necesidad_de_cumplimiento_LDP/Requisitos%20LDP%20Server/Requisitos%20funcionales%20para%20API%20REST%20LDP%20en%20proyecto%20ASIO%20de%20la%20UM.md), mediante el cumplimiento del estándar LPD, por lo que este análisis , también desde ese punto de vista, se recomienda sus uso.

### Basadas en la dificultad de implementación

Dado que hay multitud de [implementaciones de servidores LDP](https://www.w3.org/wiki/LDP_Implementations) , e incluso la W3C dispone de documentación pública de el [nivel conformidad](https://dvcs.w3.org/hg/ldpwg/raw-file/default/tests/reports/ldp.html) con la LDP de algunas de estas implementaciones,  disponibles, esto no debería de ser un impedimento para su cumplimento

1. Activas
   - [Trellis LDP Server](https://www.w3.org/wiki/LDP_Implementations#TrellisLDP_.28Server.29)
   - [LDP.js (Server)](https://www.w3.org/wiki/LDP_Implementations#LDP.js_.28Server.29)
   - [LDP4j (Client and Server)]([LDP4j (Client and Server)](https://www.w3.org/wiki/LDP_Implementations#LDP4j_.28Client_and_Server.29))
   - [Apache Marmotta (Client and Server)](https://www.w3.org/wiki/LDP_Implementations#Apache_Marmotta_.28Client_and_Server.29)
   - [Callimachus (Client and Server)](https://www.w3.org/wiki/LDP_Implementations#Callimachus_.28Client_and_Server.29)
   - [Carbon LDP (Client and Server)](https://www.w3.org/wiki/LDP_Implementations#Carbon_LDP_.28Client_and_Server.29)
   - [Eclipse Lyo (Server, Software Lifecycle)](https://www.w3.org/wiki/LDP_Implementations#Eclipse_Lyo_.28Server.2C_Software_Lifecycle.29)
   - [RWW.IO](https://www.w3.org/wiki/LDP_Implementations#RWW.IO)
   - [OpenLink Data Spaces (Hosted Service; LDP Client & Server)](https://www.w3.org/wiki/LDP_Implementations#OpenLink_Data_Spaces_.28Hosted_Service.3B_LDP_Client_.26_Server.29)
   - [OpenLink Virtuoso (Data Server; LDP Client & Server)](https://www.w3.org/wiki/LDP_Implementations#OpenLink_Virtuoso_.28Data_Server.3B_LDP_Client_.26_Server.29)
   - [rdflib.js (Client Library)](https://www.w3.org/wiki/LDP_Implementations#rdflib.js_.28Client_Library.29)
   - [rdf.sh (Client)](https://www.w3.org/wiki/LDP_Implementations#rdf.sh_.28Client.29)
   - [RWW Play Server](https://www.w3.org/wiki/LDP_Implementations#RWW_Play_Server)
   - [Tabulator (Client)](https://www.w3.org/wiki/LDP_Implementations#Tabulator_.28Client.29)
   - [TopBraid Live (Client and Server)](https://www.w3.org/wiki/LDP_Implementations#TopBraid_Live_.28Client_and_Server.29)
   - [Fedora Commons Repository (Server)](https://www.w3.org/wiki/LDP_Implementations#Fedora_Commons_Repository_.28Server.29)
   - [Glutton (Server)](https://www.w3.org/wiki/LDP_Implementations#Glutton_.28Server.29)
   - [gold (Server)](https://www.w3.org/wiki/LDP_Implementations#gold_.28Server.29)
   - [ldnode (Server)](https://www.w3.org/wiki/LDP_Implementations#ldnode_.28Server.29)
2. Inactivas
   - [Bygle (Client and Server)](https://www.w3.org/wiki/LDP_Implementations#Bygle_.28Client_and_Server.29)
   - [Genboree (Client and Server)](https://www.w3.org/wiki/LDP_Implementations#Genboree_.28Client_and_Server.29)
   - [ldpy (Client)](https://www.w3.org/wiki/LDP_Implementations#ldpy_.28Client.29)
   - [node_ldp (Server)](https://www.w3.org/wiki/LDP_Implementations#node_ldp_.28Server.29)

### Basadas en la adopción como estándar de facto al servir recursos semánticos

El conjunto de reglamentación proporcionada por la LDP, proporciona un marco de trabajo lo suficientemente detallado para que  su cumplimiento permita que el patrón de uso que se deriva del mismo para un servidor que lo implemente, sea predecible y sencillo de aplicar para un hipotético cliente que consuma dichos recursos. Por otro lado, al definirse como una extensión del protocolo HTTP, al que complementa para dar cabida la reglamentación necesaria para mejorar la interacción con recursos semánticos, y estando ambos definidos formalmente por la W3C, pensamos que esto convierte a la LDP, en un estándar de facto para la comunidad. Por otro lado, pensamos que es un protocolo lo suficientemente abierto (su reglamentación casi exclusivamente es aplica a recursos semánticos), permite una sencilla integración con otros protocolos, minimizando las colisiones en sus normativas.

Por otro lado creemos que cantidad de implementaciones de servidores que implementan en algún grado los estándares propuestos por la LDP (mirar [punto anterior](#Basadas en la dificultad de implementación)), demuestran dichos estándares se han convertido en un estándar de facto para recursos Linked Data. 

### Posibles no cumplimientos del  la LDP en proyecto ASIO

#### Relativos a conflictos con otros protocolos

Existen otros protocolos que pueden resultar interesantes para el proyecto ASIO, como es el caso de el estándar Memento descrito en el documento [Memento Guía y Normativa](https://github.com/HerculesCRUE/ib-asio-docs-/blob/master/12-An%C3%A1lisis_sobre_necesidad_de_cumplimiento_LDP/Requisitos%20LDP%20Server/Memento%20Gu%C3%ADa%20y%20Normativa.md). Dicho protocolo establece los requerimientos para implementar un servidor que permita acceder a un mismo recurso en distintos estados del tiempo, con lo que realizar una consulta en un determinado espacio temporal, seria posible.

El protocolo Memento, entra en conflicto, con 2 requerimientos de tipo **SHOULD** expresado por la LDP

**Requisito:**  

> ###### Requisito RF_04_03_02  [(5.2.4.2 LDP)](https://www.w3.org/TR/ldp/#ldpc-container): No se deben reusar URIs
>
> Los servidores que admiten PUT para creación de recursos **NO DEBERÍAN** reusar URIs.

**Requisito:**  

> ###### Requisito RF_01_03_05 [(4.2.4.5 LDP)](https://www.w3.org/TR/ldp/#ldpr-resource): Fallos por restricciones en propiedades
>
> Los clientes **PUEDEN** usar la cabecera **If-Match** y la cabecera **ETag** para garantizar que no se actualiza un recurso, que pueda haber cambiado desde que el cliente obtuvo su representación. El servidor **PUEDE** requerir el uso de ambas cabeceras. El servidor LDP **DEBE**  responder con el código 412 (Condition Failed), si falla por causa del ETag, y no existen otros errores. Los servidores que requieran el ETag, y este no este presente, **DEBEN** responder con el código 428 (Precondition Required) si esta es la única razón.

ya que en este caso, sobre un mismo recurso (en distintos dimensiones temporales) y una misma URL, podrán existir mas de un recurso, y por lo tanto, debe de permitirse infligir la norma  [(5.2.4.2 LDP)](https://www.w3.org/TR/ldp/#ldpc-container): No se deben reusar URIs, y la norma [(4.2.4.5 LDP)](https://www.w3.org/TR/ldp/#ldpr-resource): Fallos por restricciones en propiedades, relativa a la cabecera If-Match.

#### Relativos a los recursos

Por otro lado, tal como se detalla  en la sección [Recursos](https://www.w3.org/TR/ldp/#ldpr-resource), la LDP prevé soporte para recursos semánticos (LDP-RS) y no semánticos (LDP-NR) como por ejemplo imágenes, binarios, HTML.

Prevemos un soporte completo para recursos LDP-RS, tal como exige la LDP, pero en el caso de los recursos LDP-NR, dado que la LDP no exige que estos deban de ser servidos por la implementación del servidor LDP, valoramos la posibilidad de que estos puedan ser servidos por otras plataformas, que para este tipo de contenidos, podrían ser mas eficientes.

#### Relativos a contenedores

Creemos que del esquema de URIs propuesto en el documento de [Esquema de URIs Hércules](https://github.com/HerculesCRUE/ib-asio-docs-/blob/master/08-Esquema_de_URIs_H%C3%A9rcules/ASIO_Izertis_ArquitecturaDeURIs.md), puede inferirse una jerarquía de contenedores, que encajan de forma bastante precisa con los contenedores previstos por la LDP. 

Organizar adecuadamente la información dentro de contenedores, que además según lo previsto por la LDP, pueden estar anidados (un contenedor puede contener a otro contenedor),  hará un que proceso de recuperar la información, sea una tarea mucho optima, precisa y predecible por parte de un hipotético cliente. Por ejemplo, si suponemos que el componente **concepto** descrito en el esquema de URIs, puede representar una clase (por ejemplo la clase investigador), la acción de un cliente, para obtener todos los investigadores (instancias), se limitaría ha realizar una operación GET sobre el propio contenedor.

En cuanto a la jerarquía entre los conceptos (por ej. un investigador puede pertenecer a un grupo), se recomienda no modelarla en forma de contenedores, ya que por un lado esa jerarquía podría variar con el tiempo y además podría no ser única (es decir una clase podría tener mas de una clase padre) y por otro lado, implicaría un conocimiento exhaustivo de las dependencias de una clase con otra, lo que aumentaría, enormemente la complejidad. Por ese motivo, se recomienda que todos los conceptos, independientemente de su jerarquía entre ellos,  se modelen como contendores independientes, en el mismo nivel jerárquico.

En cuanto a los tipos de contenedores, la LDP, prevé contenedores Básicos (que contiene un simple link a sus recursos contenidos), contenedores Directos (que añade el concepto de pertenencia) o contenedores Indirectos (similares a los directos, pero que permiten que sus URIs estén basadas en el contenido de los documentos que contiene).

Por el momento para el caso de los conceptos, se usara el tipo de contenedor Básico, ya que los contenedores Directos o indirectos, están más orientados a establecer jerarquía entre contenedores, y esta por los motivos que se enumeraron anteriormente no se aplicaran para conceptos.

Otros componentes de descritos en el esquema de URIs, como el tipo, podría modelarse como contenedores directos, ya que dicha jerarquía,  tal como establece el esquema de URIs, es bastante mas estática. 

#### Relativos a operaciones

La LDP regula las operaciones de implementación obligatoria (operaciones de lectura GET,POST, PUT) y da recomendaciones sobre el resto (operaciones de escritura POST, PUT, DELETE y PATCH).

El servidor LDP implementado, implementara sin restricciones todas las operaciones de lectura descritas, pero en cuanto a las operaciones relativas a escritura, en ocasiones estas acciones pueden tener implicaciones en otros recursos relacionados, por lo que solo se permitirá su ejecución en operaciones internas de la plataforma ASIO (procesador de eventos), que deberá de soportar las implicaciones de dichos cambios (borrados o modificaciones recursivas).

#### Conclusión

En conclusión, deben de cumplirse todas las normativas, salvo aquellas que su incumplimiento puedan resultar de interés, por incompatibilidad con cualquier otro protocolo que deseemos aplicar, en este caso Memento o alguna otra restricción que la operativa de el proyecto pueda imponer, como por ejemplo las restricciones relativas a las operaciones permitidas.

### Conclusión final

En definitiva, no solo consideramos deseable el cumplimiento del estándar LDP, sino que lo creemos que es un **pilar básico**, para garantizar por un lado, que minimicemos el acoplamiento de los componentes de la arquitectura con el API Rest, que proporcionemos patrones de uso y comportamiento a los clientes que puedan consumir el API, de forma que no sea preciso un conocimiento expreso de la implementación y que de la forma mas fiel posible, se garantice el cumplimiento de los requisitos expresados en el pliego.

Por todo ello, (excluyendo los incumplimientos expresados en el apartado [Posibles no cumplimientos del  la LDP en proyecto ASIO](#Posibles no cumplimientos del  la LDP en proyecto ASIO)), creemos mas que deseable cumplir en la medida de lo posible con el conjunto de reglas expresadas por la LDP, en la implementación del API Rest.


![](assets/logos_feder.jpg)

| Entregable     | Control de versiones sobre ontologías OWL                    |
| -------------- | ------------------------------------------------------------ |
| Fecha          | 17/12/2020 |
| Proyecto       | [ASIO](https://www.um.es/web/hercules/proyectos/asio) (Arquitectura Semántica e Infraestructura Ontológica) en el marco de la iniciativa [Hércules](https://www.um.es/web/hercules/) para la Semántica de Datos de Investigación de Universidades que forma parte de [CRUE-TIC](https://tic.crue.org/hercules/) |
| Módulo         | Infraestructura Ontológica |
| Tipo           | Documentación / Métodos integración continua |
| Objetivo       | Establecer los métodos de integración continua de ontologías y su integración con el sistema de control de versiones GitHub |
| Estado         | **90%** En este documento se establecen los métodos de integración continua de ontologías. Además se explica como se integran estos métodos con el sistema de control de versiones de GitHub. Sin embago, estos métodos no han sido puestos en producción en el entorno de a Universidad de Murcia |
|Repositorio de Software Asociado| **NINGUNO.** Se trata de un entregable de tipo documentación / métodos. |

# Metodología para a integración continua de ontologías
Uno de los retos de investigación del proyecto Hércules, es solucionar el problema de control de versiones de ontologías. Esto se produce porque la serialización de una ontología tiene varios resultados. Es decir, una ontología podría serializarse en dos archivos OWL (A y B). Y, pese a ser la misma ontología A y B serían distintos.

Para dar solución a este problema, se ha optado por abordarlo con una serie de métodos. Todos ellos explicados en [1]. Uno de esos métodos, se basa someter a la ontología a un proceso de integración continua [2]. Si estuviésemos hablando de software, emplearíamos [Jenkin](https://www.jenkins.io/)s o [Travis](https://travis-ci.org/). Sin embargo, estas herramientas se basan en ejecutar prubas definidas con código. Es decir, que las pruebas están formadas por dos partes imprescindibles. El **sistema de ejecución de pruebas** y **las pruebas** en sí.

De esta forma este documento se centra en normar el sistema de ejecución de pruebas a emplear y en establecer una metodoloǵia para la definición de pruebas.


## Sistema de ejecución de pruebas
Como se comentó en el apartado anterior, cualquier sistema de pruebas está formado por dos partes. La definición de las pruebas y el sistema que es capaz de ejecutarlas. Y es que estas dos partes están ligadas. Pues el sistema que ejecuta las pruebas necesita conocerlas. Para ello se comparte alguna clase de interfaz que ambas partes conocen. En el caso de Java, si se emplea el framework JUnit pues se empleará el mismo framework para definir lo que es una clase de pruebas o lo que es una prueba en sí. Y, si se emplea una solución adhoc pues crearemos nuestro ejecutor de casos de prueba y luego la definición de los mismos.

Para las ontologías pasa un poco lo mismo. Podemos acoplar nuestro sistema de integración de la ontología al entorno de desarrolo, por ejemplo desarrollando nuestro propio ejecutor de casos de prueba, o, por la contra, eplear un sistema de ejecución de prueba genérico, como puede ser [OntoloCI](https://www.github.com/weso/ontolo-ci).

Para un proyecto vivo, como es el proyecto Hércules, donde el entorno de desarollo de la ontología es una comunidad abierta y open source la recomendación es en cualquier caso emplear una herramienta externa que no acople el entorno de desarrollo. De esta forma el entorno de desarroll se verá compuesto por la ontología, la definición de las pruebas y las psibles configuraciones que fueran necesarias.

Para elegir qué sistema de integración continua externo empleamos no hay un abanico muy grande donde escoger. De hecho, a fecha de realización de esta documentación sólo se encontró el sistema OntoloCI como un sistema para realizar integración continua sobre ontologías.

### Ontolo-CI
Ontolo-CI es un sistema basado en contenedores de docker que se integra con GitHub para proveer de un sistema de integración continua para ontologías. Para ello, usa [Shape Expressions](http://shex.io) como lenguaje de definición de casos de prueba.

Actualemnte, Ontolo-CI está siendo desarrollado y mantenido por el grupo de investigación WESO, de la Universidad de Oviedo. Ontolo-CI se ofrece como solución Open Source y bajo licencia MIT. Más detalles sobre esta licencia pueden explorarse en [3]. 

Este sistea es una abstracción de un ejecutor de tests. Pero con inegración con GitHub. Esto último permite automatizar tareas como revisar pull requests de forma automática o dar feedback al usuario sobre los errores cometidos en el código. Sin embargo, es cierto que Ontlo-CI impone que el lenguaje de definición de los tests sea Shape Expressions. Aunque esto no acarrera ningún comprmiso para el proyecto Hércules. Ya que, para la generación del modelo de dominio se emplean Shape Expressions. Pudiendo servir estas Shape Expressions para dos propósitos: testear la ontología y generar el modelo de dominio.

### Integración con entorno de desarrollo
En el caso de la herraienta seleccionada, Ontolo-CI, la integración es muy sencilla. Se presenta como un contenedor de Docker [4]. Una vez desplegado, provee de todos los servicios necesarios. Interfaz Web para ver el estado de las ejecuciones, ejecutor de tests y un módulo de comunicación con GitHub.

El siguiente diagrama muestra cómo Ontolo-CI puede integrarse con uno o varios repositorios de ontologías alojados en GitHub.

![](assets/ontolo-ci-main-schema.png)

La herramienta escogida, además realizar la integración continua, es capaz de comunicarse con GitHub para informar sobre el resultado de las pruebas. De esta forma, si una pull request [5] a la rama principal no cumple con las pruebas definidas, el sistema de integración continua le comunicará a GitHub que no permita que estos cambios llegen a la rama principal. De esta forma se asegura la estabilidad de la rama principal. Y, por tanto, de la ontología. 

## Definición de las pruebas
Para describir las pruebas Ontolo-CI emplea el mismo sistema que se usa en el W3C. Ficheros "manifest" de descripción. Cada repositorio de ontologías tiene un único manifest. Y en él se especifican las pruebas que se tienen que ejecutar. Por ejemplo, el siguiente fichero manifest define _n_ casos de prueba.

```json
 ...,
  {
     "test_name": "test that a project instance does not conform to a random shape",
     "ontology": "../../src/asio-core.ttl",
     "data": "../asio-individuals.ttl",
     "schema": "../random_shape.s",
     "in_shape_map": "../random_shape_in.m",
     "out_shape_map": "../random_shape_out.m"
   },
   ...
]
```

En el manifest anterior tenemmos cinco entradas:

 - **Ontology:** El fichero de ontología que queremos probar.
 - **Data:** Las instancias de datos que vamos a usar para probar la ontología.
 - **Schema:** El esquema que debería de seguir la ontología.
 - **Shape Map de entrada:** La condición que se tiene que cumplir.
 - **Shape Map de salida:** El resultado esperado de la validación. Puede esperarse que el test pase o que no pase si es un test negativo.

De esta forma un esquema posible podría ser:
```turtle
# Prefixes definitions.
prefix asio: <http://purl.org/hercules/asio/core#>
prefix xsd: <http://www.w3.org/2001/XMLSchema#>
prefix foaf: <http://xmlns.com/foaf/0.1/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>

asio:RandomShape {
  asio:name   xsd:date      ;
  asio:random foaf:Agent  + ;
}
```

Un shape map de entrada podría ser:
```turtle
asioIndividuals:CHANCE@asio:RandomShape
```

Y, un shape map de salida podría ser:
```turtle
asioIndividuals:CHANCE@!asio:RandomShape
```

Como vemos en el shape map de salida le estamos diciendo que esperamos que esa instancia no valide contra esa shape. Un test negativo.

## Referencias
 - [1] Sistema de control de versiones para OWL. [Documento](../ASIO_Izertis_ControlDeVersionesOWL.md).
 - [2] FOWLER, Martin; FOEMMEL, Matthew. Continuous integration. 2006. [PDF](https://moodle2019-20.ua.es/moodle/pluginfile.php/2228/mod_resource/content/2/martin-fowler-continuous-integration.pdf) 
 - [3] Licencia MIT Wikipedia. [Enlace](https://es.wikipedia.org/wiki/Licencia_MIT).
 - [4] Página web oficial de Docker. [Web](https://www.docker.com/)  
 - [5] Manual sobre Pull Requests de GitHub. [Web](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/proposing-changes-to-your-work-with-pull-requests)  
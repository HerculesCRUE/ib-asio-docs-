![](./images/logos_feder.png)

| Fecha        | 29/04/2021               |
| ------------ | :----------------------- |
| Revisado por | Paloma Terán Pérez       |
| Módulo       | Seguridad de información |
| Tipo         | Documento                |
| Objetivo     | Seguridad de información |



# Seguridad de información

Se precisa disponer de un sistema de seguridad de la información mostrada por la solución ASIO. 

- Limitar el acceso a ciertos datos en función del perfil del usuario
- Denegar el acceso a partes de la aplicación en función del perfil

## Requisitos afectados

| REQ. | Nombre |
| ---- | ------ |
| REQ 5.1.9 | Gestión de usuarios, permisos y acceso de datos |
| REQ 5.2 | Interfaz público |
| REQ 5.2.1 | SPARQL endpoint |
| REQ 5.2.2 | Servidor Linked Data |
| REQ 9.2 | 18.2 Interfaz |
| REQ 9.2.5 | Usuarios, acceso y seguridad |
| REQ 10.1 | 19.1 Servidor Linked Data |
| REQ 10.1.7 | Consulta SPARQL configurable desde la interfaz |
| REQ. 10.2 | 19.2 SPARQL endpoint |
| REQ 10.2.1 | Ejecución de consultas SPARQL |

## Posibles escenarios

De cara a establecer una solución, es necesario analizar los posibles escenarios, ya que cada uno tendrá que tener una solución adaptada a sus características.

### Visualización de datos a través de la aplicación Web

En la aplicación web se irán mostrando datos de diferentes entidades, a través de la navegación por las pantallas. Para la obtención de estos datos, se utiliza una capa de servicios con diferentes endpoints por cada uno de los tipos de entidad, lo que finalmente se acaba traduciendo en la ejecución de diferentes consultas SPARQL para obtener la información necesaria. 

#### Solución planteada

Dado que las consultas SPARQL que se ejecutan están muy acotadas y controladas, la autorización se podría implementar mediante un proxy de seguridad, que mediante la definición de una serie de reglas, determine si el usuario dispone de de acceso a un determinado dato o no, utilizando para ello por ejemplo una técnica de "data masking", la cual hará que los datos que no se quieran visualizar se oculten mediante la sustitución de los mismos por una máscara.

Por ejemplo, suponiendo que se dispone del siguiente dato obtenido a través de SPARQL:

```json
{
  "end": {
    "type": "literal",
    "xml:lang": "es",
    "value": ""
  },
  "fund": {
    "type": "literal",
    "xml:lang": "es",
    "value": "5500"
  },
  "id": {
    "type": "literal",
    "xml:lang": "es",
    "value": "172"
  },
  "name": {
    "type": "literal",
    "xml:lang": "es",
    "value": "HISTORIA ECONÓMICA"
  },
  "start": {
    "type": "literal",
    "xml:lang": "es",
    "value": "2000-01-01"
  },
  "tipo": {
    "type": "literal",
    "xml:lang": "es",
    "value": "GRUPO"
  }
}
```

Supongamos que se quiere limitar el acceso al dato `fund`, para ello se aplicaría la máscara, por ejemplo `<hidden>`, quedando de la siguiente forma:

```json
{
  "end": {
    "type": "literal",
    "xml:lang": "es",
    "value": ""
  },
  "fund": {
    "type": "literal",
    "xml:lang": "es",
    "value": "<hidden>"
  },
  "id": {
    "type": "literal",
    "xml:lang": "es",
    "value": "172"
  },
  "name": {
    "type": "literal",
    "xml:lang": "es",
    "value": "HISTORIA ECONÓMICA"
  },
  "start": {
    "type": "literal",
    "xml:lang": "es",
    "value": "2000-01-01"
  },
  "tipo": {
    "type": "literal",
    "xml:lang": "es",
    "value": "GRUPO"
  }
}
```

Yendo un paso más allá, esto permitiría a la interfaz interpretar la máscara `<hidden>` y no mostrar ese dato o incluso mostrar algo que refleje que ese dato está oculto.

### Editor de consultas SPARQL / Endpoint SPARQL

En la aplicación existe un editor de consultas SPARQL para humanos, además de un endpoint SPARQL para para máquinas. Este tipo de endpoints permite al usuario (humano o máquina) tanto la [consulta](https://www.w3.org/TR/2013/REC-sparql11-query-20130321/) como la [actualización](https://www.w3.org/TR/sparql11-update/) de la información.

#### Actualización de información

En el caso de la actualización de la información, SPARQL utiliza la especificación [SPARQL 1.1 Update](https://www.w3.org/TR/sparql11-update/). Consiste en una sintaxis derivada de SPARQL Query Language, permitiendo realizar operaciones de actualización en una colección de grafos. Se incluyen operaciones de actualización, creación y borrado de grafos RDF.

Dado el carácter de estas acciones, es necesario limitar quién puede realizar estas modificaciones de datos. También hay que tener en cuenta que el hecho de permitir realizar modificaciones por fuera del flujo normal de inserción / actualización de datos puede tener un impacto en el correcto funcionamiento de ciertas partes del sistema que no sean conscientes de esta modificaciones, como por ejemplo etl, uris-factory o discovery.

##### Solución planteada

Dado el motivo expresado en el párrafo anterior en el que puede tener un impacto en el correcto funcionamiento de determinados módulos el hecho de que se permita modificar información mediante un endpoint, se plantea **no permitir actualización de datos mediante SPARQL Update**.

#### Consulta de datos

La consulta de datos sigue la especificación [SPARQL 1.1 Query Language](https://www.w3.org/TR/2013/REC-sparql11-query-20130321/). Dadas las características de este tipo de herramientas, el usuario es capaz de generar una consulta en lenguaje SPARQL para consultar los datos de la forma que necesite, pudiendo incluso realizar combinaciones de consultas, subqueries, etc. Por ejemplo la siguiente consulta es un buen exponente de esto, ya que hace uso de subconsultas, uniones, agrupaciones, alias, agregaciones, etc.

```s
#Number of handed out academy awards per award type
SELECT ?awardCount ?award ?awardLabel WHERE {
  {
    SELECT (COUNT(?award) AS ?awardCount) ?award
    WHERE
    {
      {
        SELECT (SAMPLE(?human) AS ?human) ?award ?awardWork (SAMPLE(?director) AS ?director) (SAMPLE(?awardEdition) AS ?awardEdition) (SAMPLE(?time) AS ?time) WHERE {
          ?award wdt:P31 wd:Q19020 .      # All items that are instance of(P31) of Academy awards (Q19020)
          {
            ?human p:P166 ?awardStat .              # Humans with an awarded(P166) statement
            ?awardStat ps:P166 ?award .        # ... that has any of the values of ?award
            ?awardStat pq:P805 ?awardEdition . # Get the award edition (which is "subject of" XXth Academy Awards)
            ?awardStat pq:P1686 ?awardWork . # The work they have been awarded for
            ?human wdt:P31 wd:Q5 .        # Humans
          } UNION {
            ?awardWork wdt:P31 wd:Q11424 . # Films
            ?awardWork p:P166 ?awardStat . # ... with an awarded(P166) statement
            ?awardStat ps:P166 ?award .        # ... that has any of the values of ?award
            ?awardStat pq:P805 ?awardEdition . # Get the award edition (which is "subject of" XXth Academy Awards)
          }
          OPTIONAL {
            ?awardEdition wdt:P585 ?time . # the "point of time" of the Academy Award
            ?awardWork wdt:P57 ?director .
          }
        }
        GROUP BY ?awardWork ?award # We only want every movie once for a category (a 'random' person is selected)
      }
    } GROUP BY ?award
    ORDER BY ASC(?awardCount)
  }
  SERVICE wikibase:label {            # ... include the labels
    bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" .
  }
}
```

Por este motivo, se considera que existe una enorme complejidad en poner limitaciones sobre ciertos datos debido a que sería necesario interpretar la consulta SPARQL para poder revisar que se dispone de los permisos necesario para poder consultar la información. Aún pudiendo interpretarla, el mayor hándicap sería cubrir todos los posibles escenarios, lo cual se antoja bastante complicado.

En diferentes contextos se han definido numerosos modelos de control de acceso para sistemas de gestión de base de datos con el objetivo de implementar un mecanismo de seguridad que controle el acceso a datos confidenciales. Por ejemplo, modelo de vista para una base de datos relacional, modelo de Stonebraker para bases de datos Ingress, modelo de transformación de consultas, etc. Las propuestas asumen que se aplicaría un mecanismo similar para los operadores de selección y actualización, lo que generalmente no es cierto ya que no impone una coherencia entre la consulta y la modificación de datos.

Por ejemplo, en el caso de una consulta SPARQL, se asume que para dos predicados *p* y *q*, podemos seleccionar y modificar el valor de *p*, pero no se permite seleccionar el valor de *q*. Si se actualiza el valor de *p* usando una condición sobre el predicado *q*, se podría llegar a deducir el valor de *q*. Para demostrar este ejemplo, volviendo al mundo de bases de datos, aplicando un modelo de vista. Supongamos que tenemos una tabla `Employee` con los campos `name`, `city` y `salary` con la siguiente información.

| name   | city   | salary |
| ------ | ------ | ------ |
| Said   | Rennes | 45000  |
| Toutou | Madrid | 60000  |
| Aymane | London | 55000  |
| Alice  | Paris  | 90000  |
| Safa   | Paris  | 45000  |

Supongamos que un usuario no deba tener permisos para ver el dato de la columna `salary`. De acuerdo el modelo de vista, se crea una vista con los campos `name` y `city`. En este caso, se le da al usuario Bob permisos para hacer `select` en esta vista, pero no en la tabla, por tanto no podrá ver el salario. Hasta aquí parece que se no habrá ningún agujero de seguridad, pero supongamos que el usuario tiene permisos para actualizar datos de la tabla `Employee`. Actualiza por ejemplo la ciudad para los empleados que ganan 45000 y vuelve a consultar la vista para ver los valores que han cambiado, por tanto puede llegar a deducir quien tiene este valor. Este es un ejemplo de una base de datos SQL que quizás se puede ver de una forma más sencilla, pero el mismo problema se puede encontrar mediante consultas SPARQL.

Existe bibliografía acerca de este problema, como por ejemplo https://link.springer.com/chapter/10.1007/978-3-642-17650-0_2, en el que se trata la securización del acceso a datos mediante consultas SPARQL, pero se limitan a ser teorías e incluso no cubren todos los posibles aspectos que se pueden plantear.

También hay que tener en cuenta que desde la ejecución de consultas SPARQL se pueden realizar consultas federadas, para obtener información de diferentes fuentes. Este tipo de consultas tienen un gran impacto en el rendimiento al tener que consultar datos en diferentes fuentes, con lo que sería interesante que esto solo se permita realizar a determinados perfiles.

##### Solución planteada

Debido a que la consulta de datos mediante SPARQL permite acceder a la información de múltiples formas, es muy complicado poner limitaciones al acceso a determinada información de los recursos. Tampoco se observa que haya una solución de terceros que contemple la limitación a ciertos datos ni que sea completa. Para dar una solución completa para la seguridad del endpoint SPARQL, se deberá abordar desde 2 puntos de vista:

- Limitar SPARQL a perfiles
- Utilizar ACLs del endpoint SPARQL

###### Limitar SPARQL a perfiles

En este caso, se plantea que la consulta de datos SPARQL se limite solamente a ciertos perfiles que puedan visualizar toda la información del sistema. Mediante esta técnica se evitarían los problemas planteados anteriormente ya que los usuarios que puedan acceder son usuarios avanzados y tendrán privilegios suficientes para consultar toda la información.

Además, el tener la posibilidad de ejecutar consultas SPARQL, las cuales pueden llegar a ser muy pesadas, también puede influir mucho en el rendimiento del sistema. El hecho de limitar la ejecución de SPARQL a ciertos perfiles "autorizados" y especializados hace que este impacto se reduzca.

###### Utilizar ACLs del endpoint SPARQL

En este caso se haría uso de los ACLs definidos en el propio endpoint SPARQL, es decir en el triplestore que se esté utilizando, en este caso Fuseki. Mediante estas ACLs, se podría limitar el acceso a determinados grafos de conocimiento, o lo que es lo mismo recursos, para que el usuario no pueda verlos. Tendría la implicación de que en el momento que se quiera limitar el acceso a un dato habría que hacerlo a nivel de recurso y no a nivel de un dato en concreto ya que funciona como un interruptor, o pasa o no pasa.

Esto tiene como contrapartida, que al  hacerse a nivel de triplestore y no a nivel de solución, que si se desease sustituir el triplestore en algún momento, habría que volver a plantear la seguridad de los datos.

###### Impacto en consultas federadas

También habría que limitar la ejecución de consultas federadas a determinados roles autorizados para ello. No obstante, dado que el control de las consultas federadas se realizará desde el propio endpoint, el cual recibirá el token JWT, será cada uno de los nodos los que se encarguen de verificar los datos que puede ver cada usuario, por tanto será transparente de cara a la federación, salvo por el hecho de que será preciso enviar el token de seguridad en las peticiones a cada uno de los nodos.

### Servicio LDP

Desde la aplicación será necesario poder acceder al detalle de los recursos en diferentes formatos: turtle, json-ld, etc. La obtención de estos formatos está prevista que salga del API LDP de trellis mediante el uso de la cabecera `Accept`, por ejemplo: 

```
Accept: text/turtle
```

En este caso, la autorización se realiza utilizando WebAC, el cual permite definir la seguridad a nivel de recurso, pero dentro de cada recurso no sería posible definir reglas específicas para un dato en concreto del mismo.

Por ejemplo, mediante la siguiente condición se otorga a los usuarios `https://example.org/users/1` y `https://example.org/users/2` permisos de lectura y escritura sobre el recurso `https://example.org/container/resource`.

```
@prefix acl: <http://www.w3.org/ns/auth/acl#>.

<#authorization> a acl:Authorization ;
    acl:mode acl:Read, acl:Write ;
    acl:accessTo <https://example.org/container/resource> ;
    acl:agent <https://example.org/users/1>, <https://example.org/users/2> .
```
#### Solución planteada

En este caso se plantea utilizar los mecanismos que ofrece el servidor LDP, utilizando para ello WebAC para limitar así el acceso a determinados recursos, por ejemplo si se desea que determinados perfiles no puedan consultar cierta información de un proyecto se limitará el acceso por completo al recurso, es decir a toda la información relativa al proyecto.

- Más información: https://github.com/trellis-ldp/trellis/wiki/Authorization

## Bibliografía

- https://giancarloparma.com/2018/11/03/data-masking-with-jpa-and-spring-security/
- https://dzone.com/articles/masking-data-in-practice
- https://link.springer.com/chapter/10.1007/978-3-642-17650-0_2
- https://hal.inria.fr/hal-00815067/document
- http://wimmics.inria.fr/projects/shi3ld/
- https://jena.apache.org/documentation/permissions/example.html
- https://jena.apache.org/documentation/permissions/evaluator.html
- https://jena.apache.org/documentation/fuseki2/fuseki-security.html
- https://jena.apache.org/documentation/fuseki2/fuseki-data-access-control.html#endpoint-acl
- https://jena.apache.org/documentation/fuseki2/fuseki-data-access-control.html
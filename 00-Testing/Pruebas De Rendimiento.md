![](./img/logos_feder.png)



| Fecha        | 29/04/2021                                                   |
| ------------ | ------------------------------------------------------------ |
| Revisado por | Paloma Terán Pérez                                           |
| Módulo       | Pruebas de rendimiento                                       |
| Tipo         | Documento                                                    |
| Objetivo     | Documento con la información sobre las pruebas de rendimiento realizadas |



# Pruebas de rendimiento



[1. Introducción](#introducción)

[1.1 Hardware e infraestructura](#Hardware_e_infraestructura)

[2. Metodología](#metodología)

[2. Tipos de pruebas](#tipos-de-pruebas)

[2.1. Pruebas de carga](#pruebas-de-carga)

[2.2. Pruebas de estrés](#pruebas-de-estrés)

[2.2. Pruebas de estabilidad](#pruebas-de-estabilidad)

[2.2. Pruebas de pico](#pruebas-de-pico)

[3. Resultados de las pruebas](#resultados-de-las-pruebas)

[3.1. Configuración de jMeter](#configuración-de-jmeter)

[3.2. Resultados de las pruebas de carga de la API](#resultados-de-las-pruebas-de-carga-de-la-API)

[3.2. Resultados de las pruebas de estrés de la API](#resultados-de-las-pruebas-de-estrés-de-la-API)

[3.2. Resultados de las pruebas de estabilidad de la API](#resultados-de-las-pruebas-de-estabilidad-de-la-API)

[3.2. Resultados de las pruebas de pico de la API](#resultados-de-las-pruebas-de-pico-de-la-API)

[4. Anexo](#anexo)

[4.1. Endpoints](#endpoints)







## Introducción

En paralelo a las pruebas funcionales de la aplicación se realizarán una serie de pruebas de rendimiento del sistema. 

De cara a la obtención de unos buenos resultados será conveniente realizar las pruebas en un entorno lo más parecido al entorno real de producción.

Estas pruebas de rendimiento servirán, entre otras cosas, para: 

·    Demostrar que el sistema cumple los criterios de rendimiento.

·    Validar y verificar atributos de la calidad del sistema: escalabilidad, fiabilidad, uso de los recursos.

·    Medir qué partes del sistema o de carga de trabajo provocan que el conjunto rinda mal

Para la realización de las pruebas se utilizará JMeter, esta herramienta nos permitirá testear los distintos endpoints de la plataforma que dan soporte a las distintas funcionalidades.

En **JMeter**, un plan de pruebas es una jerarquía de componentes en forma de árbol. Cada nodo del árbol es un componente. A su vez, un componente es una instancia de un tipo de componente en el que se podrán ir realizando configuraciones con el fin de ajustar la prueba a un comportamiento de uso lo más real posible, para luego poder ir “jugando” con dichas configuraciones para “presionar” al sistema.

Otro de los puntos a testear en la plataforma, además de los endpoints que dan soporte al frontend, por ejemplo, serán las importaciones de datos. En ASIO dichas **importaciones** son ejecutadas por Jobs, lanzados mediante un programador de tareas. En este aparto las pruebas consistirán en el lanzamiento de distintas importaciones, variando tanto la concurrencia de las mismas, como el volumen de datos a importar.



### Hardware e infraestructura

El hardware e infraestructura dónde se encuentran los servicios sobre la que se lanzan las pruebas de rendimiento es:

| Nombre           | FRONT                                                        |
| ---------------- | ------------------------------------------------------------ |
| **SO**           | CentOS Linux release 7.7.1908                                |
| **MEMORIA**      | 16GB                                                         |
| **PROCESADOR**   | Intel Core i7 9xx (Nehalem Class Core i7)                    |
| **CORES**        | 4                                                            |
| **ARQUITECTURA** | 64                                                           |
| **PUERTOS**      | 22, 443, 80, 55555, 3030, 8081, 8070, 80, 81, 8080, 9321, 9326 |





## Metodología



De cara a la realización de las pruebas se realizarán las siguientes fases:

 

1. **Identificar el entorno de pruebas**. Identificar el entorno físico de pruebas y el entorno de producción, así como las herramientas y recursos de que dispone el equipo de prueba. El entorno físico incluye hardware, software y configuraciones de red. Tener desde el principio un profundo conocimiento de todo el entorno de prueba permite diseños de pruebas más eficientes. Facilita también la planificación y ayuda a identificar problemas en las pruebas en fases tempranas del proyecto. En algunas situaciones, este proceso debe ser revisado periódicamente durante todo el ciclo de vida del proyecto.
2. **Identificar los criterios de aceptación de rendimiento**. Determinar el tiempo de respuesta, el rendimiento, la utilización de los recursos y los objetivos y limitaciones. En general, el tiempo de respuesta concierne al usuario, el rendimiento al negocio, y la utilización de los recursos al sistema. Identificar cuáles serían criterios de éxito de rendimiento del proyecto para evaluar qué combinación de la configuración da lugar a un funcionamiento óptimo.
3. **Planificar y diseñar las pruebas**. Identificar los principales escenarios, determinar la variabilidad de los usuarios y la forma de simular esa variabilidad, definir los datos de las pruebas y establecer las métricas a recoger. Consolidar esta información en uno o más modelos de uso del sistema a implantar, ejecutarlo y analizarlo.
    En el caso de ASIO los principales escenarios serán los descritos anteriormente API e Importadores.
4. **Configurar el entorno de prueba**. Preparar el entorno de prueba, las herramientas y recursos necesarios para ejecutar cada una de las estrategias, así como las características y componentes disponibles para la prueba. Asegurarse de que el entorno de prueba se ha preparado para la monitorización de los recursos según sea necesario.
5. **Aplicar el diseño de la prueba**. Desarrollar las pruebas de rendimiento de acuerdo con el diseño del plan.
6. **Ejecutar la prueba**. Ejecutar y monitorizar las pruebas. Validar las pruebas, los datos de las pruebas y recoger los resultados. Ejecutar pruebas válidas para analizar, mientras se monitoriza la prueba y su entorno.
7. **Analizar los resultados**, realizar un informe y repetirlo. Consolidar y compartir los resultados de la prueba. Analizar los datos, tanto individualmente como con un equipo multidisciplinario. Volver a priorizar el resto de las pruebas y a ejecutarlas en caso de ser necesario. Cuando todas las métricas estén dentro de los límites aceptados, ninguno de los umbrales establecidos haya sido rebasados y toda la información deseada se ha reunido, las pruebas han acabado para el escenario definido por la configuración.



## Tipos de pruebas



### Pruebas de Carga


Permitirá observar el comportamiento del sistema bajo una cantidad esperada de peticiones. Esta carga puede ser el número esperado de usuarios concurrentes, utilizando la aplicación y realizando un número determinado de acciones, durante un tiempo establecido.

Esta prueba puede mostrar los **tiempos de respuesta** de cada una de las acciones importantes del sistema.



Para la visualización del estado de la memoria, CPUs, Disco, etc durante la realización de las distintas pruebas de carga, se ha utilizado [influxdb](https://www.influxdata.com/), que permite monitorizar el estado del sistema con gráficas y otro tipo de información gráfica, de forma personalizada.



#### Pruebas de Carga sobre el API

Sobre los distintos endpoints detallados en el Anexo se configurarán llamadas mediante JMeter. Dichas llamadas simularán el flujo de un usuario realizando consultas a través del frontal:

- Acceso a Categoría X
- Filtrado de la Categoría X
- Acceso al detalle de la entidad X

Cada uno de los usuarios (hilos) configurados en JMeter realizará un total de 15 acciones de las detalladas anteriormente.

- Usuarios Concurrentes: 100
- Acciones Por Usuario: 15
- Tiempo de la prueba: 15 min

De cara a la realización de las pruebas de carga, se ejecutará una primera prueba con un único usuario concurrente que nos ervería como _baseline_ ayudando a comprobar que todo el sistema es correcto.

Para la siguiente prueba se incrementará el número de usuarios a 20 y tras esta se irá incrementando un 20% de cada vez, hasta llegar al máximo de usuarios concurrentes establecidos (100)

Se obtendrá una tabla con los siguientes parámetros

- Nº de usuarios: Nº de usuarios concurrentes en la prueba
- Tiempo total de la prueba:
- Tiempo máximo(ms) de respuesta:
- Mediana de respuesta(ms)
- Latencia(ms)
- Fallos Totales
- Fallos (%)

Con la información obtenida en cada una de las pruebas se podrá pintar una gráfica de los distintos indicadores en función de la carga de usuarios.



#### Pruebas de Carga sobre el Importadores


Para las pruebas de carga de los importadores se ejecutarán tres importaciones consecutivas

Importación 1: Importará 100 elementos

Importación 2: importará 200 elementos

Importación 3: Importará 300 elementos



### Pruebas de Estrés

Las pruebas de estrés se utilizan para &quot;romper&quot; el sistema. Se irá doblando el número de usuarios que se agregan a la aplicación, ejecutando las pruebas hasta que se detecte la rotura del sistema. Con este tipo de prueba se podrá determinar la solidez del sistema en momentos de carga máxima



#### Pruebas de Estrés sobre el API

Sobre los distintos endpoints detallados en el Anexo se configurarán llamadas mediante JMeter. Dichas llamadas simularán el flujo de un usuario realizando consultas a través del frontal:

- Acceso a Categoría X
- Filtrado de la Categoría X
- Acceso al detalle de la entidad X

Cada uno de los usuarios (hilos) configurados en JMeter realizará un total de 15 acciones de las detalladas anteriormente.

- Usuarios Concurrentes: 100
- Acciones Por Usuario: 15
- Tiempo de la prueba: 15 min

Se irá doblando el número de usuarios en sucesivas pruebas hasta que se detecte el punto de ruptura.

Se obtendrá una tabla con los siguientes parámetros

- Nº de usuarios: Nº de usuarios concurrentes en la prueba
- Tiempo total de la prueba:
- Tiempo máximo(ms) de respuesta:
- Mediana de respuesta(ms)
- Latencia(ms)
- Fallos Totales
- Fallos (%)



#### Pruebas de Estrés sobre Importadores

Para las pruebas de carga de los importadores se ejecutarán sucesivas importaciones en las que se irá duplicando el número de datos, así como aumentando la concurrencia de las importaciones

Importación 1: Importará 100 elementos

Importación 2: Dos importadores con 200 elementos cada uno

Importación 3: Cuatro importadores con 400 elementos cada uno



### Pruebas de Estabilidad

Las pruebas de estabilidad se realizarán para comprobar si el sistema puede soportar una carga esperada continuada. Son útiles para determinar, por ejemplo, si hay alguna fuga de memoria.



#### Pruebas de Estabilidad sobre el API

Sobre los distintos endpoints detallados en el Anexo se configurarán llamadas mediante JMeter. Dichas llamadas simularán el flujo de un usuario realizando consultas a través del frontal:

- Acceso a Categoría X
- Filtrado de la Categoría X
- Acceso al detalle de la entidad X

Cada uno de los usuarios (hilos) configurados en JMeter realizará un número de acciones indeterminado para que las pruebas finalicen al acabar el tiempo independientemente del numero de acciones.

- Usuarios Concurrentes: 100
- Tiempo de la prueba: 2 horas

Las ejecuciones de cada hilo se establecerán en bucle para de esta forma establecer un flujo constante durante el tiempo de la prueba.

Se obtendrá una tabla con los siguientes parámetros

- Nº de usuarios: Nº de usuarios concurrentes en la prueba
- Tiempo total de la prueba:
- Tiempo máximo(ms) de respuesta:
- Mediana de respuesta(ms)
- Latencia(ms)
- Fallos Totales
- Fallos (%)



#### Pruebas de Estabilidad sobre el Importadores

Se concatenarán sucesivas importaciones en un periodo de 4 horas, durante este periodo, cada una de las importaciones a lanzar cargará un total de 200 registros.


### Pruebas de Pico

Como su nombre indica las pruebas de pico sirven para observar el comportamiento del sistema variando el número de usuarios, tanto cuando bajan como cuando tiene cambios drásticos en su carga.



#### Pruebas de Pico sobre el API

Como en las anteriores pruebas cada usuario (hilo) realizará las siguientes acciones:

- Acceso a Categoría X
- Filtrado de la Categoría X
- Acceso al detalle de la entidad X

Cada uno de los usuarios (hilos) configurados en JMeter realizará un total de 15 acciones de las detalladas anteriormente.

- Usuarios Concurrentes: 100
- Acciones Por Usuario: 15
- Tiempo de la prueba: 30 min

Para poder establecer los picos, tanto de máxima carga como de carga baja, se configurará el JMeter para generar en determinados momentos picos máximos de llamadas y momentos de baja carga.

Se obtendrá una tabla con los siguientes parámetros

- Nº de usuarios: Nº de usuarios concurrentes en la prueba
- Tiempo total de la prueba:
- Tiempo máximo(ms) de respuesta:
- Mediana de respuesta(ms)
- Latencia(ms)
- Fallos Totales
- Fallos (%)



#### Pruebas de Pico sobre el Importadores

Para las pruebas de pico en los importadores, se configurarán en un periodo de tiempo determinado hasta un máximo de 4 importaciones simultaneas, así como momentos en que sólo se realice una importación.





## Resultados de las pruebas



### Configuración de Jmeter

Se han establecido una serie de llamadas agrupadas por sección de la web, todas estas secciones corresponden con pantallas que hacen llamadas a servicios consultas SPARQL. Se han configurado las llamadas a las apis que se realizan en las siguientes pantallas:

- Estructuras de investigación:
  - Detalle de una estructura de investigación.
- Personal investigador:
  - Detalle de personal invertigador.
- Producción científica:
  - Detalle de un documento.
- Producción científica:
  - Detalle de un evento.
- Acciones de investigación:
  - Detalle de una patente.
- Acciones de investigación:
  - Detalle de un proyecto.
- Estadísticas.
- SPARQL.



En la siguiente imagen se pueden ver estas categorías en el árbol de Jmeter:

![Grupos en jMeter](./img/jmeter/list.JPG)



En esta otra imagen, se pueden ver las llamadas configuradas en algunas de estas categorías en el árbol de Jmeter y la configuración de una de ellas:

![Detalle de grupos en jMeter](./img/jmeter/list-detail.JPG)





Sobrecada una de las apis se ha añadido un timer aleatorio con máximo 3 segundos, para ejecutar los servicios con un tiempo entre ellos, como si se tratase de usuarios normales ejecutando la aplicación:

![Detalle de grupos en jMeter](./img/jmeter/list-timer.JPG)



**Se ha dejado el fichero creado para pruebas en el repositorio en el siguiente [link](./test-jMeter-ASIO.jmx).**



## Resultados de las pruebas de Carga de la API



Se han configurado, tal y como se explica en el apartado [pruebas de carga sobre el API](#pruebas-de-carga-sobre-el-api), los siguientes parámetros:

- Número de hilos (usuarios): 100
- Ramp-up period: 1 segundo
- Loop count: 15
- Se ha marcado la casilla "Especify threat lifetime" para limitar el tiempo que se va a estar ejecutando el hilo y se han marcado los valores:
  - Duration:  900 seconds
  - Startup delay: 0 seconds

![Configuración del hilo para los test de carga de la API](./img/jmeter/threat-test-carga.JPG)





Los resultados han sido satisfactorios, ya que, tras las pruebas de carga, en las imagenes que se muestran a continuación se puede observar que las llamadas se han podido ejecutar satisfactoriamente, de una forma bastante estable.

![Resultados de los test de carga en la gráfica](./img/jmeter/grafica-test-carga.png)





Los resultados obtenidos se pueden ver en la siguiente tabla:



| Label                                 | # Samples | Average | Min  | Max   | Std. Dev. | Error % | Throughput | Received KB/sec | Sent KB/sec | Avg. Bytes |
| ------------------------------------- | --------- | ------- | ---- | ----- | --------- | ------- | ---------- | --------------- | ----------- | ---------- |
| /api/university/organizationByType    | 600       | 456     | 86   | 2401  | 617.62    | 0.000%  | .69342     | 0.65            | 0.43        | 965.0      |
| /api/organization/search              | 600       | 264     | 103  | 1440  | 180.72    | 0.000%  | .69185     | 1.78            | 0.43        | 2635.0     |
| /api/organization/-1/T3JnYW5pemF0aW9u | 600       | 218     | 88   | 1301  | 133.49    | 0.000%  | .69138     | 0.63            | 0.49        | 933.0      |
| /api/person/area                      | 1199      | 225     | 83   | 1248  | 148.39    | 0.000%  | 1.34618    | 0.52            | 0.86        | 398.0      |
| /api/academicpublication/search       | 3952      | 336     | 117  | 15488 | 329.75    | 0.000%  | 4.43068    | 13.01           | 3.17        | 3006.1     |
| /api/project/search                   | 3200      | 284     | 118  | 7336  | 209.60    | 0.000%  | 3.61781    | 11.31           | 2.36        | 3202.0     |
| /api/document/search                  | 3928      | 382     | 142  | 15704 | 400.49    | 0.000%  | 4.42048    | 10.36           | 3.04        | 2398.8     |
| /api/patent/area                      | 1600      | 235     | 86   | 1677  | 168.91    | 0.000%  | 1.83115    | 6.07            | 1.16        | 3393.0     |
| /api/patent/search                    | 3795      | 274     | 102  | 1499  | 169.44    | 0.000%  | 4.29563    | 6.23            | 2.85        | 1484.9     |
| /api/researchstaff/search             | 1697      | 365     | 161  | 1891  | 186.33    | 0.000%  | 1.95527    | 3.49            | 1.28        | 1827.0     |
| /api/person/3519                      | 597       | 534     | 198  | 2645  | 398.88    | 0.000%  | .69581     | 0.46            | 0.46        | 683.0      |
| /api/event/search                     | 2737      | 416     | 144  | 3957  | 297.95    | 0.000%  | 3.18793    | 8.03            | 2.03        | 2579.5     |
| /api/otherpublication/search          | 2168      | 338     | 124  | 1671  | 192.00    | 0.000%  | 2.55587    | 6.13            | 1.65        | 2456.0     |
| /api/booksection/search/              | 1587      | 293     | 96   | 1390  | 201.69    | 0.000%  | 1.92826    | 1.44            | 1.35        | 766.0      |
| /api/document/M-21543-97/Qm9vaw==     | 534       | 310     | 127  | 1542  | 186.44    | 0.000%  | .64999     | 0.45            | 0.45        | 708.0      |
| /api/event/48/Q29uZmVyZW5jZQ==        | 501       | 281     | 102  | 967   | 178.78    | 0.000%  | .63378     | 0.47            | 0.43        | 758.0      |
| /api/project/byModality               | 1001      | 240     | 89   | 7303  | 275.13    | 0.000%  | 1.26698    | 2.97            | 0.77        | 2403.0     |
| /api/patent/1                         | 500       | 209     | 92   | 1326  | 133.65    | 0.000%  | .70431     | 0.46            | 0.41        | 671.0      |
| /api/project/1                        | 500       | 222     | 101  | 1023  | 127.14    | 0.000%  | .70343     | 0.27            | 0.44        | 398.0      |
| /api/person/search                    | 500       | 337     | 187  | 1203  | 132.38    | 0.000%  | .70050     | 1.25            | 0.44        | 1821.0     |
| TOTAL                                 | 31796     | 320     | 83   | 15704 | 278.41    | 0.000%  | 35.31692   | 73.25           | 23.45       | 2123.8     |



Teniendo en cuenta que los test se han lanzado entre las 12:25 del 10/05/2021 y las 12:40 del 10/05/2021, el resultado de la monitorización del sistema durante los test de carga se puede ver en las siguientes imágenes:

![Resultado general de la monitorización de test de carga](./img/jmeter/general-state-test-carga.png)



![Resultado de la monitorización de la ocupación de memoria de test de carga](./img/jmeter/memory-state-test-carga.png)



![Resultado de la monitorización de el uso de CPU de test de carga](./img/jmeter/cpu-state-test-carga.png)



![Resultado de la monitorización de el estado del disco de test de carga](./img/jmeter/disk-state-test-carga.png)



![Resultado de la monitorización de los procesos de test de carga](./img/jmeter/processes-state-test-carga.png)



## Resultados de las pruebas de Estrés de la API



Se han configurado, tal y como se explica en el apartado [pruebas de estrés sobre el API](#pruebas-de-estrés-sobre-el-api), los siguientes parámetros:

- Número de hilos (usuarios): 100/200/400/800/1600
- Ramp-up period: 1 segundo
- Loop count: 15
- Se ha marcado la casilla "Especify threat lifetime" para limitar el tiempo que se va a estar ejecutando el hilo y se han marcado los valores:
  - Duration:  900 seconds
  - Startup delay: 0 seconds



Se van duplicando el valor del número de hilos conforme se van ejecutando los test hasta obtener el valor al que "rompen" los servicios.



![Configuración del hilo para los test de carga de la API](./img/jmeter/threat-test-estres.JPG)





En las siguientes imágenes se pueden ver los resultados con 400 usuarios, que en este caso es al que han fallado servicios con valores entre un 20% de fallos y un 45% de fallos en los servicios, dado que las consultas SPARQL con las que se realizan las pruebas son un tanto complejas:

![Resultados de los test de carga en la gráfica](./img/jmeter/grafica-test-estres.png)



Los resultados obtenidos se pueden ver en la siguiente tabla:

| Label                                 | # Samples | Average | Min  | Max   | Std. Dev. | Error % | Throughput | Received KB/sec | Sent KB/sec | Avg. Bytes |
| ------------------------------------- | --------- | ------- | ---- | ----- | --------- | ------- | ---------- | --------------- | ----------- | ---------- |
| /api/university/organizationByType    | 937       | 8335    | 104  | 21063 | 9028.05   | 32.871% | 1.02926    | 1.61            | 0.43        | 1603.4     |
| /api/organization/search              | 929       | 8136    | 113  | 21063 | 9049.72   | 32.400% | 1.01565    | 2.70            | 0.43        | 2723.1     |
| /api/organization/-1/T3JnYW5pemF0aW9u | 920       | 8044    | 97   | 21069 | 9129.85   | 32.717% | 1.02800    | 1.59            | 0.49        | 1578.8     |
| /api/person/area                      | 1753      | 7020    | 87   | 21068 | 8349.81   | 24.244% | 1.92825    | 1.89            | 0.94        | 1006.3     |
| /api/academicpublication/search       | 5549      | 5937    | 122  | 21067 | 7753.54   | 19.823% | 6.14084    | 18.04           | 3.54        | 3008.1     |
| /api/project/search                   | 4221      | 5202    | 125  | 21068 | 7391.34   | 17.034% | 4.68351    | 14.42           | 2.55        | 3151.8     |
| /api/document/search                  | 5514      | 5635    | 148  | 21070 | 7636.49   | 18.462% | 6.14916    | 15.07           | 3.46        | 2509.9     |
| /api/patent/area                      | 2149      | 4933    | 94   | 21067 | 7416.42   | 16.659% | 2.41969    | 7.83            | 1.29        | 3312.0     |
| /api/patent/search                    | 4981      | 5113    | 106  | 21082 | 7275.76   | 16.402% | 5.61329    | 9.22            | 3.14        | 1681.2     |
| /api/researchstaff/search             | 2227      | 7123    | 165  | 21068 | 8542.56   | 25.101% | 2.58405    | 5.29            | 1.27        | 2098.1     |
| /api/person/3519                      | 831       | 7884    | 191  | 21063 | 8822.15   | 28.761% | .99472     | 1.28            | 0.47        | 1322.6     |
| /api/event/search                     | 3754      | 6136    | 148  | 21072 | 8087.12   | 21.843% | 4.50868    | 11.70           | 2.24        | 2658.3     |
| /api/otherpublication/search          | 2993      | 5922    | 124  | 21067 | 7976.24   | 20.748% | 3.66230    | 9.12            | 1.87        | 2549.6     |
| /api/booksection/search/              | 2224      | 4852    | 100  | 21066 | 7238.30   | 15.692% | 2.88451    | 3.10            | 1.71        | 1102.0     |
| /api/document/M-21543-97/Qm9vaw==     | 743       | 4744    | 124  | 21064 | 7172.53   | 15.478% | .98432     | 1.01            | 0.57        | 1048.4     |
| /api/event/48/Q29uZmVyZW5jZQ==        | 667       | 5539    | 106  | 21060 | 8024.52   | 20.390% | .93015     | 1.09            | 0.51        | 1196.2     |
| /api/project/byModality               | 1259      | 5219    | 99   | 21065 | 7742.47   | 18.348% | 1.76435    | 4.30            | 0.88        | 2495.5     |
| /api/patent/1                         | 616       | 5006    | 106  | 21062 | 7569.19   | 17.857% | .88798     | 0.93            | 0.43        | 1070.3     |
| /api/project/1                        | 566       | 5694    | 106  | 21065 | 8030.71   | 19.965% | .85278     | 0.75            | 0.43        | 898.9      |
| /api/person/search                    | 561       | 5394    | 210  | 21071 | 7598.74   | 17.825% | .84628     | 1.66            | 0.44        | 2014.6     |
| TOTAL                                 | 43394     | 5858    | 87   | 21082 | 7880.91   | 20.141% | 47.22720   | 105.67          | 25.15       | 2291.2     |



Teniendo en cuenta que los test se han lanzado entre las 13:32 del 10/05/2021 y las 13:47 del 10/05/2021, el resultado de la monitorización del sistema durante los test de carga se puede ver en las siguientes imágenes:

![Resultado general de la monitorización de test de estrés](./img/jmeter/general-state-test-estres.png)



![Resultado de la monitorización de la ocupación de memoria de test de estrés](./img/jmeter/memory-state-test-estres.png)



![Resultado de la monitorización de el uso de CPU de test de estrés](./img/jmeter/cpu-state-test-estres.png)



![Resultado de la monitorización de el estado del disco de test de estrés](./img/jmeter/disk-state-test-estres.png)



![Resultado de la monitorización de los procesos de test de estrés](./img/jmeter/processes-state-test-estres.png)



En estas imágenes se puede ver claramente cómo el uso de disco, de CPU sufren un aumento considerable, la memoria sufre un aumento menos significativo, y el número de procesos casi no sufre cambios. Por lo cual, para permitir un mayor número de peticiones, habría que plantearse mejorar el rendimiento del disco y mejorar las CPUs del servidor.



## Resultados de las pruebas de Estabilidad de la API



Se han configurado, tal y como se explica en el apartado [pruebas de estabilidad sobre el API](#pruebas-de-estabilidad-sobre-el-api), los siguientes parámetros:

- Número de hilos (usuarios): 100
- Ramp-up period: 1 segundo
- Loop count: Infinite
- Se ha marcado la casilla "Especify threat lifetime" para limitar el tiempo que se va a estar ejecutando el hilo y se han marcado los valores:
  - Duration:  7200 seconds
  - Startup delay: 0 seconds



![Configuración del hilo para los test de carga de la API](./img/jmeter/threat-test-estabilidad.JPG)



En las siguientes imágenes se pueden ver los resultados en gráfica y tabla. Se puede observar que los resultados se mantienen en una estabilidad en la tabla y que el porcentaje de error es inferior a un 1% en su mayoría.



![Resultados de los test de carga en la gráfica](./img/jmeter/grafica-test-estabilidad.png)





Los resultados obtenidos se pueden ver en la siguiente tabla:

| Label                                 | # Samples | Average | Min  | Max   | Std. Dev. | Error % | Throughput | Received KB/sec | Sent KB/sec | Avg. Bytes |
| ------------------------------------- | --------- | ------- | ---- | ----- | --------- | ------- | ---------- | --------------- | ----------- | ---------- |
| /api/university/organizationByType    | 4422      | 285     | 84   | 8576  | 371.29    | 0.000%  | .61547     | 0.58            | 0.38        | 965.0      |
| /api/organization/search              | 4422      | 306     | 98   | 10084 | 402.01    | 0.000%  | .61534     | 1.58            | 0.39        | 2635.0     |
| /api/organization/-1/T3JnYW5pemF0aW9u | 4422      | 271     | 86   | 9887  | 339.83    | 0.000%  | .61497     | 0.56            | 0.44        | 933.0      |
| /api/person/area                      | 8825      | 259     | 83   | 8990  | 319.03    | 0.000%  | 1.22659    | 0.48            | 0.79        | 398.0      |
| /api/academicpublication/search       | 30777     | 349     | 118  | 12955 | 337.93    | 0.000%  | 4.27930    | 12.63           | 3.06        | 3021.8     |
| /api/project/search                   | 26216     | 321     | 116  | 9638  | 312.13    | 0.000%  | 3.64586    | 11.40           | 2.37        | 3202.0     |
| /api/document/search                  | 30773     | 388     | 141  | 9650  | 344.43    | 0.000%  | 4.28089    | 10.09           | 2.94        | 2413.2     |
| /api/patent/area                      | 13119     | 267     | 85   | 9180  | 313.79    | 0.000%  | 1.82579    | 6.05            | 1.15        | 3393.0     |
| /api/patent/search                    | 30597     | 308     | 100  | 15414 | 345.48    | 0.000%  | 4.26018    | 6.36            | 2.81        | 1529.7     |
| /api/researchstaff/search             | 13133     | 389     | 158  | 9719  | 329.26    | 0.000%  | 1.83183    | 3.27            | 1.20        | 1827.0     |
| /api/person/3519                      | 4402      | 428     | 195  | 5241  | 297.41    | 0.000%  | .61475     | 0.41            | 0.41        | 683.0      |
| /api/event/search                     | 21945     | 387     | 138  | 9161  | 305.14    | 0.000%  | 3.06538    | 7.76            | 1.95        | 2591.6     |
| /api/otherpublication/search          | 17553     | 349     | 123  | 17489 | 386.31    | 0.000%  | 2.45591    | 5.89            | 1.58        | 2456.0     |
| /api/booksection/search/              | 13169     | 305     | 94   | 9782  | 396.67    | 0.000%  | 1.84709    | 1.38            | 1.30        | 766.0      |
| /api/document/M-21543-97/Qm9vaw==     | 4392      | 320     | 123  | 9240  | 406.75    | 0.000%  | .61642     | 0.43            | 0.43        | 708.0      |
| /api/event/48/Q29uZmVyZW5jZQ==        | 4367      | 286     | 100  | 8873  | 409.66    | 0.000%  | .61521     | 0.46            | 0.42        | 758.0      |
| /api/project/byModality               | 8707      | 263     | 88   | 15350 | 329.85    | 0.000%  | 1.22726    | 2.88            | 0.75        | 2403.0     |
| /api/patent/1                         | 4348      | 265     | 90   | 8736  | 305.91    | 0.000%  | .61411     | 0.40            | 0.36        | 671.0      |
| /api/project/1                        | 4329      | 275     | 99   | 5971  | 265.61    | 0.000%  | .61318     | 0.24            | 0.39        | 398.0      |
| /api/person/search                    | 4328      | 399     | 184  | 17477 | 373.69    | 0.000%  | .61308     | 1.09            | 0.39        | 1821.0     |
| TOTAL                                 | 254246    | 333     | 83   | 17489 | 344.62    | 0.000%  | 35.30878   | 73.64           | 23.38       | 2135.8     |



Teniendo en cuenta que los test se ha estado ejecutando entre las 10:15 del 11/05/2021 y las 12:15 del 11/05/2021, podemos observar en las siguientes imágenes que el sistema sufrió un aumento considerable del uso de recursos, pero a pesar de esto, como podemos ver en la tabla superior, durante las dos horas que duraron los test no ha fallado ningún servicio:

![Resultado general de la monitorización de test de estabilidad](./img/jmeter/general-state-test-estabilidad.png)



![Resultado de la monitorización de la ocupación de memoria de test de estabilidad](./img/jmeter/memory-state-test-estabilidad.png)



![Resultado de la monitorización de el uso de CPU de test de estabilidad](./img/jmeter/cpu-state-test-estabilidad.png)



![Resultado de la monitorización de el estado del disco de test de estabilidad](./img/jmeter/disk-state-test-estabilidad.png)



![Resultado de la monitorización de los procesos de test de estabilidad](./img/jmeter/processes-state-test-estabilidad.png)



## Resultados de las pruebas de Pico de la API



Se han configurado, tal y como se explica en el apartado [pruebas de pico sobre el API](#pruebas-de-pico-sobre-el-api), los siguientes parámetros:

- Número de hilos (usuarios): 100
- Ramp-up period: 1 segundo
- Loop count: 15
- Se ha marcado la casilla "Especify threat lifetime" para limitar el tiempo que se va a estar ejecutando el hilo y se han marcado los valores:
  - Duration:  1800 seconds
  - Startup delay: 0 second



![Configuración del hilo para los test de carga de la API](./img/jmeter/threat-test-pico.JPG)



En las siguientes imágenes se pueden ver los resultados en gráfica y tabla. Se puede observar que los resultados se mantienen en una estabilidad en la tabla y que el porcentaje de error es inferior a un 1% en su mayoría.

![Resultados de los test de carga de pico en la gráfica](./img/jmeter/grafica-test-pico.png)



Los resultados obtenidos se pueden ver en la siguiente tabla:



| Label                                 | # Samples | Average | Min  | Max   | Std. Dev. | Error % | Throughput | Received KB/sec | Sent KB/sec | Avg. Bytes |
| ------------------------------------- | --------- | ------- | ---- | ----- | --------- | ------- | ---------- | --------------- | ----------- | ---------- |
| /api/university/organizationByType    | 1092      | 476     | 84   | 19276 | 1486.73   | 0.458%  | .60818     | 0.58            | 0.38        | 974.3      |
| /api/organization/search              | 1092      | 343     | 96   | 19255 | 1011.84   | 0.275%  | .60821     | 1.57            | 0.38        | 2636.0     |
| /api/organization/-1/T3JnYW5pemF0aW9u | 1091      | 379     | 87   | 19274 | 1445.71   | 0.367%  | .61140     | 0.56            | 0.43        | 940.5      |
| /api/person/area                      | 2176      | 313     | 84   | 19256 | 1015.01   | 0.092%  | 1.21465    | 0.47            | 0.78        | 400.4      |
| /api/academicpublication/search       | 7491      | 434     | 119  | 21049 | 1240.40   | 0.133%  | 4.17929    | 12.32           | 2.98        | 3017.5     |
| /api/project/search                   | 6184      | 404     | 116  | 21028 | 1286.53   | 0.323%  | 3.45685    | 10.81           | 2.24        | 3201.3     |
| /api/document/search                  | 7491      | 463     | 140  | 21050 | 1154.02   | 0.107%  | 4.18881    | 9.86            | 2.87        | 2410.4     |
| /api/patent/area                      | 3099      | 340     | 86   | 19265 | 1195.88   | 0.258%  | 1.73665    | 5.75            | 1.10        | 3392.0     |
| /api/patent/search                    | 7260      | 384     | 100  | 31434 | 1245.75   | 0.275%  | 4.07718    | 6.03            | 2.69        | 1514.4     |
| /api/researchstaff/search             | 3166      | 478     | 164  | 21048 | 1308.79   | 0.221%  | 1.78850    | 3.20            | 1.17        | 1829.5     |
| /api/person/3519                      | 1086      | 483     | 204  | 16083 | 855.23    | 0.000%  | .61881     | 0.41            | 0.41        | 683.0      |
| /api/event/search                     | 5297      | 488     | 145  | 21050 | 1226.48   | 0.132%  | 3.00584    | 7.60            | 1.91        | 2589.0     |
| /api/otherpublication/search          | 4231      | 408     | 122  | 21051 | 1024.77   | 0.047%  | 2.42000    | 5.80            | 1.56        | 2456.2     |
| /api/booksection/search/              | 3174      | 371     | 95   | 15680 | 981.37    | 0.000%  | 1.83737    | 1.37            | 1.29        | 766.0      |
| /api/document/M-21543-97/Qm9vaw==     | 1062      | 382     | 124  | 15496 | 941.66    | 0.000%  | .61609     | 0.43            | 0.43        | 708.0      |
| /api/event/48/Q29uZmVyZW5jZQ==        | 1020      | 384     | 100  | 19227 | 1249.27   | 0.098%  | .60205     | 0.45            | 0.41        | 760.2      |
| /api/project/byModality               | 2013      | 390     | 89   | 19274 | 1474.11   | 0.397%  | 1.18991    | 2.80            | 0.72        | 2405.3     |
| /api/patent/1                         | 1000      | 384     | 91   | 19272 | 1399.61   | 0.200%  | .60046     | 0.40            | 0.35        | 675.6      |
| /api/project/1                        | 994       | 353     | 98   | 19265 | 1211.95   | 0.302%  | .60061     | 0.24            | 0.38        | 405.8      |
| /api/person/search                    | 992       | 503     | 191  | 19250 | 1425.94   | 0.403%  | .60318     | 1.08            | 0.38        | 1825.7     |
| TOTAL                                 | 61011     | 416     | 84   | 31434 | 1212.30   | 0.187%  | 33.87244   | 70.56           | 22.41       | 2133.0     |



Teniendo en cuenta que los test se han lanzado entre las 14:45 del 10/05/2021 y las 15:15 del 10/05/2021, se puede ver que hay picos durante esos minutos tanto en uso de memoria, CPU y disco como en el número de procesos, pero sin que afecte de forma alarmante en la latencia o el porcentaje de error de la respuesta de los servicios. El resultado de la monitorización del sistema durante los test de carga se puede ver en las siguientes imágenes:

![Resultado general de la monitorización de test de pico](./img/jmeter/general-state-test-pico.png)



![Resultado de la monitorización de la ocupación de memoria de test de pico](./img/jmeter/memory-state-test-pico.png)



![Resultado de la monitorización de el uso de CPU de test de pico](./img/jmeter/cpu-state-test-pico.png)



![Resultado de la monitorización de el estado del disco de test de pico](./img/jmeter/disk-state-test-pico.png)



![Resultado de la monitorización de los procesos de test de pico](./img/jmeter/processes-state-test-pico.png)





## Anexo

### Endpoints

- article-Article
- book-Book
- conference-Conference
- doctoral-thesis-Doctoral
- document-Document
- dossier-Dossier
- exhibit-Exhibit
- funding-Funding
- funding-source-Funding
- international-project-International
- invoice-Invoice
- master-thesis-Master
- patent-Patent
- person-Person
- project-Project
- project-expense-Project
- research-accreditation-Research Accreditation
- research-group-Research
- sparql-Sparql
- university-University
- article-Article
- book-Book
- document-Document
- patent-Patent
- person-Person
- project-Project






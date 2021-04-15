# Pruebas de carga



[1. Introducción](#introducción)

[2. Metodología](#metodología)

[2. Tipos de pruebas](#tipos-de-pruebas)







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



### Prueba de Carga


Permitirá observar el comportamiento del sistema bajo una cantidad esperada de peticiones. Esta carga puede ser el número esperado de usuarios concurrentes, utilizando la aplicación y realizando un número determinado de acciones, durante un tiempo establecido.

Esta prueba puede mostrar los **tiempos de respuesta** de cada una de las acciones importantes del sistema.



### Pruebas de Carga sobre el API

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



### Pruebas de Carga sobre el Importadores


Para las pruebas de carga de los importadores se ejecutarán tres importaciones consecutivas

Importación 1: Importará 100 elementos

Importación 2: importará 200 elementos

Importación 3: Importará 300 elementos



# Prueba de Estrés

Las pruebas de estrés se utilizan para &quot;romper&quot; el sistema. Se irá doblando el número de usuarios que se agregan a la aplicación, ejecutando las pruebas hasta que se detecte la rotura del sistema. Con este tipo de prueba se podrá determinar la solidez del sistema en momentos de carga máxima



### Pruebas de Estrés sobre el API

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



### Pruebas de Estrés sobre el Importadores

Para las pruebas de carga de los importadores se ejecutarán sucesivas importaciones en las que se irá duplicando el número de datos, así como aumentando la concurrencia de las importaciones

Importación 1: Importará 100 elementos

Importación 2: Dos importadores con 200 elementos cada uno

Importación 3: Cuatro importadores con 400 elementos cada uno



# Prueba de Estabilidad

Las pruebas de estabilidad se realizarán para comprobar si el sistema puede soportar una carga esperada continuada. Son útiles para determinar, por ejemplo, si hay alguna fuga de memoria.



### Pruebas de Estabilidad sobre el API

Sobre los distintos endpoints detallados en el Anexo se configurarán llamadas mediante JMeter. Dichas llamadas simularán el flujo de un usuario realizando consultas a través del frontal:

- Acceso a Categoría X
- Filtrado de la Categoría X
- Acceso al detalle de la entidad X

Cada uno de los usuarios (hilos) configurados en JMeter realizará un total de 15 acciones de las detalladas anteriormente.

- Usuarios Concurrentes: 100
- Acciones Por Usuario: 15
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



### Pruebas de Estabilidad sobre el Importadores

Se concatenarán sucesivas importaciones en un periodo de 4 horas, durante este periodo, cada una de las importaciones a lanzar cargará un total de 200 registros.


# Prueba de Pico

Como su nombre indica las pruebas de pico sirven para observar el comportamiento del sistema variando el número de usuarios, tanto cuando bajan como cuando tiene cambios drásticos en su carga.



### Pruebas de Pico sobre el API

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



### Pruebas de Pico sobre el Importadores

Para las pruebas de pico en los importadores, se configurarán en un periodo de tiempo determinado hasta un máximo de 4 importaciones simultaneas, así como momentos en que sólo se realice una importación.


# Anexo

# Endpoints

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






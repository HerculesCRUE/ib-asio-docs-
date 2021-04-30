![](./resources/logos_feder.png)



| Fecha        | 29/04/2021                               |
| ------------ | :--------------------------------------- |
| Revisado por | Paloma Terán Pérez                       |
| Módulo       | Estudio de herramientas                  |
| Tipo         | Documento                                |
| Objetivo     | Documento con el estudio de herramientas |



# Estudio de herramientas

## Automatización

El proceso de CI para ser efectivo requiere que esté automatizado y no dependa del error humano. Al ser un proceso rutinario es muy fácilmente llevado a una máquina que lo ejecute y así no tener que invertir tiempo humano en llevarlo a cabo. 

![Flujo de integración contínua CI](./resources/ci.png)

Lo habitual es que este proceso se lance por cada push / commit que se haga al repositorio en cada una de sus ramas. De esta forma se consigue tener una métricas en near real time, lo cual es muy útil para los desarrolladores, pudiendo detectar:

- Posibles fallos de compilación
- Bugs
- Code smells
- Fallos en testing
- Cobertura

Herramientas de automatización hay muchas, algunas de las más conocidas son:

- Jenkins
- Travis CI
- GitHub Actions

### Jenkins

[Jenkins](https://www.jenkins.io/) es un servidor de automatización Open Source, que se puede encargar de automatizar construcción, testing y despliegue facilitando así tanto la integración continua (CI) como la entrega continua (CD). 

Jenkins es muy potente ya que es fácilmente configurable y da soporte para la realización de tareas muy complejas, pero requiere de tener una instalación propia en un servidor (ya sea on-premise o IaaS).

### Travis CI

[Travis CI](https://travis-ci.org/) es un servicio de integración continua cloud. Se integra fácilmente con GitHub, ejecutando automáticamente las pipelines por cada push. Hasta hace unos meses era el servicio CI de facto para los proyectos opensource de GitHub.

Al ser un servicio SaaS, no requiere instalación, simplemente es necesario logarse usando la cuenta de GitHub y con eso es suficiente para que esté escuchando los push. Las tareas se definen mediante el fichero `.travis.yml` ubicado en la raíz del repositorio.

![Flujo para GitHub con Travis](./resources/github-travis.png)

En cuanto a precios, tiene planes free para proyectos opensource, aunque para finales de 2020 se eliminarán estos planes.

### GitHub Actions

[GitHub Actions](https://github.com/features/actions) es el servicio de GitHub para la automatización de workflows. Se trata de un servicio completamente integrado dentro de la plataforma GitHub, lo cual hace que no se dependa de componentes externos o de terceros para lanza las pipelines.

![Flujo para GitHub con Actions](./resources/github-actions.png)

Tras las ultimas actualizaciones se ha ido añadido más y más características que hacen de GitHub Actions un sistema de automatización maduro y una alternativa muy fuerte a otros servicios como Travis CI, más teniendo en cuenta el cambio de planes de este último. Aunque es posible que Travis CI disponga de más funcionalidades, hoy día GitHub Actions es un servicio que será suficiente para la mayoría de los escenarios, siendo el recomendado en los proyectos OpenSource actuales.

En cuanto a la configuración, GitHub observará los ficheros en formato YAML que existan dentro de `.github/workflows`, donde se definirán todas las pipelines necesarias, por ejemplo:

```yml
name: Java CI

on: 
  push:
  pull_request:
  schedule:
    - cron: '0 0 * * 0' # weekly

jobs:
  build:
    runs-on: ubuntu-latest 

    steps:
      - uses: actions/checkout@v2
      - name: Set up JDK 1.8
        uses: actions/setup-java@v1
        with:
          java-version: 1.8 
      - name: Build with Maven
        run: ./mvnw -B verify 
```

### Conclusión

Una vez analizados los principales sistemas de automatización disponibles, se cree que la mejor opción sería GitHub Actions al tratarse de un servicio completamente integrado dentro de GitHub no teniendo que depender de terceros (Travis CI) ni de instalaciones propias (Jenkins). Como se comentó anteriormente, GitHub Actions ha ido ganando popularidad a medida que se han añadido funcionalidades siendo hoy día una muy fuerte alternativa a soluciones más usadas tradicionalmente.

## Análisis estático

Tener un sistema de CI aporta una serie de beneficios indudables, como puede ser garantizar que el código se integra correctamente o que pasan los tests, pero necesita un añadido que es es análisis estático del código. Este tipo de herramientas permiten ejecutar una serie de reglas sobre el código detectando posibles bugs, code smells o si no se siguen los estándares de codificación, entre otras.

Las herramientas de análisis estático de código más usadas son las siguientes:

- SonarCloud
- Codacy

### SonarCloud

[SonarCloud](https://sonarcloud.io/) es una plataforma cloud, lider del sector, que permite gestionar la calidad del código controlando los 7 ejes principales:

- Arquitectura y diseño
- Errores potenciales
- Reglas de codificación
- Comentarios
- Duplicidades
- Pruebas unitarias
- Complejidad

Esta plataforma realiza varios análisis de nuestro código a través de otras herramientas (Checkstyle, PMD, Findbugs, JUnit, …) y presenta de manera unificada a través de su interfaz la información, generada por ellas en forma de métricas, donde podremos ver de forma detallada los puntos débiles de nuestro proyecto, como errores potenciales en el código, escasez de comentarios, clases demasiado complejas, escasez de cobertura de las pruebas unitarias, etc.

Las características principales son:

- +20 lenguajes: incluyendo Java, C#, C/C++, JS, Typescript, Python, Go, Swift, Cobol, Apex, PHP, Kotlin, Ruby, Scala, HTML5, CSS3, ABAP, Flex, Objective-C, PL/I, PL/SQL, RPG, T-SQL, VB.Net, VB6, XML
- Cientos de reglas definidas para validar la calidad del código, así como posibles bugs, mediante un análisis estático
- Integración con herramientas CI cloud, como Travis CI o GitHub Actions
- Gestión de la cobertura
- Gestión multirama
- Análisis de la complejidad ciclomática
- Duplicidades
- Definición de Quality Gates
- Escalable

En cuanto a planes de precios, para proyectos Open Source públicos es gratuita.

### Codacy

[Codacy](https://www.codacy.com/) es una herramienta de análisis estático de la calidad del código, que ayuda a los desarrolladores a crear mejor software. Se trata de una herramienta cloud, también integrable con otros sistemas de CI. Entre las características principales se puede enumerar:

- Análisis estático
- Complejidad ciclomática
- Duplicidades de código
- Cobertura de testing unitario
- 10 lenguajes soportados: Go, Java, JS, PHP, Python, Ruby, Scala, Shell, Swift y Typescript

En cuanto a planes de precios, para proyectos Open Source públicos es gratuita.

### Conclusión

A priori, tanto Codacy como SonarCloud cumplen para las características del proyecto (lenguajes, OpenSource, ...). No obstante, es cierto que SonarCloud tiene mayor soporte de lenguajes y es el líder del sector, con lo que se propone la utilización de este analizador estático.

## Integración continua de ontologías

Las ontologías como tal no son programas. Es decir no expresan un algoritmo, si no que declaran y modelan un dominio. Por tanto, cuando queremos asegurar que el dominio descrito por una ontología es el que nosotros queremos, tenemos que ejecutar pruebas sobre la ontología. Este tipo de pruebas no pueden ser ejecutadas en sistemas como TravisCI o similares. Por lo tanto se ha desarrollado una herramienta similar cuya única función es realizar integración continua de ontologías a través de Shape Expressions y consultas de SPARQL.

### Ontolo-CI

[Ontolo-CI](https://github.com/weso/ontolo-ci) es una herramienta implementada ad-hoc para realizar integración continua de ontologías. Gracias a esta integración continua se puede asegurar que la ontología que se está desarrollando cumple con los requisitos que se esperan de ella. Además, es fundamental para poder realizar un control de versiones efectivo sobre ontologías. Entre las características principales se puede enumerar:

- Ejecución de tests con Shape Expressions.
- Ejecución de preguntas de competencia con consultas SPARQL.
- Localización automática de errores de sintaxis en las ontologías.
- Informes visuales con el resultado de las pruebas realizadas.

### Conclusión

Una vez se hayan unificado las ontologías en un único repositorio de código se deberá de realizar una instalación de una instancia de Ontolo-Ci en el entorno de despliegue de La Universidad de Murcia. Esta instancia se comunicará con el repositorio donde esté alojada la ontología de forma que realice el proceso de integración continua.
![](./img/logos_feder.png)

| Entregable     | Servicio API de validación de RDF                            |
| -------------- | ------------------------------------------------------------ |
| Fecha          | 15/04/2021                                                   |
| Proyecto       | [ASIO](https://www.um.es/web/hercules/proyectos/asio) (Arquitectura Semántica e Infraestructura Ontológica) en el marco de la iniciativa [Hércules](https://www.um.es/web/hercules/) para la Semántica de Datos de Investigación de Universidades que forma parte de [CRUE-TIC](https://www.crue.org/proyecto/hercules/) |
| Módulo         | Librería de validación de RDF                  |
| Tipo           | Software                                                     |
| Objetivo       | Servicio web en formato API para la validación de RDF |
| Estado         | **100%**  |
| API         | [https://github.com/HerculesCRUE/ib-hercules-rdf-validator-back](https://github.com/HerculesCRUE/ib-hercules-rdf-validator-back) |
| Cliente         | [https://github.com/HerculesCRUE/ib-hercules-rdf-validator-client](https://github.com/HerculesCRUE/ib-hercules-rdf-validator-client) |


# Librería de validación de RDF

La librería de validación de RDF cumple la función de averiguar si unos datos expresados por medio de RDF están conformes a unas shape expressions. Para más información sobre el proceso de validación recomendamos leer [Validating RDF data book](http://book.validatingrdf.com). 

Tal y como se especificaba en el pliego la librería se presenta como dos componentes. Por una parte tenemos una [API](https://github.com/HerculesCRUE/ib-hercules-rdf-validator-back/blob/herculesCRUE/main/README.md) que puede ser consumida de forma independiente. Y, por otra parte, tenemos el servicio web que se presenta como un [cliente](https://github.com/HerculesCRUE/ib-hercules-rdf-validator-client) que ataca la API mencionada.

## HErcules RDF Validator Back

RDF playground. This repository contains the server part of the Hércules RDF Validator Back web app.
The server has been implemented in Scala using the [http4s](https://http4s.org/) library. 

### More info

* The client part of Hércules RDF Validator Back has been separated to a [React app](https://github.com/weso/rdfshape-client).
* Background info about validating RDF: [Validating RDF data book](http://book.validatingrdf.com)
* [How-to](https://github.com/labra/rdfshape/wiki/Tutorial) explains how to use Hércules RDF Validator Back to validate RDF

### Deployed versions of Hércules RDF Validator Back

Hércules RDF Validator Back is already deployed [here](http://rdfshape.weso.es).

### Installation and Local Deployment 

#### Requirements

* Hércules RDF Validator Back server requires [SBT](https://www.scala-sbt.org/) to be built

#### Deploy at local machine

* Clone the [github repository](https://github.com/labra/rdfshape)

* Go to directory where Hércules RDF Validator Back source code is located and execute `sbt run`

* After some time downloading and compiling           uri(
the source code it will start the application, which can be accessed at: [localhost:8080](http://localhost:8080)

* To use a different port run `sbt "run --server --port <PortNumber>"`

#### Build a docker image

* Install [SBT](https://www.scala-sbt.org/)

* Run `sbt docker:publishLocal` which will create a docker file at `target/docker`

#### Dependencies

Hércules RDF Validator Back server has been implemented in Scala using the following libraries:

* [SHaclEX](https://github.com/labra/shaclex): a Scala implementation of ShEx and SHACL.
* [http4s](https://http4s.org/): a purely functional library for http.
* [cats](https://typelevel.org/cats/): a library for functional programming in Scala.
* [UMLShaclex](https://github.com/labra/shaclex): contains the visualization code that converts schemas to UML diagrams
* [SRDF](http://www.weso.es/srdf/): is the library used to handle RDF. It is a simple interface with 2 implementations, one in [Apache Jena](https://jena.apache.org/), and the other in [RDF4j](https://rdf4j.org/).
* [Any23](https://any23.apache.org/): is used by Hércules RDF Validator Back to convert HTML files in RDFa and Microdata to RDF.
* [Topbraid SHACL API](https://github.com/TopQuadrant/shacl): is used to add another SHACL engine apart of the SHaclEX and Apache Jena SHACL engines.


## Hercules RDF Validator Client

This is the front-end part of the [https://github.com/HerculesCRUE/ib-hercules-rdf-validator-back](https://github.com/HerculesCRUE/ib-hercules-rdf-validator-back) tool. 

This project is a pure client library implemented with [React](http://reactjs.org/). 
It was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

[![Build Status](https://travis-ci.org/weso/rdfshape-client.svg?branch=master)](https://travis-ci.org/weso/rdfshape-client)


### Available Scripts

In the project directory, you can run:

#### `npm start`

Runs the app in the development mode.<br>
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br>
You will also see any lint errors in the console.

#### `npm test`

Launches the test runner in the interactive watch mode.<br>
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

#### `npm run build`

Builds the app for production to the `build` folder.<br>
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br>
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

#### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (Webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.




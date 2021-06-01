

# Instalador ASIO

El presente documento, describe el Script de instalación implementado con python.

Se puede encontrar una documentación completa del proceso de instalación en el [Manual de despliegue](https://github.com/HerculesCRUE/ib-asio-docs-/blob/master/00-Arquitectura/Manual_de_despliegue/manual_de_despliegue.md), ya que dicho Script implementa los pasos aquí descritos, y en la presente documentación se referenciaran varios de los apartados aquí descritos.

En cualquier caso debe usarse para el completo entendimiento de las acciones aquí descritas la información contenida en el [Manual de despliegue](https://github.com/HerculesCRUE/ib-asio-docs-/blob/master/00-Arquitectura/Manual_de_despliegue/manual_de_despliegue.md). 

## Requisitos Hardware

Los requisitos hardware son obviamente los mismos que en el proceso de instalación manual, puede servir como referencia la estimación para los entornos de desarrollo y test que ha resultado ser bastante ajustada a la realidad, descrita en la sección [Hardware e infraestructura para los despliegues.](https://github.com/HerculesCRUE/ib-asio-docs-/blob/master/00-Arquitectura/Manual_de_despliegue/manual_de_despliegue.md#21-hardware-y-e-infraestructura-para-los-despliegues)

Básicamente se estima unos 16GB de RAM para los servicios de DB y de FRONT y 32GB para los servicios de BACK, es decir un total de 64 GB. 

## Requisitos Software

Los requisitos software son los mismos que los descritos en la sección [instalación de dependencias](https://github.com/HerculesCRUE/ib-asio-docs-/blob/master/00-Arquitectura/Manual_de_despliegue/manual_de_despliegue.md#31-instalaciones-de-dependencias).

Obviamente hay que adaptar lo aquí descrito (para una máquina Unix), a el tipo de máquina donde queremos realizar el despliegue: 

* [Docker](https://docs.docker.com/get-docker/)
* [docker-compose](https://docs.docker.com/compose/install/)
* [Python 3](https://www.python.org/downloads/)

Adicionalmente a esto, puede ser necesario configurar para algunos servicios la cantidad de memoria de la maquina virtual java dentro para los contenedores docker.

Para hacerlo en maquinas **Windows** puede ser necesario ejecutar los siguientes comandos:

```sh
wsl -d docker-desktop
sysctl -w vm.max_map_count=262144
```

Para **Linux**:

```sh
sudo sysctl -w vm.max_map_count=262144
sudo sysctl -w fs.file-max=65536
```

## 

Por otro lado en entornos Windows es necesario configurar Docker con configuración experiemental, que integra docker-compose en el motor de docker.



![config](./img/docker.config.png)



```{
  "registry-mirrors": [],
  "insecure-registries": [],
  "debug": false,
  "experimental": true,
  "builder": {
    "gc": {
      "enabled": true,
      "defaultKeepStorage": "20GB"
    }
  }
}
```

Por otro lado para instalar las dependencias en de el proyecto, antes de ejecutar el Script es necesario, ejecutar el comando`pip install -r requirements.txt` desde la raíz del instalador.

## Instalador

Podemos ejecutar el instalador mediante el comando

```Python deployer.py```

Tras lo cual podremos ver el menú de despliegue

![menu](./img/menu.png)



Básicamente el menú ofrece opciones de despliegue y parada de los servicios relacionados con Front, DB, Backend, todos los servicios y Portanier.

El despliegue se realiza mediante la ejecución de distintos docker-compose  para orquestar el despliegue de los contenedores docker. Las imágenes publicas de dichos contenedores, están alojadas en [docker hub](https://hub.docker.com/search?q=herculescrue&type=image), por lo que la primera vez que se invoque el despliegue desde una determinada maquina, se procederá a la descarga de todas las imágenes definidas en el fichero docker-compose.yml.

Tal como se comenta en el documento [Manual de despliegue](https://github.com/HerculesCRUE/ib-asio-docs-/blob/master/00-Arquitectura/Manual_de_despliegue/manual_de_despliegue.md#21-hardware-y-e-infraestructura-para-los-despliegues), existen ciertas dependencias entre servicios, básicamente, a nivel de el instalador, es necesario seguir el siguiente orden:

1. Despliegue de servicios de DB
2. Despliegue de servicios de FRONT
3. Despliegue de servicio de BACK

### Despliegue de servicios BD

La ejecución de la opción 2 (Desplegar servicios de Base de Datos),  automatizara el despliegue de los servicios descritos en la sección [Servicios desplegados en DB](https://github.com/HerculesCRUE/ib-asio-docs-/blob/master/00-Arquitectura/Manual_de_despliegue/manual_de_despliegue.md#241-servicios-desplegados-en-db) , siguiendo los pasos que se describen en [Despliegue de Maquina DB](https://github.com/HerculesCRUE/ib-asio-docs-/blob/master/00-Arquitectura/Manual_de_despliegue/manual_de_despliegue.md#321-m%C3%A1quina-db) del manual de despliegue  (a excepción del servicio Portainer, que debe instalarse una vez por cada máquina física).

Los servicios desplegados, lo harán con un nombre de prefijo ASIO_DB_XXXX, por lo que  podemos visualizarlos mediante el comando 

`docker ps | grep ASIO_DB`

### Despliegue de servicios FRONT

La ejecución de la opción 2 (Desplegar servicios de Frontal),  automatizara el despliegue de los servicios descritos en la sección [Servicios desplegados en FRONT](https://github.com/HerculesCRUE/ib-asio-docs-/blob/master/00-Arquitectura/Manual_de_despliegue/manual_de_despliegue.md#242-servicios-desplegados-en-front) , siguiendo los pasos que se describen en [Despliegue de Maquina Front](https://github.com/HerculesCRUE/ib-asio-docs-/blob/master/00-Arquitectura/Manual_de_despliegue/manual_de_despliegue.md#322-m%C3%A1quina-front) del manual de despliegue (a excepción del servicio Portainer, que debe instalarse una vez por cada máquina física).

Los servicios desplegados, lo harán con un nombre de prefijo ASIO_FRONT_XXXX, por lo que  podemos visualizarlos mediante el comando 

`docker ps | grep ASIO_FRONT`

### Despliegue de servicios BACK

La ejecución de la opción 2 (Desplegar servicios de Backend),  automatizara el despliegue de los servicios descritos en la sección [Servicios desplegados en Backend](https://github.com/HerculesCRUE/ib-asio-docs-/blob/master/00-Arquitectura/Manual_de_despliegue/manual_de_despliegue.md#243-servicios-desplegados-en-back) , siguiendo los pasos que se describen en [Despliegue de Maquina DB](https://github.com/HerculesCRUE/ib-asio-docs-/blob/master/00-Arquitectura/Manual_de_despliegue/manual_de_despliegue.md#323-m%C3%A1quina-back) del manual de despliegue (a excepción del servicio Portainer, que debe instalarse una vez por cada máquina física).

Los servicios desplegados, lo harán con un nombre de prefijo ASIO_FRONT_XXXX, por lo que  podemos visualizarlos mediante el comando 

`docker ps | grep ASIO_FRONT`

## Ficheros relevantes para el instalador

Dentro del directorio environments, podemos ver todos los ficheros de configuración que afectan a el despliegue de los contenedores, donde podemos ver los directorios back, db, front y portainer, que obviamente, contienen los ficheros relativos a el cada uno de los despliegues del mismo nombre.

En cada uno de las carpetas podemos ver distintos tipos de dicheros:

### Ficheros docker-compose

Son los que orquestan el despliegue de los servicios, normalmente existen varios asociados al despliegue de una sola maquina.

Todos los que se invocaran están descritos en cada uno de los aparatados por maquinas en el apartados [despliegue de servicios](https://github.com/HerculesCRUE/ib-asio-docs-/blob/master/00-Arquitectura/Manual_de_despliegue/manual_de_despliegue.md#32-despliegue-de-servicios), del documento manual de despliegue.

### Ficheros para variables de entorno

Siempre se encuentran (de existir) en el directorio **env** y tienen la extensión **.env**.

En principio ya están configurados adecuadamente para funcionar, pero si se desea alterar el comportamiento de algún servicio puede ser necesario cambiar algunos valores, tal y como se describe en el documentación disponible en el repositorio de cada uno de los servicios.

### Ficheros de configuración

Adicionalmente, algunos servicios precisan de ficheros de configuración.

Podemos encontrarlos siempre dentro de la ruta de cada una de las maquinas, normalmente con el nombre del servicio.

En principio ya están configurados adecuadamente para funcionar, pero si se desea alterar el comportamiento de algún servicio puede ser necesario cambiar algunos valores, siendo conveniente para ello, consultar la documentación especifica del servicio.




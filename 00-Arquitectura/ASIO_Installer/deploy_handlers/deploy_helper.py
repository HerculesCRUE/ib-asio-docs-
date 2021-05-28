from deploy_handlers.docker_helper import DockerHelper
import sys
is_windows = sys.platform.startswith('win')
import os
import Utils.utils as u


def deploy_db():
    dh = DockerHelper()
    db_path = 'environments/db'
    project_name = 'ASIO_DB'
    dh.run_compose('docker-compose.yml', db_path, project_name, True)
    dh.run_compose('docker-compose-redis.yml', db_path, project_name, True)
    dh.run_compose('docker-compose-wikibase.yml', db_path, project_name, True)


def stop_db():
    dh = DockerHelper()
    db_path = 'environments/db'
    project_name = 'ASIO_DB'
    dh.stop_compose('docker-compose.yml', db_path, project_name)
    dh.stop_compose('docker-compose-redis.yml', db_path, project_name)
    dh.stop_compose('docker-compose-wikibase.yml', db_path, project_name)


def deploy_front(db_address, back_address):
    dh = DockerHelper()
    project_name = 'ASIO_FRONT'
    db_path = 'environments/front'
    os.environ.putenv('BACK_HOST', db_address)
    os.environ.putenv('DB_HOST', back_address)
    dh.run_compose('docker-compose.yml', db_path, project_name, True)
    dh.run_compose('docker-compose-service-discovery.yml', db_path, project_name, True)
    dh.run_compose('docker-compose-bechmarks.yml', db_path, project_name, True)

    option = u.option_handler("Desplegar Wikibase Ontologico [S|n]", "Valor no valido, solo son validos los valores [s|n]", None, ['S', 'N'], 0)
    if option == 0:
        dh.run_compose('docker-compose.yml', db_path+'/io', 'ASIO_FRONT_IO', True)

    option = u.option_handler("Desplegar Reports [S|n]", "Valor no valido, solo son validos los valores [s|n]", None, ['S', 'N'], 0)
    if option == 0:
        dh.run_compose('docker-compose.yml', db_path+'/reports', 'ASIO_REPORTS', True)

    option = u.option_handler("Desplegar ONTOLOCI (Integración continua para ontologías) [S|n]", "Valor no valido, solo son validos los valores [s|n]", None, ['S', 'N'], 0)
    if option == 0:
        dh.run_compose('docker-compose.yml', db_path+'/deploy_ontoloci', 'ASIO_ONTOLOCI', True)

    option = u.option_handler("Desplegar SAML TEST [S|n]", "Valor no valido, solo son validos los valores [s|n]", None, ['S', 'N'], 0)
    if option == 0:
        dh.run_compose('docker-compose.yml', db_path+'/samltest', 'ASIO_SAMLTEST', True)

    dh.run_compose('docker-compose.yml', db_path+'/gateway', 'ASIO_GATEWAY', True)
    print("\tWeb publication backend publicado diponible en https://linkeddata1test.um.es")
    print("\tBenchmarks publicado en http://benchmarks.hercules1testgrp.atica.um.es")
    print("\tGraylog publicado en https://monitorld1test.um.es")
    print("\tKeycloak publicado en http://authld1test.um.es")
    print("\tServidor LDP (Trellis) publicado en http://ldpld1test.um.es")
    print("\tPortainer (Monitorización de contenedores docker) publicado en http://portainer.hercules1testgrp.atica.um.es")
    print("\tReports (Test) publicado en http://reports.hercules1testgrp.atica.um.es")
    print("\tWikibase (Front) publicado en http://wb.hercules1testgrp.atica.um.es")
    print("\tWikibase (Endpoint) publicado en http://wbquery.hercules1testgrp.atica.um.es")
    print("Recuerde meter los dominios descritos en el fichero host de su equipo")
    print("Completado despliegue de maquina FRONT, " +
          "Recuerde meter los dominios enumerados en el fichero host de su equipo")


def stop_front():
    dh = DockerHelper()
    db_path = 'environments/front'
    project_name = 'ASIO_FRONT'
    dh.stop_compose('docker-compose.yml', db_path, project_name)
    dh.stop_compose('docker-compose-service-discovery.yml', db_path, project_name)
    dh.stop_compose('docker-compose-bechmarks.yml', db_path, project_name)

    option = u.option_handler("Parar Wikibase Ontologico [S|n]", "Valor no valido, solo son validos los valores [s|n]", None, ['S', 'N'], 0)
    if option == 0:
        dh.stop_compose('docker-compose.yml', db_path+'/io', 'ASIO_FRONT_IO')

    option = u.option_handler("Parar Reports [S|n]", "Valor no valido, solo son validos los valores [s|n]", None, ['S', 'N'], 0)
    if option == 0:
        dh.stop_compose('docker-compose.yml', db_path+'/reports', 'ASIO_REPORTS')

    option = u.option_handler("Parar ONTOLOCI (Integración continua para ontologías) [S|n]", "Valor no valido, solo son validos los valores [s|n]", None, ['S', 'N'], 0)
    if option == 0:
        dh.stop_compose('docker-compose.yml', db_path+'/deploy_ontoloci', 'ASIO_ONTOLOCI')

    option = u.option_handler("Parar SAML TEST [S|n]", "Valor no valido, solo son validos los valores [s|n]", None, ['S', 'N'], 0)
    if option == 0:
        dh.stop_compose('docker-compose.yml', db_path+'/samltest', 'ASIO_SAMLTEST')

    dh.stop_compose('docker-compose.yml', db_path+'/gateway', 'ASIO_GATEWAY')


def deploy_back(db_address, front_address):
    dh = DockerHelper()
    project_name = 'ASIO_BACK'
    db_path = 'environments/back'
    os.environ.putenv('DB_HOST', db_address)
    os.environ.putenv('FRONT_HOST', front_address)
    dh.run_compose('docker-compose.yml', db_path, project_name, True)
    dh.run_compose('docker-compose-pdi.yml', db_path, project_name, True)

    option = u.option_handler("Desplegar Wikibase IO [S|n]", "Valor no valido, solo son validos los valores [s|n]", None, ['S', 'N'], 0)
    if option == 0:
        dh.run_compose('docker-compose.yml', db_path+'/wikibase-IO', 'ASIO_BACK_WB_IO', True)


def stop_back():
    dh = DockerHelper()
    db_path = 'environments/back'
    project_name = 'ASIO_BACK'
    dh.stop_compose('docker-compose.yml', db_path, project_name)
    # dh.stop_compose('docker-compose-pdi.yml', db_path, project_name)


def deploy_portainer():
    dh = DockerHelper()
    db_path = 'environments/portainer'
    project_name = 'ASIO_PORTAINER'
    if not is_windows:
        print('Desplegando Portainer para Linux')
        dh.run_compose('docker-compose-ce.yml', db_path, project_name, True)
    else:
        print('Desplegando Portainer para windows')
        dh.run_compose('docker-compose-ce.yml', db_path, project_name, True)
        #dh.run_docker(['docker run -p 9000:9000 --name portainer --restart always -v \\.\pipe\docker_engine:\\.\pipe\docker_engine -v portainer_data:C:\data portainer/portainer-ce'])


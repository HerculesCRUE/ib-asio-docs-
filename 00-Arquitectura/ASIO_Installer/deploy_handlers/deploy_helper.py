from deploy_handlers.docker_helper import DockerHelper
import sys
is_windows = sys.platform.startswith('win')
import os
import Utils.utils as u


def deploy_db():
    dh = DockerHelper()
    db_path = 'environments\\db'
    project_name = 'ASIO_DB'
    dh.run_compose('docker-compose.yml', db_path, project_name)
    dh.run_compose('docker-compose-redis.yml', db_path, project_name)
    dh.run_compose('docker-compose-wikibase.yml', db_path, project_name)


def deploy_front(db_address, back_address):
    dh = DockerHelper()
    project_name = 'ASIO_FRONT'
    db_path = 'environments\\front'
    os.environ.putenv('BACK_HOST', db_address)
    os.environ.putenv('DB_HOST', back_address)
    dh.run_compose('docker-compose.yml', db_path, project_name)
    dh.run_compose('docker-compose-service-discovery.yml', db_path, project_name)
    print("Desplegar Wikibase [S|n]")
    option = u.option_handler("Desplegar Wikibase [S|n]", "Valor no valido, solo son validos los valores [s|n]", None, ['S', 'N'], 0)
    if option == 0:
        dh.run_compose('docker-compose.yml', db_path+'\\wikibase', project_name)


def deploy_portainer():
    dh = DockerHelper()
    db_path = 'environments\\portainer'
    project_name = 'ASIO_PORTAINER'
    if not is_windows:
        print('Desplegando Portainer para Linux')
        dh.run_compose('docker-compose-ce.yml', db_path, project_name)
    else:
        print('Desplegando Portainer para windows')
        dh.run_compose('docker-compose-ce.yml', db_path, project_name)
        #dh.run_docker(['docker run -p 9000:9000 --name portainer --restart always -v \\.\pipe\docker_engine:\\.\pipe\docker_engine -v portainer_data:C:\data portainer/portainer-ce'])


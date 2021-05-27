import subprocess
import os
from datetime import datetime
from pathlib import Path


class NiceLogger:
    def log(self, message):
        date_now = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
        print("{0} |  {1}".format(date_now, message))


class DockerHelper:
    niceLogger = NiceLogger()
    base_dir = ROOT_DIR = Path(__file__).absolute().parent.parent

    def run_compose(self, composer_file, composer_path, project_name):
        self.stop_compose(composer_file, composer_path, project_name)
        os.environ.putenv('COMPOSE_PROJECT_NAME', project_name)
        config_path = os.path.join(self.base_dir, composer_path)
        p = subprocess.Popen(['docker', 'compose', '-f', composer_file, 'up', '-d'], cwd=config_path)
        p.wait()

    def stop_compose(self, composer_file, composer_path, project_name):
        os.environ.putenv('COMPOSE_PROJECT_NAME', project_name)
        config_path = os.path.join(self.base_dir, composer_path)
        p = subprocess.Popen(['docker', 'compose', '-f', composer_file, 'down'], cwd=config_path)
        p.wait()

    def run_docker(self, command):
        print(command)
        p = subprocess.Popen(command)
        p.wait()

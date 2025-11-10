from urllib import request
from project import Project
from pathlib import Path
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        data = tomli.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella

        dependencies = data["tool"]["poetry"]["dependencies"]
        dev_dependencies = data["tool"]["poetry"]["group"]["dev"]["dependencies"]

        return Project(data["tool"]["poetry"]["name"], data["tool"]["poetry"]["description"], ["\n- ".join(dependencies)], ["\n- ".join(dev_dependencies)], ["\n- ".join(data["tool"]["poetry"]["authors"])])

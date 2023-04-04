from inventory_report.importer.importer import Importer
import json

INVALID_FILE = "Arquivo inválido!"


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".json"):
            with open(path, encoding="utf-8") as json_file:
                products_file = json.load(json_file)
                return products_file

    raise ValueError(INVALID_FILE)

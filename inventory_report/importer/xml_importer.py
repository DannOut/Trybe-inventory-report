from inventory_report.importer.importer import Importer

import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        INVALID_FILE = "Arquivo inválido!"
        if path.endswith(".xml"):
            with open(path) as xml_file:
                file = xmltodict.parse(xml_file.read())
                products_file = file["dataset"]["record"]
                return products_file
        raise ValueError(INVALID_FILE)

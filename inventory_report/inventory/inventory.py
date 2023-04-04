from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        product_file = ""
        if path.endswith(".csv"):
            product_file = CsvImporter.import_data(path)

        elif path.endswith(".json"):
            product_file = JsonImporter.import_data(path)

        elif path.endswith(".xml"):
            product_file = XmlImporter.import_data(path)

        return Inventory.generate(report_type, product_file)

    @staticmethod
    def generate(report_type, products_type):
        if report_type == "simples":
            return SimpleReport.generate(products_type)
        elif report_type == "completo":
            return CompleteReport.generate(products_type)

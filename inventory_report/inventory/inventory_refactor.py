from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self.simple_report = SimpleReport
        self.complete_report = CompleteReport
        self.importer = importer
        self.data = []

    def import_data(self, file, type):
        self.data.extend(self.importer.import_data(file))
        if type == "simples":
            return self.simple_report.generate(self.data)
        elif type == "completo":
            return self.complete_report.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)

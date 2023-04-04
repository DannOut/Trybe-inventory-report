from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self.__simple_report = SimpleReport
        self.__complete_report = CompleteReport
        self.importer = importer
        self._data = []

    def import_data(self, file, type):
        self._data.extend(self.importer.import_data(file))
        if type == "simples":
            return self.__simple_report.generate(self._data)
        elif type == "completo":
            return self.__complete_report.generate(self._data)

    def __iter__(self):
        return InventoryIterator(self._data)

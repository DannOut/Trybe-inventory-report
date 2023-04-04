from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self._data = data
        self.__index = 0

    def __next__(self):
        result = self._data[self.__index]

        if not result:
            raise StopIteration()

        self.__index += 1
        return result

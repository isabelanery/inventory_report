from collections.abc import Iterator

class InventoryIterator(Iterator):
    def __init__(self, inventory):
        self.__inventory = inventory
        self.__index = 0

    def __next__(self):
        try:
            result = self.__inventory[self.__index]
        except IndexError as e:
            raise StopIteration() from e

        self.__index += 1
        return result
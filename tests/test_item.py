"""Здесь надо написать тесты с использованием pytest для модуля item."""

class Data:
    def __init__(self):
        self._data = []

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data.append(value)

    @data.deleter
    def data(self):
        self._data.pop()
        print("Value deleted from data list")

d = Data()
d.data = 10
d.data = 20
print(d.data) # Output: [10, 20]
del d.data[-1] # Output: Value deleted from data list
print(d.data) # Output: [10]
from src.item import Item

class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other_instance):
        if not issubclass(self.__class__, other_instance.__class__):
            raise TypeError('Возможно сложить только с экземплярами Phone или Item классов')
        return self.quantity + other_instance.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other_instance) -> int:
        if not issubclass(self.__class__, other_instance.__class__):
            raise TypeError('Возможно сложить только с экземплярами Phone или Item классов')
        return self.quantity + other_instance.quantity
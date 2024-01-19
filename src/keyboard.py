from src.item import Item


class MixinLanguage:
    language = 'EN'

    def __init__(self, language):
        self.language = language

    def change_lang(self):

        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"
        MixinLanguage.language = self.language
        return self

class Keyboard(Item, MixinLanguage):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.language = MixinLanguage.language







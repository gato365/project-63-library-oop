class Product:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def update(self, name):
        self.name = name

    def search(self, name):
        return self.name == name

class Clothing(Product):
    def __init__(self, id, name, size):
        super().__init__(id, name)
        self.size = size

class Electronics(Product):
    def __init__(self, id, name, brand):
        super().__init__(id, name)
        self.brand = brand
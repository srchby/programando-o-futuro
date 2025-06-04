class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Book(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author
        
    def exibir_detalhes(self):
        return f"Livro: {self.name} escrito por {self.author} por R${self.price}"
    
class Eletronic(Product):
    def __init__(self, name, price, maker):
        super().__init__(name, price)
        self.maker = maker
    
    def exibir_detalhes(self):
        return f"Eletrônico: {self.name} do fabricanter {self.maker} por R${self.price}"
    
class Clothing(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand
    
    def exibir_detalhes(self):
        return f"Roupa: {self.name} da marca {self.brand} por R${self.price}"
        
products = [Book("Macbeth", "40", "Shakespeare"), Clothing("Camisa", "50", "Gucci"), Eletronic("Notebook", "2500", "Lenovo")]

for p in products:
    print(p.exibir_detalhes())
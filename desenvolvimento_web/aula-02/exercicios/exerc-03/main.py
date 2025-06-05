class Vehicle:
    def __init__(self, maker, model):
        self.maker = maker
        self.model = model
    
class Luxury(Vehicle):
    def __init__(self, maker, model):
        super().__init__(maker, model)
    
    def mover(self):
        return f"Andou 100 Kms em uma hora"
        
class Suv(Vehicle):
    def __init__(self, maker, model):
        super().__init__(maker, model)
    
    def mover(self):
        return f"Andou 90 Kms em uma hora"
        
class Sport(Vehicle):
    def __init__(self, maker, model):
        super().__init__(maker, model)
    
    def mover(self):
        return f"Andou 120 Kms em uma hora"
    
    
vehicles = [Luxury('Toyota', 'Lexus'), Sport('Dodge', 'Viper'), Suv('Suzuki', 'Vitara')]

for v in vehicles:
    print(f'{v.mover()}')
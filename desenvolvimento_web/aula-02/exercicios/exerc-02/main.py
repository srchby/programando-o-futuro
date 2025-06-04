class staff:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
    
    def print(self):
        return f"Nome: {self.name} \nSalário: {self.salary} \nAge: {self.age}" 
    

class manager(staff):
    def __init__(self, name, salary, age, secretary):
        super().__init__(name, salary, age)
        self.secretary = secretary
        
    def apresentar(self):
        return f"{print()} \nSecretário: {self.secretary}"

class analyst(staff):
    def __init__(self, name, salary, age, area):
        super().__init__(name, salary, age)
        self.area = area

    def apresentar(self):
        return f"{super().print()} \nÁrea {self.area}"

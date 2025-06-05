class Staff:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
    
    def print(self):
        return f"Nome: {self.name} \nSalário: {self.salary} \nAge: {self.age}"

class Manager(Staff):
    def __init__(self, name, salary, age, secretary):
        super().__init__(name, salary, age)
        self.secretary = secretary
        
    def apresentar(self):
        return f"{super().print()} \nSecretário: {self.secretary}\n"

class Analyst(Staff):
    def __init__(self, name, salary, age, area):
        super().__init__(name, salary, age)
        self.area = area

    def apresentar(self):
        return f"{super().print()} \nÁrea {self.area}\n"

workers = [Manager("B","3000","30","C"), Analyst("D","5000","50","E")]

for w in workers:
    print(w.apresentar())

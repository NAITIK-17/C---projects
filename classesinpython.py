class Person:
    name = "Naitik"
    occupation = "Student"
    networth = 500
    def info(self):
        print(f"Name: {self.name}\nOccupation: {self.occupation}")

a = Person()
b = Person()
a.name = "Nakato"
a.occupation = "Software Engineer"
a.info()
b.info()
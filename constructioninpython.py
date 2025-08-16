class Person:
    def __init__(self, n, o):
        print("I am a person")
        self.name = n
        self.occupation = o
    def info(self):
        print(f"Name: {self.name}\nOccupation: {self.occupation}")

a = Person("Naitik", "Student")
b = Person("Nakato", "Gangster")
a.info()
b.info()
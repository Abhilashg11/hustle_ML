class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def meow(self,x):
        return x + 1
    def bark(self):
        print('bark')

    def call_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self,age):
        self.age = age

d = Dog('tim',34)
print(d.get_age())

d1 = Dog("rolly",23)
d1.set_age(43)
print(d1.get_age())


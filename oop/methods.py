class A():
    age = 25
     
    def a(self, a1, a2):
        self.a1 = a1
        self.a2 = a2
        pass
    
    #не потребує об`єкт класа для виклику: A.b()
    @classmethod
    def b(cls, b1): # cls - ссилка на клас
        '''Характеризує поведінку класа'''
        print(cls.age + b1)
        pass
    
    #не потребує об`єкт класа для виклику: A.с()
    @staticmethod
    def c(c1, c2): # нема обовязкових параметрів
        '''сервісна, допоміжна функція. може як звичайна функція вне класу'''
        return(c1+c2)
    
    
    
'''
When do you use the class method?

- Factory methods are those methods that return a
class object (like constructor) for different use cases.
'''

from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person('Adam', 19)
person.display() # Adam's age is: 19

person1 = Person.fromBirthYear('John',  1985)
person1.display() # John's age is: 31

'''
The fromBirthYear method takes Person class (not Person object) 
as the first parameter cls and returns the constructor by calling 
cls(name, date.today().year - birthYear), which is equivalent to 
Person(name, date.today().year - birthYear)
'''
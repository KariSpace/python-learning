# https://github.com/Dobiasd/articles/blob/master/implementation_inheritance_is_bad_-_the_fragile_base_class_problem.md
# проблема крихкого класа


class Person:
    def __init__(self, name):
        self.name = name

    def say(self, text):
        print(f'{self.name}: {text}')

    def greet_casual(self):
        self.say("Hi.")

    def greet_formal(self):
        self.greet_casual()  # changed from  self.say("Hi."). Fix: Person.greet_casual(self) 
        self.say("How are you?")


class VeryPolitePerson(Person):
    def greet_casual(self):
        self.greet_formal()


p = VeryPolitePerson("John")
p.greet_casual()  # RecursionError: maximum recursion depth exceeded

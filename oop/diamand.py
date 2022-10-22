class Doctor():
    def __init__(self, years):
        self.years = years
        
    def __str__(self):
       return('hey, i help people {years} years'.format(years = self.years))


class Progrer():
    def __init__(self, language):
        self.language = language
    
    def __str__(self):
       return('hey, i`m write on {language}'.format(language = self.language))


class Student(Doctor, Progrer):
    def __init__(self, years, language):
        super().__init__(years)  # делегуємо батьківському класу
        Progrer.__init__(self, language)  # делегуємо ще одному батьківському класу
        
    def __str__(self):
        return('hey, i`m write on {language} and cure {years} years'.format(language=self.language, years=self.years))


person1 = Student('1', 'python')

print(person1)

#MRO - method resolution order. Линерализация
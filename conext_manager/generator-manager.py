from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()
    

with open_file('some_file') as f:
    f.write('hola!')


'''
    1. Python встречает ключевое слово yield. Благодаря этому он создает
генератор, а не простую функцию.
    2. Благодаря декоратору, contextmanager вызывается с функцией
open_file в качестве аргумента.
    3. Функция contextmanager возвращает генератор, обёрнутый в объект
GeneratorContextManager.
    4. GeneratorContextManager присваивается функции open_file. Таким
образом, когда мы вызовем функцию open_file в следующий раз, то
фактически обратимся к объекту GeneratorContextManager.
'''
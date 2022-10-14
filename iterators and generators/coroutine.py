'''
генераторы возвращают данные
корутины потребляют данные
'''



def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)
            
            
            
# Iter:
search = grep('coroutine')
next(search) # Вывод: Searching for coroutine
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutines instead!") # Вывод: I love coroutines instead!

search.close() # returt stopiteration after it
'''next() требуется для запуска корутины. 
Так же как и в случае с генераторами, корутины не запускают функцию сразу же. 
Вместо этого они запускают её в ответ на вызов методов __next__() и .send(). 
По этой причине вам требуется вызвать next(), чтобы исполнение дошло до yield.'''
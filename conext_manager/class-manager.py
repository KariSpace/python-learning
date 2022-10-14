'''Необходимый минимум функциональности контекстного менеджера требует методов __enter__ и __exit__. '''


class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()
        
        
with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')
    
    
'''
Метод __exit__ принимает три аргумента. 
Они обязательны для любого метода __exit__ класса контекстного менеджера. 

1. with сохраняет метод __exit__ класса File.
2. Следует вызов метода __enter__ класса File.
3. Метод __enter__ открывает файл и возвращает его.
4. Дескриптор файла передается в opened_file.
5. Мы записываем информацию в файл при помощи .write().
6. with вызывает сохраненный __exit__ метод.
7. Метод __exit__ закрывает файл.
'''


''' 
with при возникновении исключения:

1. Тип, значение и обратная трассировка ошибки передается в метод __exit__.
2. Обработка исключения передается методу __exit__
3. Если __exit__ возвращает True, то исключение было корректно обработано.
4. При возврате любого другого значения with вызывает исключение.
'''
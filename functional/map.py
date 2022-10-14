# map применяет функцию ко всем элементам списка

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)


# map(function_to_apply, list_of_inputs)
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)


funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Вывод:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]



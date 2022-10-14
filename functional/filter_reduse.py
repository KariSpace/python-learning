# filter возвращает список элементов, для которых заданная функция возвращает True

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Вывод: [-5, -4, -3, -2, -1]



# REDUSE -- return only one element

# посчитать произведение всех элементов списка чисел.

product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
# product = 24


from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
# Вывод: 24
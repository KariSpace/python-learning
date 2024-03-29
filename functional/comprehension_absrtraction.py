'''Абстракции - это конструкторы, позволяющие создавать 
последовательности из других последовательностей

абстракции списков
абстракции словарей
абстракции множеств
абстракции генераторов
      ======
list/dict/set comprehension (comprehension - включение) listcomp/dictcomp/setcomp.
'''


'''
Template: 

newlist = [expression for item in iterable if condition == True]

'''


# LISTS ABSTRACTIONS

multiples = [i for i in range(30) if i % 3 == 0] #вместо функции filter
print(multiples)
# Вывод: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]


#example 2:

squared = []
for x in range(10):
    squared.append(x**2)
    
# same to

squared = [x**2 for x in range(10)]




# DICTS ABSTRACTIONS

# поменять местами ключи и значения в словаре
{v: k for k, v in some_dict.items()}


# суммируем значения ключей, которые отличаются только регистром
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}

# mcase_frequency == {'a': 17, 'z': 3, 'b': 34}


# GENERATORS ABSTRACTIONS

'''
Абстракции генераторов похожи на абстракции списков. 
Единственное отличие - генераторы не выделяют память сразу под все элементы, 
а возвращают их один за одним, что намного более экономно:
'''

multiples_gen = (i for i in range(30) if i % 3 == 0)
print(multiples_gen)
# Output: <generator object <genexpr> at 0x7fdaa8e407d8>
for x in multiples_gen:
    print(x)
    # Outputs numbers

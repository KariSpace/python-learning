my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)

# Вывод:
# 1 apple
# 2 banana
# 3 grapes
# 4 pear


my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)

# Вывод: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]
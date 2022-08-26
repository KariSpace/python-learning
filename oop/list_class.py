# Make list index start with 1
class NewList (list) :  # Наслідуємо клас list
    def __getitem__(self, index): # поліморфізм __getitem__ 
        if index > 0:
            return super().__getitem__(index-1)
        elif index == 0:
            raise IndexError('List index out of rande')
        return super().__getitem__(index)

n_list = NewList([1, 2, 3, 4])

a = [1, 2, 3, 4] 
print(n_list[1])
print(n_list[-1])

try:
     print(n_list[0])
except IndexError as e:
    print(e)

try:
     print(n_list[111])
except IndexError as e:
    print(e)


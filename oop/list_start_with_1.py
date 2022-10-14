# Make list index start with 1
class NewList (list) :  # Наслідуємо клас list
    def __getitem__(self, index): # поліморфізм __getitem__ 
        if index > 0:
            return super().__getitem__(index-1)
        elif index == 0:
            raise IndexError('List index out of rande')
        return super().__getitem__(index)

n_list = NewList([1, 2, 3, 4])

a = [1, 2, 3, 4]*2

print(a)
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


'''

why lists start with 0: 
- https://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html
- https://en.wikipedia.org/wiki/Zero-based_numbering#cite_note-dijkstra-8

- In C, the name of an array is essentially a pointer, a reference to a memory location, 
and so the expression array[n] refers to a memory location n-elements away from the starting element. 
This means that the index is used as an offset. The first element of the array is exactly contained in the memory 
location that array refers (0 elements away), so it should be denoted as array[0]. 

Most programming languages have been designed this way, so indexing from 0 is pretty much inherent to the 
language as most of the languages (not all) follow C standards. 
You can refer this link for more details.

- https://stackoverflow.com/questions/41530124/why-does-an-array-index-or-base-index-start-with-0

'''
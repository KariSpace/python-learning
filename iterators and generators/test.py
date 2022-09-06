# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}

list1 = [1,2,2,2,2,2,3,3,3,3,5]
fSet = set(person)

fs = set(list1)

print(fSet)
print(fs)

# Frozensets
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozenset
C = A.copy()  # Output: frozenset({1, 2, 3, 4})
print("copy", C)
print(id(C))
# union
C = A.union(B)  # Output: frozenset({1, 2, 3, 4, 5, 6})
print("union", C)
print(id(C))
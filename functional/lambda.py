'''
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.


lambda argument: manipulate(argument)
'''

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) # 22
print(mytripler(11)) # 33




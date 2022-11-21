def huy(diametr, length = 30):
    print('wow, you have {l} cm and {d} mm huy'.format(l = length, d = diametr))
    
  
my_huy = huy(diametr = 5, length = 25)


def foo(*args, **kwargs):
    for value in args:
        print(value)
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


foo([1, 2, 3, 4],  {'a':1, 'd':2, 'c':5} )
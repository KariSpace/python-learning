
cash = {}
def foo_cash(func):
    def inner(x):
        global cash
        
        if x in cash:
           print(cash[x])
        else:
            print('foo_cash 1')
            res = func(x)
            print(res)
            cash[x] = res
            print('foo_cash 2')
            
    return inner

@foo_cash
def foo(x: int) -> int:
    print('foo')
    return x*x + 1

foo(3)
foo(3)
foo(2)
print(cash)
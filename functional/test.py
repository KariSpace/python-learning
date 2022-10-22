
from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    # your code here
    print(''.join(elements).replace('1', ''))
    return  len(str(elements).replace(str(elements[0]), ''))>0


print("Example:")
print(all_the_same([1, 1, 1]))
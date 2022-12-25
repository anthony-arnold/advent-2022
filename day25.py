import sys 
from itertools import zip_longest
from functools import reduce

def val(c):
    if c == '=':
        return -2
    elif c == '-':
        return -1
    else:
        return 0 if c is None else int(c)
    
def add(a, b):
    s = ''
    carry = 0
    for u, v in zip_longest(reversed(a), reversed(b)):
        w = val(u) + val(v) + carry
        carry = 0
        
        if w == -1:
            s += '-'
        elif w == -2:
            s += '='
        elif 0 <= w <= 2:
            s += str(w)
        elif w > 2:
            carry = 1 
            s += "0-="[5 - w]
            
        elif w < -2:
            carry = -1
           
            s += str(w + 5)
           

        assert(-5 <= w <= 5)
    if carry:
        s += '1'

    return ''.join(reversed(s)) 

if __name__ == '__main__':    
    print(reduce(add, (l.strip() for l in sys.stdin), '0'))

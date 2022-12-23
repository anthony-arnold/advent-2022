import sys
import re 

expr = re.compile(r'(\w+): (\S+)( ([+\-*/]) (\S+))?')

ops = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b 
}


def monkey(s):
    m = expr.match(s)
    try:
        return (m[1], int(m[2]))
    except:
        return (m[1], (m[2], m[4], m[5]))
    
def yell(m, M):
    v = M[m]
    try:
        a = yell(v[0], M)
        b = yell(v[2], M)
        v = ops[v[1]](a, b)
    finally:
        return v
    

def expand(m, M):
    if m  == 'humn':
        return 'x'

    v = M[m]
    try:
        a = expand(v[0], M)
        b = expand(v[2], M)
        v = (a, v[1], b)
    finally:
        return v
        
     
def reduce(expr):
    if isinstance(expr, tuple):
        a, op, b = expr
        a = reduce(a)
        b = reduce(b)
        
        if not any(x == 'x' or isinstance(x, tuple) for x in [a, b]):
            expr = ops[op](a, b)
        elif expr != (a, op, b):
            expr = reduce((a, op, b))
            
    return expr 

def solve(left, right):
    if isinstance(right, tuple):
        t = left 
        left = right 
        right = t
        
    while isinstance(left, tuple):
        a, op, b = left 
        if op == '*':
            if a == 'x' or isinstance(a, tuple):
                right /= b 
                left = a 
            else:
                right /= a
                left = b 
                
        elif op == '+':
            if a == 'x' or isinstance(a, tuple):
                right -= b 
                left = a 
            else:
                right -= a
                left = b 
            
        elif op == '-':
            if a == 'x' or isinstance(a, tuple):
                right += b 
                left = a 
            else:
                left = reduce((right, '+', b))
                right = a 
                
        else:
            if a == 'x' or isinstance(a, tuple):
                right *= b 
                left = a 
            else:
                left = reduce((right, '*', b))
                right = a 
    return int(right)
            

if __name__ == '__main__':
    M = dict(map(monkey, sys.stdin))
    print(yell('root', M))
        
    left = expand(M['root'][0], M)
    right = expand(M['root'][2], M)
    
    left = reduce(left)
    right = reduce(right)
    print(solve(left, right))

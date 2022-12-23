import sys
from itertools import count

def mix(N, times=1, f=1):
    a = list(N)
    h = len(N) - 1
    
    for _ in range(times):
        for n, c in N:
            if not n:
                continue 
                
            i = a.index((n, c))
            j = ((n % h) * (f % h)) % h
            
            a = a[i+1:] + a[:i]
            a[j:j] = [(n, c)] 
            
    z = a.index((0, -1))
    a = a[z:] + a[:z]
    return sum(a[(i * 1000) % len(N)][0] for i in range(1, 4))*f


if __name__ == '__main__':
    c = count()
    N = list(map(int, sys.stdin))
    NC = [(n, -1 if n == 0 else next(c)) for n in N]
    key = 811589153
    print(mix(NC))
    print(mix(NC, 10, key))
   

import sys
from itertools import chain

def adjacent(cell):
    for dx in [-1, 1]:
        for x in range(3):
            yield tuple(x+d for x, d in zip(cell, [0]*x + [dx] + [0]*(2-x)))


if __name__ == '__main__':
    lava = set(
        tuple(int(i) for i in s.split(','))
        for s in sys.stdin
    )
    
    surfaces = list(chain.from_iterable(adjacent(cell) for cell in lava)) 
    air = set(surfaces) - lava 
    
    print(sum(ex in air for ex in surfaces))
    
    minx = tuple(min(x[i] for x in lava) for i in range(3))
    maxx = tuple(max(x[i] for x in lava) for i in range(3))
    
    # FINE!
    outside = set()
    bubbles = set()
    for pocket in air:
        if pocket in outside:
            continue
    
        bubble = set()
        queue = [pocket]
        
        while queue:
            cell = queue.pop(0)
            if cell in bubble:
                continue
                
            if cell in outside or any(x<mn or x>mx for x,mn,mx in zip(cell, minx, maxx)):
                outside |= bubble 
                bubble = set()
                break 
                
            if cell not in lava:
                bubble.add(cell)
                
                for neighbour in adjacent(cell):
                    queue.append(neighbour)
                
                
        bubbles |= bubble 
        
    air -= bubbles
            
    
    print(sum(ex in air for ex in surfaces))
    

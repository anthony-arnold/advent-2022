import sys 
from heapq import heappush, heappop
from itertools import count

movable = [(-1, 0), (0, -1), (0, 0), (1, 0), (0, 1)]

def isfree(x, b, d, w, c, l, r):
    dx = d % (w - 2)
    if c == l:
        n = b - dx 
        if n <= 0:
            n += w - 2
    elif c == r:
        n = b + dx 
        if n >= w-1:
            n -= w - 2
    else:
        return True 
         
    return x != n
    

def canmove(x, y, w, h, d, bliz):
    if x < 0 or x > w - 1:
        return False
    if y < 0 or y > h - 1:
        return False
    if bliz[y][x] == '#':
        return False
        
    for by in range(h):
        c = bliz[by][x]
        if not isfree(y, by, d, h, c, '^', 'v'):
            return False       
        
    for bx in range(w):
        c = bliz[y][bx]
        if not isfree(x, bx, d, w, c, '<', '>'):
            return False
        
    return True 


def find_path(bliz, width, height, goals):
    i = count()
    state = (1, 0, (0, 0), goals)
    e = [0, next(i), state]
    distances = {state: 0}
    track = {
        state: e
    }
    rem = '<DEL>'
    q = [e]
    
    while q:
        d, c, state = heappop(q)
            
        if state is rem:
            continue 
        del track[state]
        
        x, y, _, goals = state 
        
        if x == goals[0][0] and y == goals[0][1]:
            goals = goals[1:]
            if len(goals) < 1:
                return d
        
        new = d + 1
        valid = list(filter(lambda dd: canmove(x + dd[0], y + dd[1], width, height, new, bliz), movable))
        
        for dx, dy in valid:
            nx, ny = x+dx, y+dy
            state = (nx, ny, (new % (width - 2), new % (height - 2)), goals)
            old = distances.get(state, 1e6)
            new = d + 1
            if new < old:
                e = [new, next(i), state]
                distances.update({ state: new })
                if state in track:
                    track[state][-1] = rem 
                track[state] = e 
                heappush(q, e)
                


if __name__ == '__main__':    
    bliz = [
        line.strip() for line in sys.stdin
    ]
    height = len(bliz)
    width = len(bliz[0])
    
    print(find_path(bliz, width, height, ((width - 2, height - 1),)))

    print(find_path(bliz, width, height, (
        (width - 2, height - 1),
        (1, 0),
        (width - 2, height - 1)
    )))

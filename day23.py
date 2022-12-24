import sys 
from itertools import product

def canmove(elf, elves):
    x, y = elf
    for dx, dy in product([-1, 0, 1], repeat=2):
        if (dx,dy) == (0, 0):
            continue
        
        if (x+dx, y+dy) in elves:
            return True 
            
    return False
    

if __name__ == '__main__':
    elves = set()
    
    for y, line in enumerate(sys.stdin):
        for x, c in enumerate(line):
            if c == '#':
                elves.add((x, y))
                
    consider = [
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0)
    ]
    
    round = 0
    while True:
        round += 1
        proposals = {}
        for x, y in elves:
            if not canmove((x, y), elves):
                proposals[(x,y)] = set([(x, y)])
                continue
        
            moved = False
            for dd in consider:
                im = dd.index(0) 
                
                free = 0
                for z in [-1, 0, 1]:
                    dl = list(dd)
                    dl[im] = z 
                    p = (x + dl[0], y + dl[1])
                    if p in elves:
                        break
                    free += 1
                    
                if free == 3:
                    dest = (x + dd[0], y + dd[1])
                    if dest not in proposals:
                        proposals[dest] = set()
                    proposals[dest].add((x, y))
                    moved = True 
                    break
            if not moved:
                proposals[(x,y)] = set([(x, y)])
                    
        nelves = set()
        for (nx, ny), candidates in proposals.items():
            for x, y in candidates:
                if len(candidates) > 1:
                    nelves.add((x, y))
                else:
                    nelves.add((nx, ny))
            
        if nelves == elves:
            break
            
        elves = nelves    
        consider = consider[1:] + consider[:1]
        
        if round == 10:
            minx = 1e6
            miny = 1e6
            maxx = -1e6
            maxy = -1e6
            for (x, y) in elves:
                minx = min(minx, x)
                miny = min(miny, y)
                maxx = max(maxx, x)
                maxy = max(maxy, y)
                
            area = (maxx - minx + 1) * (maxy - miny + 1)
            free = area - len(elves)
            
            print(free)
        
    print(round)
    

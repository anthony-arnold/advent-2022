import sys 

quadrants = {
    (1, 0): {
        (-1, 0): ((0, 2), (1, 0)),
        (0, -1): ((0, 3), (1, 0))
    },
    (2, 0): {
        (1, 0): ((1, 2), (-1, 0)),
        (0, -1): ((0, 3), (0, -1)),
        (0, 1): ((1, 1), (-1, 0))
    },
    (1, 1): {
        (1, 0): ((2, 0), (0, -1)),
        (-1, 0): ((0, 2), (0, 1))
    },
    (0, 2): {
        (0, -1): ((1, 1), (1, 0)),
        (-1, 0): ((1, 0), (1, 0))
    }, 
    (1, 2): {
        (1, 0): ((2, 0), (-1, 0)),
        (0, 1): ((0, 3), (-1, 0))
    },
    (0, 3): {
        (1, 0): ((1, 2), (0, -1)),
        (0, 1): ((2, 0), (0, 1)),
        (-1, 0): ((1, 0), (0, 1))
    }
}

def quadrant(xt):
    return quadrants[tuple(x//50 for x in xt)]
    

def wrap3d(dx, xt, chart):
    q = quadrant(xt)    
    nq, nd = q[dx]
    
    if dx.index(0) == nd.index(0):
        # same axis
        r = any(a!=b for a,b in zip(dx, nd)) # changed direction
    else:
        r = all(a==b for a,b in zip(dx, reversed(nd))) # maintained direction
        
    m = (xt[0] if dx[1] else xt[1])  % 50 
    if r:
        m = 49 - m
    if nd[0] == 1:
        nx = (nq[0] * 50, nq[1] * 50 + m)
    elif nd[0] == -1:
        nx = (nq[0] * 50 + 49, nq[1] * 50 + m)
    elif nd[1] == 1:
        nx = (nq[0] * 50 + m, nq[1] * 50)
    else: 
        nx = (nq[0] * 50 + m, nq[1] * 50 + 49)
        
    return nx, nd 
    

def wrap2d(dx, xt, chart):
    if dx[0] == -1:
        xt = (len(chart[xt[1]]) - 1, xt[1])
    elif dx[0] == 1:
        xt = (0, xt[1])
    elif dx[1] == -1:
        xt = (xt[0], len(chart) - 1)
    else:
        xt = (xt[0], 0)

    space = chart[xt[1]][xt[0]]
    while space == ' ':
        xt = tuple(x + d for x, d in zip(xt, dx))
        space = chart[xt[1]][xt[0]]
    return xt, dx 
    
    
def code(pos, dx):
    return (pos[1]+1) * 1000 + (pos[0]+1) * 4 + [(1, 0), (0, 1), (-1, 0), (0, -1)].index(dx)


def walk(pos, moves, chart, wrap):
    dx = (1, 0)
    for move, turn in moves:
        for _ in range(move):
            xt = tuple(x+d for x, d in zip(pos, dx))
            td = dx 
            
            if any(x < 0 for x in xt):
                space = ' '
            else:
                try:
                    space = chart[xt[1]][xt[0]]
                except IndexError:
                    space = ' '
                
            if space == ' ':
                # wrap around 
                xt, td = wrap(dx, pos, chart)
                space = chart[xt[1]][xt[0]]
                
            if space == '#':
                break 
                
            pos = xt
            dx = td
            
        if turn == 'L':
            dx = (dx[1], dx[0]*-1)
        elif turn == 'R':
            dx = (dx[1]*-1, dx[0])

    return pos, dx 


if __name__ == '__main__':
    lines = [l[:-1] for l in sys.stdin]
    chart = lines[:-2]
    w = max(len(l) for l in chart)
    
    for i in range(len(chart)):
        chart[i] = chart[i] + ' ' * (w - len(chart[i]))
    
    instr = lines[-1]
    moves = []
    move = 0
    while instr:
        if instr[0].isdigit():
            move = move*10 + int(instr[0])
        else:
            moves.append((move, instr[0]))
            move = 0 
        instr = instr[1:]
    moves.append((move, None))
    
    
    for i, x in enumerate(lines[0]):
        if x == '.':
            orig = (i, 0)
            break
            
    pos, dx = walk(orig, moves, chart, wrap2d)
    print(code(pos, dx))
    
    pos, dx = walk(orig, moves, chart, wrap3d)
    print(code(pos, dx))
    

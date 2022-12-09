import sys

dpos = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, 1),
    'D': (0, -1) 
}

def sim(moves, l):
    pos = [(0, 0) for _ in range(l)]
    v = {pos[-1]}

    for h, d in moves:
        for _ in range(int(d)):
            dX = dpos[h]
            for i in range(l):
                pos[i] = (pos[i][0] + dX[0], pos[i][1] + dX[1])
                if i + 1 == l:
                    break

                dP = (pos[i][0] - pos[i+1][0], pos[i][1] - pos[i+1][1])
                if all(abs(x) < 2 for x in dP):
                    break
                
                dX = tuple(0 if x == 0 else x/abs(x) for x in dP)
            v |= {pos[-1]}

    return len(v)

if __name__ == '__main__':
    moves = [l.split() for l in sys.stdin]
    print(sim(moves, 2))
    print(sim(moves, 10))



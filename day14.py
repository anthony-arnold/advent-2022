import sys


if __name__ == '__main__':
    obstacles = set()

    maxy = 0
    for line in sys.stdin:
        paths = line.split(' -> ')
        moves = [[int(i) for i in path.split(',')] for path in paths]

        x0, y0 = moves[0]

        for x, y in moves[1:]:
            if x == x0:
                d = (y - y0)//abs(y - y0)
                for j in range(y0, y + d, d):
                    obstacles.add((x, j))
                    maxy = max(maxy, j)
            else:
                d = (x - x0)//abs(x - x0)
                for j in range(x0, x + d, d):
                    obstacles.add((j, y))
            x0 = x
            y0 = y


    rest = 0
    blocked = False
    lost = False
    while (500, 0) not in obstacles:
        x, y = 500, 0
        stopped = False
        while not stopped:
            stopped = True
            if y + 1 < maxy + 2:
                for x1 in [x, x-1, x+1]:
                    if (x1, y+1) not in obstacles:
                        x = x1
                        y += 1
                        stopped = False
                        
                        if y > maxy and not lost:
                            lost = True
                            print(rest)
                        break

            if stopped:
                obstacles.add((x, y))
                rest += 1
                break
    print(rest)


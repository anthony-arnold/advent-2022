import sys
import itertools
import heapq


def path(grid, start, end):

    distance = {
        start: 0
    }
    counter = itertools.count()
    removed = '<DEL>'
    queue = [[0, next(counter), start]]
    finder = {
        start: queue[0]
    }

    while queue:
        _, _, p =  heapq.heappop(queue)
        if p is removed:
            continue
        if p == end:
            break
        del finder[p]
        dp = distance[p]

        qs = [
            (p[0] - 1, p[1]),
            (p[0] + 1, p[1]),
            (p[0], p[1] - 1),
            (p[0], p[1] + 1)
        ]

        for q in qs:
            if q in distance and q not in finder:
                continue
            if any(c < 0 for c in q):
                continue

            try:
                d = ord(grid[q[1]][q[0]]) - ord(grid[p[1]][p[0]])
            except IndexError:
                continue

            if d > 1:
                continue
            d = 1
            
            old = distance.get(q, 1e20)
            new = dp + d
            if new < old:
                distance[q] = new
                if q in finder:
                    e = finder.pop(q)
                    e[2] = removed
                e = [new, next(counter), q]
                finder[q] = e
                heapq.heappush(queue, e)

    try:
        return distance[end]
    except KeyError:
        return 1e20

if __name__ == "__main__":
    grid = []
    y = 0
    As = []
    for line in sys.stdin:
        grid.append(list(line.strip()))
        for x, c in enumerate(grid[-1]):
            if c == 'S':
                start = (x, y)
                grid[y][x] = 'a'
            elif c == 'a':
                As += [(x, y)]
            elif c == 'E':
                end = (x, y)
                grid[y][x] = 'z'
        y += 1

    p1 = path(grid, start, end)
    p2 = p1
    for a in As:
        p = path(grid, a, end)
        if p < p2:
            p2 = p

    print(p1)
    print(p2)

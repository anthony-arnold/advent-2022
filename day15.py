import sys
import re
from enum import Enum

LIMIT = 4000000
def contains(x, y, zone):
    (zx, zy), zd = zone
    dx = abs(x - zx)
    dy = abs(y - zy)
    return (dx + dy) <= zd


if __name__ == '__main__':
    row = 2000000
    omit = set()
    zones = set()

    for line in sys.stdin:
        m = re.match(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
        s = (int(m[1]), int(m[2]))
        b = (int(m[3]), int(m[4]))

        d = abs(s[0]-b[0]) + abs(s[1]-b[1])
        zones.add((s, d))

        if row in range(s[1]-d, s[1]+d+1):
            dy = abs(row - s[1])
            dx = d - dy
            omit.add((s[0]-dx, s[0]+dx))


    ranges = list(sorted(omit))
    ans = 0
    x = ranges[0][0]
    for r in ranges:
        x = max(r[0], x)
        if r[1] > x:
            ans += r[1] - x 
            x = r[1] 
    print(ans)

    ans = None
    for ((zx, zy), zd) in zones:
        for x in range(max(0, zx-zd), min(LIMIT, zx+zd + 1)):
            v = zd - abs(x - zx) + 1
            y = zy + v
            if y >= 0 and y <= LIMIT and not any(contains(x, y, z) for z in zones):
                ans = x * LIMIT + y
                break
            
            y = zy - v
            if y >= 0 and y <= LIMIT and not any(contains(x, y, z) for z in zones):
                ans = x * LIMIT + y
                break
                
        if ans:
            break
    print(ans)

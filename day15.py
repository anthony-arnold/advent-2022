import sys
import re

if __name__ == '__main__':
    row = 2000000
    omit = set()

    for line in sys.stdin:
        m = re.match(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
        s = (int(m[1]), int(m[2]))
        b = (int(m[3]), int(m[4]))

        d = abs(s[0]-b[0]) + abs(s[1]-b[1])

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

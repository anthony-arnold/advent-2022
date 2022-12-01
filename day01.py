import sys

if __name__ == '__main__':
    s = 0
    m = []
    for line in sys.stdin:
        if len(line.strip()) > 0:
            s += int(line)
        else:
            m += [s]
            s = 0
    m += [s]
    x = list(reversed(sorted(m)))
    print(sum(x[0:3]))

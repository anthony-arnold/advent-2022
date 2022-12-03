import sys
import itertools

def priority(item):
    if item >= 'a' and item <= 'z':
        return ord(item) - (ord('a')) + 1
    return (ord(item) - ord('A')) + 27

def invalid(line):
    split = len(line) // 2
    c1, c2 = set(line[:split]), set(line[split:])
    return next(itertools.islice(c1 & c2, 1))


if __name__ == "__main__":
    lines = list(sys.stdin)
    print(sum(priority(invalid(l.strip()))for l in lines))
    
    p = 0
    for i in range(0, len(lines), 3):
        s = set(lines[i].strip())
        for j in range(1, 3):
            s &= set(lines[i+j].strip())
        p += priority(next(itertools.islice(s, 1)))
    print(p)

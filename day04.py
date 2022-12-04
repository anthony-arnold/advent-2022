import sys

def rng(s):
    l, r = s.split('-')
    return set(range(int(l), int(r) + 1))

def assig(line):
    left, right = line.split(',')
    return rng(left), rng(right)

def contains(l, r):
    u = l & r
    return u == l or u == r

def overlap(l, r):
    return len(l & r) > 0

if __name__ == "__main__":
    assignments = [assig(l) for l in sys.stdin]
    
    print(sum(contains(*a) for a in assignments))
    print(sum(overlap(*a) for a in assignments))


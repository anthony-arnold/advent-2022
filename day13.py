import sys
from itertools import chain
from functools import cmp_to_key


def parse(line):
    try:
        return int(line), len(line)
    except:
        pass

    line = line[1:]
    if line.startswith(']'):
        return [], 2

    r = 1
    i = 0
    elems = []
    while line and not line.startswith(']'):
        if line.startswith('['):
            i, e = parse(line)
            line = line[e:]
            r += e 
            continue

        elif line.startswith(','):
            elems.append(i)
            i = 0

        else:
            i = i * 10 + int(line[0])

        line = line[1:]
        r += 1

    elems.append(i)
    return elems, r+1

def aslist(e):
    if isinstance(e, list):
        return e
    return [e]


def compare(left, right):
    if isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            r = compare(left[i], right[i]) 
            if r == 0:
                continue
            return r
        
        left = len(left)
        right = len(right)

    elif isinstance(left, list):
        return compare(left, [right])
    elif isinstance(right, list):
        return compare([left], right)

    if left == right:
        return 0
    return -1 if left < right else 1
    

if __name__ == "__main__":
    pairs = []
    pair = []
    for line in sys.stdin:
        if line.strip():
            pair.append(parse(line.strip())[0])
        else:
            pairs.append(pair)
            pair = []
    pairs.append(pair)

    x = 0
    for i, [left, right] in enumerate(pairs):
        if compare(left, right) < 0:
            x += i + 1
    print(x)

    codes = list(chain.from_iterable(pairs))
    codes += [[[2]], [[6]]]

    order = sorted(codes, key=cmp_to_key(compare))
    for i,packet in enumerate(order):
        if packet == [[2]]:
            y = i + 1
        elif packet == [[6]]:
            z = i + 1

    print(y * z)

    


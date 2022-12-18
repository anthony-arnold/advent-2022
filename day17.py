import sys
import itertools
import pprint
import re

regex = re.compile(r'(.+ .+)( \1)+')

shapes = [
    [0b0011110],
    [0b0001000, 0b0011100, 0b0001000],
    [0b0011100, 0b0000100, 0b0000100],
    [0b0010000, 0b0010000, 0b0010000, 0b0010000],
    [0b0011000, 0b0011000]
]

def stacksize(goal, jets, search=False):
    j = itertools.count()

    buff = [0]
    memo = []
    find = {}

    for i in range(goal):
        old = len(buff)

        bottom = len(buff) + 3
        shape = shapes[i % 5]

        while bottom > 0:
            jet = jets[next(j) % len(jets)]
            test = shape

            if jet == '<':
                if not any(0b1000000 & row for row in shape):
                    test = [row << 1 for row in shape]
            if jet == '>':
                if not any(0b0000001 & row for row in shape):
                    test = [row >> 1 for row in shape]

            if test is not shape:
                if all(
                    bottom + k >= len(buff) or
                    (row & buff[bottom + k]) == 0
                    for k,row in enumerate(test)
                ):
                    shape = test

            if any(
                bottom + k - 1 < len(buff) and
                (row & buff[bottom + k - 1]) != 0
                for k,row in enumerate(shape)
            ):
                break

            bottom -= 1
        
        for k, row in enumerate(shape):
            if k + bottom < len(buff):
                buff[k + bottom] |= row
            else:
                buff.append(row)

            
            
        if search:
            memo.append(len(buff))
            for k in range(1000, len(buff) // 2):
                if buff[-k:] == buff[-k*2:-k]:
                    find[len(buff) + k] = (k, i)
                    break
                        
            if len(buff) in find:
                cycle, c = find[len(buff)]
                pre = memo[2*c - i] - cycle 
                target = goal - (2*c - i) 
                if target % (i - c) == 0:
                    return cycle * (1 + (target // (i - c))) - 1 + pre
                        
            
                        
                    
        
    return len(buff)

if __name__ == '__main__':
    jets = sys.stdin.readline().strip()
    print(stacksize(2022, jets))
    print(stacksize(1000000000000, jets, True))
    

import sys

def visible(array, index):
    return all(a < array[index] for a in array[:index]) or \
           all(a < array[index] for a in array[index+1:]) 


def score(array, index, direction):
    b = array[index]

    left = 0
    idx = index + direction
    while idx >= 0 and idx < len(array):
        a = array[idx]
        left += 1
        if a >= b:
            break
        idx += direction
        
    return left

def fscore(array, index):
    return score(array, index, -1) * score(array, index, 1)

if __name__ == '__main__':
    rows = []
    for line in sys.stdin:
        rows.append([
            int(c) for c in line if c.isnumeric()
        ])

    v = 0
    for i,row in enumerate(rows):
        for j,col in enumerate(row):
            if visible(row, j):
                v += 1
            elif visible([r[j] for r in rows], i):
                v += 1
    print(v)

    s = 0
    for i,row in enumerate(rows):
        for j,col in enumerate(row):
            s = max(s, fscore(row, j) * fscore([r[j] for r in rows], i))
    print(s)

    

import sys

if __name__ == '__main__':
    line = sys.stdin.read()
    sop = -1
    som = -1
    for i in range(4, len(line)):
        bytes = set(line[i-4:i])

        if sop < 0 and len(bytes) == 4:
            sop = i

        if i >= 14:
            bytes = set(line[i - 14:i])
            if som < 0 and len(bytes) == 14:
                som = i

    print(sop)
    print(som)

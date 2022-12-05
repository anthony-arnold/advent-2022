import sys


if __name__ == "__main__":
    stacks = {}

    for line in sys.stdin:
        if not line.strip():
            break

        x = 1
        while len(line) >= 3:
            code = line[:3]
            line = line[4:]
            if code.startswith('['):
                code = code[1]
                if x not in stacks:
                    stacks[x] = []
                stacks[x].append(code)
            x += 1


    instructions = []
    for line in sys.stdin:
        _, n, _, src, _, dst = line.split()
        instructions.append((int(n), int(src), int(dst)))

    part1 = {
        i: lst.copy()
        for i, lst in stacks.items()
    }
    for n, src, dst in instructions:
        for i in range(n):
            x = part1[src].pop(0)
            part1[dst].insert(0, x)
    print(''.join([s[1][0] for s in sorted(part1.items())]))

    for n, src, dst in instructions:
        for i in range(n):
            x = stacks[src].pop(0)
            stacks[dst].insert(i, x)

    print(''.join([s[1][0] for s in sorted(stacks.items())]))

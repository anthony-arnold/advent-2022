import sys


if __name__ == "__main__":
    prog = [(line.split() + ['0'])[:2] for line in sys.stdin]
    x = 1
    c = 0
    s = 0
    screen =  ''

    for instr, v in prog:
        for _ in range(1 if instr == 'noop' else 2):
            h = c % 40
            if x - 1 <= h <= x + 1:
                screen += '#'
            else:
                screen += '.'

            c += 1
            if (c - 20) % 40 == 0:
                s += c * x
            if c % 40 == 0:
                screen += '\n'

        x += int(v)
    print(s)
    print(screen)

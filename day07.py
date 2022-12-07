import sys


if __name__ == '__main__':
    d = ['']  
    totals = {}

    for line in sys.stdin:
        if line.startswith('$'):
            cmd = line[2:]
            if cmd.startswith('cd'):
                e = cmd[2:].strip()
                if e.startswith('/'):
                    d = ['']
                elif e == '..':
                    d.pop()
                else:
                    d.append(e)
        else:
            # This will actually fail if 'ls' is called on the same directory twice
            # but that didn't happen for my input.
            x = d.copy()
            while len(x):
                f = '/'.join(x)
                i = line.split()[0].strip()

                if i != 'dir':
                    s = int(i)
                    totals[f] = totals.get(f, 0) + s
                x.pop()
    
    print(sum(v for v in totals.values() if v <= 100000))

    avail = 70000000 - totals['']
    reqd = 30000000 - avail

    print(min(v for v in totals.values() if v > reqd))



import sys
import re
import heapq
import itertools

def path(adj, src, dst):
    c = itertools.count()
    pre = {}
    v = set()
    rm = '<del>'
    e = [0, next(c), src]
    lookup = {src: e}
    dist = {src: 0}
    q = [e]

    while q:
        d, _, valve = heapq.heappop(q)
        if valve is rm:
            continue
        del lookup[valve]
        if valve in v:
            continue
        v.add(valve)

        if valve == dst:
            break

        for goto in adj[valve]:
            old = dist.get(goto, 1e10)
            new = d + 1
            if new < old:
                dist[goto] = new
                pre[goto] = valve
                if goto in lookup:
                    lookup[goto][-1] = rm
                e = [new, next(c), goto]
                lookup[goto] = e
                heapq.heappush(q, e)

    path = []
    valve = dst
    while valve:
        path.insert(0, valve)
        valve = pre.get(valve)
    return path

def all_paths(adj, valves):
    paths = {}
    for src in valves:
        for dst in valves:
            if src == dst:
                continue

            paths[(src,dst)] = len(path(adj, src, dst))
    return paths


def dfs(pressure, paths, visited=set(), time=30, valve='AA'):
    m = 0
    n = time * pressure[valve]

    for v, d in paths[valve]:
        if v in visited:
            continue
        if time - d <= 0:
            continue
        
        x = dfs(pressure, paths, visited | {v}, time - d, v)
        if x > m:
            m = x
    return n + m

if __name__ == '__main__':
    pressure = {}
    adj = {}

    for line in sys.stdin:
        m = re.match(r'Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? (([A-Z]+, )*)([A-Z]+)', line)
        
        valve = m[1]
        rate = int(m[2])
        pressure[valve] = rate

        adj[valve] = [v.strip() for v in m[3].split(',') if v.strip()] + [m[5]]
        
    working = list(k for k,v in pressure.items() if v > 0)
    paths = all_paths(adj, working + ['AA'])
    
    lookup = {}
    for (src, dst), d in paths.items():
        if src not in lookup:
            lookup[src] = []
        lookup[src] += [(dst, d)]

    print(dfs(pressure, lookup))
    

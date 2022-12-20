import sys
import re
from itertools import count
from collections import namedtuple
from heapq import heappush, heappop
from multiprocessing import Pool
from functools import reduce

names = ['geode', 'obsidian', 'clay', 'ore']

Robots = namedtuple('Robots', names)
Materials = namedtuple('Materials', names)
State = namedtuple('State', ['robots', 'materials'])

def build_robot(state, robot, instructions):
    robots = list(state.robots)
    robots[robot] += 1
    robots = Robots(*robots)
    
    materials = list(state.materials)
    for name, n in enumerate(instructions[robot]):
        materials[name] -= n 
    materials = Materials(*materials)
    
    return State(robots, materials)


def harvest(state):
    return Materials(*[state.materials[i]+state.robots[i] for i in range(len(names))])


def fastest_geode(instructions, state, time, limit):
    # Surely a lot in this function isn't needed but I'm too afraid to remove anything
    
    index = count(0)
    deleted = '<DEL>'
    
    e = [time, next(index), state, frozenset()]
    distance = { state: time }
    active = { state: e }
    queue = [e]
    visited = set()
    pre = {}
    
    m = 0
    
    stop = limit
    while queue:
        weight, _, state, ignore = heappop(queue)
        if state is deleted:
            continue
            
        del active[state]
            
        if state in visited:
            continue
            
        visited.add(state)
        
        if weight >= stop:
            # too far 
            m = max(m, state.materials.geode)
            break
        
        # What is possible to build 
        build = [
            i for i in range(len(names))
            if i not in ignore and 
                all(state.materials[mat] >= req for mat, req in enumerate(instructions[i])) and (i == 0 or 
                any(instructions[type][i] > state.robots[i] for type in range(len(names))))
        ]
        
        harvested = State(state.robots, harvest(state))
        if 0 in build:            
            f = build_robot(harvested, 0, instructions)
            
            m = max(fastest_geode(instructions, f, weight + 1, limit), m)
            continue
        
        if weight + 1 == limit:
            m = max(m, harvested.materials.geode)
            break
        
        if weight == stop:
             # All future states are too late
            continue
        
        future = [(build_robot(harvested, i, instructions), frozenset()) for i in build]
        
        future.append((harvested, frozenset(build))) # build nothing 
        
        
        for f, i in future:
            if f in visited:
                continue
        
            old = distance.get(f, 1e6)
            new = weight + 1
            if new < old:
                distance[f] = new 
                e = [new, next(index), f, i]
                if f in active:
                    active[f][-2] = deleted 
                active[f] = e 
                pre[f] = state
                heappush(queue, e)
                
    return m
    
    
def best_score(instructions, limit):
    state = State(Robots(0, 0, 0, 1), Materials(0, 0, 0, 0))
    weight = 0
    return fastest_geode(instructions, state, weight, limit)
    
def twentyfour(i):
    return best_score(i, 24)

def thirtytwo(i):
    return best_score(i, 32)

if __name__ == '__main__':
    blueprints = {}

    for line in sys.stdin:
        id = int(re.match(r'^Blueprint (\d+)', line)[1])
        recipes = line.split(':')[1].split('.')
        
        make = [None] * 4
        for rec in recipes:
            rec = rec.strip()
            if not rec:
                continue
            
            
            m = re.match(r'Each ([a-z]+) robot costs (\d+) ([a-z]+)( and (\d+) ([a-z]+))*', rec)
            components = {}
            
            components = [0] * 4
            components[names.index(m[3])] = int(m[2])
            
            if m[4]:
                components[names.index(m[6])] = int(m[5])
                
            make[names.index(m[1])] = components 
            
        blueprints[id] = make
        
    with Pool() as p:
        scores = p.map(twentyfour, blueprints.values())
        print(sum(id * s for id, s in zip(blueprints.keys(), scores)))
    
    
        scores = p.map(thirtytwo, (blueprints[i] for i in range(1, 4)))
        print(reduce(lambda x, y: x * y, scores, 1))

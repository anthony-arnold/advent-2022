import sys
import copy


def play(monkeys, boredom, rounds, group):
    for _ in range(rounds):
        for monkey in monkeys.values():
            while monkey['items']:
                item = monkey['items'].pop(0)
                monkey['inspections'] += 1

                # apply op
                left, op, right = monkey['op']
                if left == 'old':
                    left = item
                if right == 'old':
                    right = item
                left = int(left)
                right = int(right)
                
                if op == '*':
                    item = left * right
                if op == '+':
                    item = left + right

                # boredom
                if boredom == 1:
                    item %= group
                else:
                    item //= boredom

                # test
                dest = monkey[(item % monkey['test']) == 0]
                monkeys[dest]['items'].append(item)

    maxinsp = [0, 0]
    for monkey in monkeys.values():
        i = monkey['inspections']
        if i > maxinsp[0]:
            maxinsp[1] = maxinsp[0]
            maxinsp[0] = i
        elif i > maxinsp[1]:
            maxinsp[1] = i

    print(maxinsp[0] * maxinsp[1])


if __name__ == "__main__":
    mid = None
    monkeys = {}
    group = 1

    for line in sys.stdin:
        line = line.strip()

        if line.startswith('Monkey'):
            mid = int(line.split()[-1].strip(':'))
            monkey = {
                'inspections': 0
            }
            monkeys[mid] = monkey

        elif line.startswith('Starting items'):
            items = [int(l) for l in line.split(':')[-1].split(',')]
            monkey['items'] = items

        elif line.startswith('Operation'):
            monkey['op'] = line.split()[-3:]

        elif line.startswith('Test'):
            monkey['test'] = int(line.split()[-1])
            group *= monkey['test'] 

        elif line.startswith('If true'):
            monkey[True] = int(line.split()[-1])

        elif line.startswith('If false'):
            monkey[False] = int(line.split()[-1])

    play(copy.deepcopy(monkeys), 3, 20, group)
    play(copy.deepcopy(monkeys), 1, 10000, group)

import sys

outcome_1 = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6,
}

outcome_2 = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7,
}

if __name__ == "__main__":
    rounds = [l.strip() for l in sys.stdin]

    print(sum(outcome_1[r] for r in rounds))
    print(sum(outcome_2[r] for r in rounds))

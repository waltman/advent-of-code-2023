from sys import argv
import re

def good_set(cubes):
    MAX_COUNT = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    toks = cubes.split(', ')
    for tok in toks:
        count, color = tok.split(' ')
        if MAX_COUNT[color] < int(count):
            return False

    return True

def good_game(game):
    toks = game.split('; ')
    for cubes in toks:
        if not good_set(cubes):
            return False

    return True

part1 = 0
with open(argv[1]) as f:
    for line in f:
        if m := re.match(r'Game (\d+): (.*)', line.rstrip()):
            game_num = int(m.group(1))
            game = m.group(2)
            if good_game(game):
                part1 += game_num

    print('Part 1:', part1)

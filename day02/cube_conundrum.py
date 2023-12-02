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

def min_set_prod(game):
    min_set = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    toks = game.split('; ')
    for cubes in toks:
        toks = cubes.split(', ')
        for tok in toks:
            count, color = tok.split(' ')
            min_set[color] = max(min_set[color], int(count))

    return min_set['red'] * min_set['green'] * min_set['blue']

part1 = 0
part2 = 0
with open(argv[1]) as f:
    for line in f:
        if m := re.match(r'Game (\d+): (.*)', line.rstrip()):
            game_num = int(m.group(1))
            game = m.group(2)
            if good_game(game):
                part1 += game_num
            part2 += min_set_prod(game)

print('Part 1:', part1)
print('Part 2:', part2)

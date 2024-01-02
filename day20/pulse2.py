import sys
from collections import deque
import copy
from math import lcm

class Module:
    def __init__(self, name, dest_str):
        self.name = name
        self.dests = dest_str.split(', ')

class FlipFlop(Module):
    def __init__(self, name, dest_str):
        super().__init__(name, dest_str)
        self.on = False

    def recv(self, from_mod, pulse):
        if pulse == 0:
            self.on = not self.on
            for dest in self.dests:
                yield(dest, int(self.on))

            # new_pulse = 0 if self.on else 1
            # for dest in self.dests:
            #     yield(dest, new_pulse)
            # self.on = not self.on

class Conjunction(Module):
    def __init__(self, name, dest_str):
        super().__init__(name, dest_str)
        self.mem = dict()
        self.got0 = False

    def recv(self, from_mod, pulse):
        self.got0 = (pulse == 0)
        self.mem[from_mod] = pulse
        new_pulse = 0 if all(self.mem.values()) else 1
        for dest in self.dests:
            yield(dest, new_pulse)

    def add_input(self, dest):
        self.mem[dest] = 0

    def next_pulse(self):
        return 0 if all(self.mem.values()) else 1

    def __str__(self):
        return ''.join([str(d) for d in self.mem.values()])

class Broadcast(Module):
    def __init__(self, name, dest_str):
        super().__init__(name, dest_str)

    def recv(self, from_mod, pulse):
        for dest in self.dests:
            yield(dest, pulse)

class Button(Module):
    def __init__(self, name, dest_str):
        super().__init__(name, dest_str)

    def recv(self, from_mod, pulse):
        yield(self.dests[0], 0)

def press_button(mods):
    queue = deque()
    queue.append(('root', 'button', 0))
    low, high = 0, 0
    while queue:
        src, dest, pulse = queue.popleft()
        if dest in mods:
            for new_dest, new_pulse in mods[dest].recv(src, pulse):
                if new_pulse == 0:
                    low += 1
                else:
                    high += 1
                queue.append((dest, new_dest, new_pulse))

    return low, high

def main():
    # parse the input
    modules = dict()
    with open(sys.argv[1]) as f:
        for line in f:
            name, dest_str = line.rstrip().split(' -> ')
            if name[0] == '%':
                modules[name[1:]] = FlipFlop(name[1:], dest_str)
            elif name[0] == '&':
                modules[name[1:]] = Conjunction(name[1:], dest_str)
            else:
                modules[name] = Broadcast(name, dest_str)

    modules['button'] = Button('button', 'broadcaster')

    # initialize destinations for all the conjunctions
    for k in modules:
        for dest in modules[k].dests:
            if dest in modules and type(modules[dest]) is Conjunction:
                modules[dest].add_input(k)

    mods = copy.deepcopy(modules)
    part2 = 0
    nodes = {'dr': 0, 'vn': 0, 'zx': 0, 'ln': 0}
    while not all(nodes.values()):
#    while True:
        part2 += 1
#        print('part2', part2, str(mods['dr']), str(mods['vn']), str(mods['zx']), str(mods['ln']))
        low, high = press_button(mods)
        if (low, high) == (1, 0):
            break
        else:
            if part2 % 1_000 == 0:
                print('step', part2)
                # for k, v in mods.items():
                #     if type(mods[k]) is Conjunction:
                #         print(k, str(v))
            # mask = []
            # for k in nodes.keys():
            #     mask.append(str(mods[k]))
            # mask.append(str(mods['kj']))
            # print(part2, mask)
            for k, v in nodes.items():
#                if v == 0 and str(mods[k]) == '0':
                if v == 0 and mods[k].got0:
                    print(f'found loop for {k} at {part2}')
                    nodes[k] = part2
            # # if str(mods['vn']) == '0':
            # #     print(part2, 'vn', mods['vn'], mods['pr'])
            # # if str(mods['dr']) == '0':
            # #     print(part2, 'dr', mods['dr'], mods['qs'])
            # # if str(mods['zx']) == '0':
            # #     print(part2, 'zx', mods['zx'], mods['jm'])
            # if str(mods['dr']) == '1':
            #     print(part2, 'dr', mods['dr'])
            # if str(mods['vn']) == '1':
            #     print(part2, 'vn', mods['vn'])
            # if str(mods['zx']) == '1':
            #     print(part2, 'zx', mods['zx'])
            # # print(part2, low, high)
            # # for k in mods:
            # #     if type(mods[k]) is Conjunction:
            # #         print(k, mods[k])
            
    print('Part 2', lcm(*nodes.values()))

main()

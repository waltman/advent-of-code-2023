import sys
from collections import deque
import copy

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
            new_pulse = 0 if self.on else 1
            for dest in self.dests:
                yield(dest, new_pulse)
            self.on = not self.on

class Conjunction(Module):
    def __init__(self, name, dest_str):
        super().__init__(name, dest_str)
        self.mem = dict()

    def recv(self, from_mod, pulse):
        self.mem[from_mod] = pulse
        new_pulse = 0 if all(self.mem.values()) else 1
        for dest in self.dests:
            yield(dest, new_pulse)

    def add_input(self, dest):
        self.mem[dest] = 0

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
    tot_low, tot_high = 0, 0
    for i in range(1000):
        low, high = press_button(mods)
        tot_low += low
        tot_high += high

    print('Part 1:', tot_low, tot_high, tot_low * tot_high)

    mods = copy.deepcopy(modules)
    part2 = 0
    while True:
        part2 += 1
        low, high = press_button(mods)
        if (low, high) == (1, 0):
            break
        else:
            if part2 % 1_000_000 == 0:
                print('step', part2)
            # if str(mods['vn']) == '0':
            #     print(part2, 'vn', mods['vn'], mods['pr'])
            # if str(mods['dr']) == '0':
            #     print(part2, 'dr', mods['dr'], mods['qs'])
            # if str(mods['zx']) == '0':
            #     print(part2, 'zx', mods['zx'], mods['jm'])
            if str(mods['ln']) == '0':
                print(part2, 'ln', mods['ln'], mods['jv'])
            # print(part2, low, high)
            # for k in mods:
            #     if type(mods[k]) is Conjunction:
            #         print(k, mods[k])
            
    print('Part 2', part2)

main()

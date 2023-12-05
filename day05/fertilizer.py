from sys import argv

class Almanac:
    def __init__(self):
        self.maps = []

    def add_map(self, dest_start, src_start, range_len):
        self.maps.append((dest_start, src_start, range_len))

    def map_val(self, val):
        for dest_start, src_start, range_len in self.maps:
            if src_start <= val < src_start+range_len:
                return dest_start + (val-src_start)
        return val

    def __repr__(self):
        return str(self.maps)

steps = ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']

def location(seed, almanacs):
    val = seed
    for k in steps:
        val = almanacs[k].map_val(val)
    return val

almanacs = {k:Almanac() for k in steps}
k = ''
with open(argv[1]) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('seeds: '):
            seeds = [int(d) for d in line[7:].split(' ')]
        elif line.startswith('seed-'):
            k = 'soil'
        elif line.startswith('soil-'):
            k = 'fertilizer'
        elif line.startswith('fertilizer-'):
            k = 'water'
        elif line.startswith('water-'):
            k = 'light'
        elif line.startswith('light-'):
            k = 'temperature'
        elif line.startswith('temperature-'):
            k = 'humidity'
        elif line.startswith('humidity-'):
            k = 'location'
        elif line and line[0].isdigit():
            dest_start, src_start, range_len = [int(d) for d in line.split(' ')]
            almanacs[k].add_map(dest_start, src_start, range_len)

print('Part 1:', min([location(seed, almanacs) for seed in seeds]))    

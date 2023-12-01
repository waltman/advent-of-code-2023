from sys import argv

def calibrate(line):
    digits = [c for c in line if c.isdigit()]
    return int(digits[0]) * 10 + int(digits[-1]) if digits else 0

def transform(line):
    vals = {'one':   '1',
            'two':   '2',
            'three': '3',
            'four':  '4',
            'five':  '5',
            'six':   '6',
            'seven': '7',
            'eight': '8',
            'nine':  '9',
            }

    ss = line + '    '
    digits = []
    for i in range(len(ss)):
        if ss[i].isdigit():
            digits.append(ss[i])
        else:
            for k, v in vals.items():
                if ss[i:i+len(k)] == k:
                    digits.append(v)
    return digits

calibration_total1 = 0
calibration_total2 = 0

with open(argv[1]) as f:
    for line in f:
        line = line.rstrip()
        calibration_total1 += calibrate(line)
        calibration_total2 += calibrate(transform(line))

print('Part 1:', calibration_total1)
print('Part 2:', calibration_total2)


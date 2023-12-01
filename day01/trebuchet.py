from sys import argv

calibration_total = 0

with open(argv[1]) as f:
    for line in f:
        digits = [c for c in line if c.isdigit()]
        calibration = int(digits[0]) * 10 + int(digits[-1])
        calibration_total += calibration

print('Part 1:', calibration_total)


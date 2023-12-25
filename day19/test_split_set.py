def split_set(vals, op, n):
    if op == '<':
        mask = set(range(1, n))
    else:
        mask = set(range(n+1, 4001))
    out_set = vals - mask
    return vals - out_set, out_set

x = set(range(1,11))
print(split_set(x, '<', 5))
print(split_set(x, '>', 5))

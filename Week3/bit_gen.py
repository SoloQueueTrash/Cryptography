def gen_all_hex():
    i = 0
    while i < 16**10:
        yield "{:010X}".format(i)
        i += 1

for s in gen_all_hex():
    print(s)
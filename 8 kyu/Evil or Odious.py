def evil(n):
    b = bin(n)
    counter = 0
    for x in range(0, len(b)):
        if b[x] is '1':
            counter += 1
    return "It's Evil!" if counter % 2 is 0 else "It's Odious!"
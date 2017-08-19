def match_arrays(v, r):
    solution = 0
    for x in range(0, len(v)):
        for y in range(0, len(r)):
            if v[x] == r[y]:
                solution += 1
    return solution


# DON'T remove
verbose = False  # set to True to diplay arrays being tested in the random tests
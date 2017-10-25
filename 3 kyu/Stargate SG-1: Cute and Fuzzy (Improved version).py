def wire_DHD_SG1(wires):
    grid = {(y, x) for y, row in enumerate(wires.split()) for x, c in enumerate(row) if c in '.G'}
    gate = {(y, x) for y, row in enumerate(wires.split()) for x, c in enumerate(row) if c == 'G'}.pop()
    start = {(y, x) for y, row in enumerate(wires.split()) for x, c in enumerate(row) if c == 'S'}.pop()

    paths, mindists, minpaths = [[start]], {start: 0}, {start: []}
    while paths:
        newbests = {}
        for path in [e for e in [path + [p] for path in paths for p in possibles(grid, path)] if e]:
            dist, pos = distance(path), path[-1]
            if gate in mindists and mindists[gate] <= dist: continue
            if pos not in mindists or pos in mindists and dist < mindists[pos]:
                mindists[pos], minpaths[pos], newbests[pos] = dist, path, path
        paths = [p for p in newbests.values()]

    if gate in minpaths:
        p = minpaths[gate][1:-1]
        return '\n'.join(
            ''.join('P' if (y, x) in p else c for x, c in enumerate(row)) for y, row in enumerate(wires.split()))

    return "Oh for crying out loud..."


distance = lambda p: sum(1 if a[0] == b[0] or a[1] == b[1] else 2 ** 0.5 for a, b in zip(p, p[1:]))


def possibles(grid, path):
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return grid & {(path[-1][0] + y, path[-1][1] + x) for y, x in moves} - {p for p in path}
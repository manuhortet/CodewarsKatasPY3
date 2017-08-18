def to_weird_case(string):
    res = ''
    string.split(' ')
    for x in range(0, len(string.split(' '))):
        if string[x] is '' or string[x] is None:
            res = res
        for y in range(0, len(string.split(' ')[x])):
            if y % 2 is 0:
                res += string.split(' ')[x][y].upper()
            else:
                res += string.split(' ')[x][y].lower()
        if x+1 < len(string.split(' ')):
            res += ' '
    return res
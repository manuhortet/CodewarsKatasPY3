def accum(s):
    res = s[0].upper()
    for x in range(1, len(s)):
        res += '-'
        res += s[x].upper()
        for y in range(0, x):
            res += s[x].lower()
    return res
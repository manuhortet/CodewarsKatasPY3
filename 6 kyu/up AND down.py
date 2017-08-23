def arrange(strng):
    s = strng.split(" ")
    for x in range(1, len(s)):
        if x % 2 is not 0:
            if len(s[x-1]) > len(s[x]):
                aux = s[x-1]
                s[x - 1] = s[x]
                s[x] = aux
        else:
            if len(s[x-1]) < len(s[x]):
                aux = s[x-1]
                s[x - 1] = s[x]
                s[x] = aux
    result = ""
    for x in range(0, len(s)):
        if x % 2 == 0:
            result += s[x].lower()
        else:
            result += s[x].upper()
        if x is not len(s)-1:
            result += " "

    return result

# This code is bad and so I feel
# sorry
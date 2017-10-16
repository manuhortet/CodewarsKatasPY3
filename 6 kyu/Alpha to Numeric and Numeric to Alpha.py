def AlphaNum_NumAlpha(string):
    res, x = "", 0
    while x < len(string):
        if 96 < ord(string[x]) < 123:
            res += str(alphabetnums[string[x]])
        else:
            if x is len(string) - 1:
                res += chr(int(string[x]) + 96)
            elif 96 < ord(string[x+1]) < 123:
                res += chr(int(string[x]) + 96)
            else:
                res += chr(int(str(string[x]) + str(string[x+1])) + 96)
                x += 1
        x += 1
    return res


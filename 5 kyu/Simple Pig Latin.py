def pig_it(text):
    text2 = text.split(" ")
    result = ''
    for x in range(0, len(text2)):
        if text2[x] is '?':
            return result + '?'
        if text2[x] is '!':
            return result + '!'
        text2[x] += text2[x][0]
        text2[x] = text2[x][1:]
        text2[x] += 'ay'
        if x is not len(text2)-1:
            result += text2[x] + ' '
        else:
            result += text2[x]
    return result
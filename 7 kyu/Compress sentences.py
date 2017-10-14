def compress(sentence):
    if len(sentence) is not 0:
        words = sentence.lower().split(" ")
        res = []
        for x in words:
            if str(x) not in res:
                res.append(x)
        sol = ""
        for x in words:
            sol += str(res.index(x))
        return sol
    else:
        return sentence

def last(s):
    return sorted(s.split(" "), key=lambda word: word[len(word)-1])

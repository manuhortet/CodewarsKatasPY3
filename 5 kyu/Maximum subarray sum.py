def maxSequence(arr):
    maximum = total = 0
    for a in arr:
        total = max(0, total + a)
        if total > maximum:
            maximum = total
    return maximum
def is_monotone(heights):
    if heights is None:
        return True
    for x in range (1, len(heights)):
        if heights[x] < heights[x-1]:
            return False
    return True
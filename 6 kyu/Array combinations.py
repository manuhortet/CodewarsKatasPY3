def solve(arr):
    j = 1
    for i in range(0, len(arr)):
        j *= len(set(arr[i]))
    return j

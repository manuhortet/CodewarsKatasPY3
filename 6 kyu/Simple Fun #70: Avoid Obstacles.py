def avoid_obstacles(arr):
    sx = True
    for n in range(2, 100):
        x = n
        sx = True
        while x < 100:
            for m in range(0, len(arr)):
                if x == arr[m]:
                    sx = False
                    break
            x += n
        if sx:
            return n
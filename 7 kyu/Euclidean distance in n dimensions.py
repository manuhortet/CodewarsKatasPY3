def euclidean_distance(point1, point2):
    vector = []
    for x in range(0, len(point1)):
       vector.append(point1[x]-point2[x])
    sol = 0
    for x in range(0, len(vector)):
        sol += vector[x]**2
    return round(sol**.5, 2)
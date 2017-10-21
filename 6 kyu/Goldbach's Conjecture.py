def goldbach_partitions(n):
    if n % 2 is not 0: return []

    def is_primes(x):
        if x >= 2:
            for y in range(2, x):
                if not (x % y):
                    return False
        else:
            return False
        return True

    primes = []

    for x in range(0, n):
        if is_primes(x):
            primes.append(x)

    partitions = []

    for x in primes:
        for y in primes:
            if (x + y) == n:
                partitions.append(str(x) + '+' + str(y))
    return partitions[:int((len(partitions) / 2) + .5)]

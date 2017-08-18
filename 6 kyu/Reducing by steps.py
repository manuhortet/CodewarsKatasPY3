def gcdi(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a if a > 0 else -a


def lcmu(a, b):
    sol = (a * b) // gcdi(a, b)
    return sol if sol > 0 else -sol


def som(a, b):
    return a + b


def maxi(a, b):
    return max(a, b)


def mini(a, b):
    return min(a, b)


def oper_array(fct, arr, init):
    r = [fct(init, arr[0])]
    for x in range(0, len(arr)-1):
        r.append(fct(r[x], arr[x+1]))
    return r


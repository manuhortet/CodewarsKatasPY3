def namelist(names):
    quantity = len(names)
    solution = ""
    for x in range(0, quantity):
        solution += names[x]['name']
        if x is quantity - 2:
            solution += ' & '
        elif x < quantity - 2:
            solution += ', '
    return solution

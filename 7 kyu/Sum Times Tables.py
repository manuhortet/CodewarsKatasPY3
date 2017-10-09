def sum_times_tables(table, a, b):
    if len(table) is 0: return 0
    result = 0
    for x in range(0, len(table)):
        for y in range(a, b+1):
            result += table[x] * y

    return result
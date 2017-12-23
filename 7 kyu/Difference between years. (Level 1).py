def how_many_years (date1,date2):
    year1 = date1[0:4]
    year2 = date2[0:4]
    return int(year1) - int(year2) if year1 > year2 else int(year2) - int(year1)
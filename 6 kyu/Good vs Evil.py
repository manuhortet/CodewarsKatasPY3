def goodVsEvil(good, evil):
    good = good.split(" ")
    evil = evil.split(" ")
    evil_worth = int(evil[0]) * 1 + int(evil[1]) * 2 + int(evil[2]) * 2 + int(evil[3]) * 2 + int(evil[4]) * 3 + int(evil[5]) * 5 + int(evil[6]) * 10
    good_worth = int(good[0]) * 1 + int(good[1]) * 2 + int(good[2]) * 3 + int(good[3]) * 3 + int(good[4]) * 4 + int(good[5]) * 10
    if evil_worth > good_worth:
        return 'Battle Result: Evil eradicates all trace of Good'
    elif evil_worth == good_worth:
        return 'Battle Result: No victor on this battle field'
    else:
        return 'Battle Result: Good triumphs over Evil'

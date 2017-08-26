def rps(p1, p2):
    win = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if win[p1] == p2:
        return "Player 1 won!"
    if win[p2] == p1:
        return "Player 2 won!"
    return "Draw!"
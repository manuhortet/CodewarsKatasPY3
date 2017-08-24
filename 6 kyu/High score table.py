class HighScoreTable:
    def __init__(self, len=3):
        self.len = len
        self.reset()

    def update(self, score):
        self.scores = sorted(self.scores + [score], reverse=True)[:self.len]

    def reset(self):
        self.scores = []
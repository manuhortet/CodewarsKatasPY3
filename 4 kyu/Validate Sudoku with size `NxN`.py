class Sudoku(object):
    def __init__(self, data):
        n = int(len(data) ** 0.5)
        self.n = n
        self.data = data
        self.lines = data
        if not all(len(line) == len(data) for line in self.lines):
            self.lines = [[0] * n]
            self.columns = []
            self.squares = []
        else:
            self.columns = [[row[i] for row in data] for i in range(n)]
            self.squares = []
            for i in range(n):
                for j in range(n):
                    rows = data[i * n:i * n + n]
                    cols = [row[j * n:j * n + n] for row in rows]
                    squa = sum(cols, [])
                    self.squares.append(squa)

    def is_valid(self):
        if self.data[0][0] is True:
            return False
        iterables = self.lines, self.columns, self.squares
        for iterable in iterables:
            for segment in iterable:
                if list(sorted(segment)) != list(range(1, self.n ** 2 + 1)):
                    return False
        print(self.data)
        return True
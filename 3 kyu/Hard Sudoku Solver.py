import math

def generate_matrix(lines, cols, val):
    result = []

    for i in range(lines):
        line = []

        for j in range(cols):
            line.append(val)

        result.append(line)

    return result


def depth_first_search(board, rows, cols, blocks, positions):
    if len(positions) == 0:
        return True

    nr = int(math.sqrt(len(board)))

    i, j = positions.pop()

    for k in range(len(board)):
        index = int(i / nr) * nr + int(j / nr)

        if rows[i][k] or cols[j][k] or blocks[index][k]:
            continue

        board[i][j] = k + 1
        rows[i][k] = True
        cols[j][k] = True
        blocks[index][k] = True

        if depth_first_search(board, rows, cols, blocks, positions) == True:
            return True

        blocks[index][k] = False
        cols[j][k] = False
        rows[i][k] = False
        board[i][j] = 0

    positions.append((i, j))

    return False


def solve(board):
    if len(board) == 0:
        return []

    if len(board) != len(board[0]):
        return []

    for i in range(len(board)):
        for j in range(len(board[0])):
            aux = int(board[i][j])

    a, b, positions, d = init_matrixes(board)

    if depth_first_search(board, d, b, a, positions):
        return board

    return []


def init_matrixes(board):
    a = generate_matrix(len(board), len(board), False)
    b = generate_matrix(len(board), len(board), False)
    c = generate_matrix(len(board), len(board), False)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                a[i][board[i][j] - 1] = True
                b[j][board[i][j] - 1] = True

                size = int(math.sqrt(len(board[0])))
                index = int(i / size) * size + int(j / size)
                c[index][board[i][j] - 1] = True

    positions = to_boolean(board)

    return c, b, positions, a


def to_boolean(board):
    result = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                result.append((i, j))

    return result

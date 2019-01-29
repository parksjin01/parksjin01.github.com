domino = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [5, 6], [5, 7], [5, 8], [5, 9], [6, 7], [6, 8], [6, 9], [7, 8], [7, 9], [8, 9]]
column = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8}

def print_board(board):
    s = ''
    for column in board:
        for row in column:
            s += str(row)
        s += "\n"
    s.strip("\n")
    print s,

def check_duplication(arr):
    for num in range(1, 10):
        if arr.count(num) > 1:
            return False
    return True

def row_check(board, row, column):
    res = board[column]
    return check_duplication(res)

def column_check(board, row, column):
    res = []
    for column in range(9):
        res.append(board[column][row])

    return check_duplication(res)

def square_check(board, row, column):
    res = []
    row /= 3
    column /= 3
    for tmp_row in range(row * 3, (row + 1) * 3):
        for tmp_column in range(column * 3, (column + 1) * 3):
            res.append(board[tmp_column][tmp_row])

    return check_duplication(res)

# def board_compare(board):
#     answer = [list("872643195"),
#               list("361975842"),
#               list("549218637"),
#               list("126754983"),
#               list("738169254"),
#               list("495832761"),
#               list("284597316"),
#               list("657381429"),
#               list("913426578")]
#
#     for y in range(8):
#         for x in range(8):
#             if int(answer[y][x]) != board[y][x]:
#                 return False
#     return True

def solving(board, row, column, used_domino):
    if row == 8 and column == 8:
        # if board_compare(board) == False:
            # print_board(board)
            # print used_domino
        print_board(board)
        # print "\n\n----------------------------------------\n\n"
        return 1
    elif board[column][row] > 0:
        row += 1
        if row > 8:
            row = 0
            column += 1
        return solving(board, row, column, used_domino)
    else:
        res = 0
        for d in domino:
            if d not in used_domino:
                # pprint.pprint(board, width=200)
                if row + 1 < 9 and board[column][row + 1] == 0:
                    board[column][row] = d[0]
                    board[column][row + 1] = d[1]
                    next_row = row + 1
                    next_column = column
                    if next_row > 8:
                        next_row = 0
                        next_column += 1
                    if row_check(board, row, column) and column_check(board, row + 1, column) and column_check(board, row, column) and square_check(board, row, column):
                        res = solving(board, next_row, next_column, used_domino + [d])
                    if res == 1:
                        return res

                    board[column][row] = d[1]
                    board[column][row + 1] = d[0]
                    next_row = row + 1
                    next_column = column
                    if next_row > 8:
                        next_row = 0
                        next_column += 1
                    if row_check(board, row, column) and column_check(board, row + 1, column) and column_check(board, row, column) and square_check(board, row, column):
                        res = solving(board, next_row, next_column, used_domino + [d])
                    if res == 1:
                        return res

                    board[column][row] = 0
                    board[column][row + 1] = 0

                if column + 1 < 9 and board[column + 1][row] == 0:
                    board[column][row] = d[0]
                    board[column + 1][row] = d[1]
                    next_row = row + 1
                    next_column = column
                    if next_row > 8:
                        next_row = 0
                        next_column += 1
                    if row_check(board, row, column) and row_check(board, row, column + 1) and column_check(board, row, column) and square_check(board, row, column):
                        res = solving(board, next_row, next_column, used_domino + [d])
                    if res == 1:
                        return res

                    board[column][row] = d[1]
                    board[column + 1][row] = d[0]
                    next_row = row + 1
                    next_column = column
                    if next_row > 8:
                        next_row = 0
                        next_column += 1
                    if row_check(board, row, column) and row_check(board, row, column + 1) and column_check(board, row, column) and square_check(board, row, column):
                        res = solving(board, next_row, next_column, used_domino + [d])
                    if res == 1:
                        return res

                    board[column][row] = 0
                    board[column + 1][row] = 0

puzzle = 1
while True:
    num_input = input()
    if num_input == 0:
        break
    used_domino = []
    board = []
    for _ in range(9):
        board.append([0] * 9)

    for _ in range(int(num_input)):
        d1, s, d2, e = raw_input().strip(" ").split(" ")

        used_domino.append(sorted(map(int, [d1, d2])))
        board[column[s[0]]][int(s[1]) - 1] = int(d1)
        board[column[e[0]]][int(e[1]) - 1] = int(d2)

    coordinate = raw_input().strip(" ").split(" ")
    for num in range(1, 10):
        board[column[coordinate[num - 1][0]]][int(coordinate[num - 1][1]) - 1] = num

    print "Puzzle", puzzle
    puzzle += 1
    solving(board, 0, 0, used_domino)

board = [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]




is_sudoku = True

for each in board:
    row = set()
    for every in each:
        if every == ".":
            continue 
        elif every in row:
            is_sudoku = False
        
        else:
            row.add(every)

for i in range(len(board)):
    column = set()
    for j in range(len(board)):
        if board[j][i] == ".":
            continue
        elif board[j][i] in column:
            is_sudoku = False
        else:
            column.add(board[j][i])

starts = [(0,0),(0,3),(0,6),
          (3,0),(3,3),(3,6),
          (6,0),(6,3),(6,6)]

for i , j in starts:
    s = set()
    for row in range(i, i+3):
        for col in range(j, j+3):
            item = board[row][col]

            if item == ".":
                continue
        
            elif item in s:
                is_sudoku = False
            else:
                s.add(item)          

print(is_sudoku)

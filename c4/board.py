def create_board(cols: int = 7, rows: int = 6) -> list[list[str]]:
    board = []
    for col in range(rows):
        l = []
        for row in range(cols):
            l.append("-")
        board.append(l)
    return board



def column_is_full(board: list[list[str]], col: int) -> bool:
    for i in range(len(board)):
        if board[i][col] == "-":
            return False

    return True


def drop_disc(board: list[list[str]], col: int, mark: str) -> tuple[int,int] | None:
    if column_is_full(board,col):
        return
    else:
        x = -1
        if board[x][col] == "-":
            board[x][col] = mark
        else:
            while board[x][col] != "-":
                x -= 1
    return x,col

def legal_moves(board:list[list[str]]) -> list[int]:
    col =[]
    for i in range(len(board[0])):
        empty = column_is_full(board,i)
        if empty:
          continue
        else:
            col.append(i)
    return col






# m = [[1,2,3],
#      [1,2,3]]
# for i in range(len(m)):
#     for j in range(len(m)):
#         print (j)
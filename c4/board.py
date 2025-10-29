def create_board(cols: int = 7, rows: int = 6) -> list[list[str]]:
    board = []
    for col in range(rows):
        l = []
        for row in range(cols):
            l.append("-")
        board.append(l)
    return board



def column_is_full(board: list[list[str]], col: int) -> bool:
    for i in range(board):
        for j in range(i):


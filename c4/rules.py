def in_bounds(board:list[list[str]],row:int, col:int) -> bool:
    row_bound = len(board)  >= row
    col_bound = len(board[0])  >= col
    return row_bound,col_bound

def has_winner_from(board:list[list[str]]) -> bool:
    pass
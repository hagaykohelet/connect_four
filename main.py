from c4.board import create_board,drop_disc,legal_moves,column_is_full,print_board,render
from c4.rules import in_bounds


if __name__ == "__main__":
    print(in_bounds(create_board(),2,9))
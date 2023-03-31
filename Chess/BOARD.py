import PIECES

#Set the board
def set_board(white_pieces,black_pieces,board):
    for i in range(len(white_pieces)):
        board[white_pieces[i].column][white_pieces[i].row] = white_pieces[i].name
    for i in range(len(black_pieces)):
        board[black_pieces[i].column][black_pieces[i].row] = black_pieces[i].name
    return board

#Print the board
def print_board(board):
    for row in range(8,0,-1):
        for column in range(1,9):
            if not board[column][row]:
                if (column + row) % 2 == 0:
                    print(" ▫ ",end="")
                else:
                    print(" ▪ ",end="")
            elif board[column][row] == "pawn":
                print(" ♙ ",end="")
        print("\n")
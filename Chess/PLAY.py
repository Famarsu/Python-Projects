import BOARD
import PIECES



#Create the empty variables board, white_pieces and black_pieces
#board = [[[] for _ in range(9)] for _ in range(9)]
board = [[["",""] for _ in range(10)] for _ in range(10)]
white_pieces = []
black_pieces = []

#Fill the board with pieces
white_pieces = PIECES.start_white_pieces(white_pieces)
black_pieces = PIECES.start_black_pieces(black_pieces)
board = BOARD.set_board(white_pieces,black_pieces,board)
#BOARD.start_board(board)

#Print the board
BOARD.print_board(board)
#print(board[white_pieces[0].column + 1][white_pieces[0].row + 1][0])
for piece in white_pieces:
    print(piece.get_moves(board))
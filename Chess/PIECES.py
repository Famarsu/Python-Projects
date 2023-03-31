def start_white_pieces(white_pieces):
    white_pieces.append(Pawn("white","P",1,2))
    white_pieces.append(Pawn("white","P",2,2))
    white_pieces.append(Pawn("white","P",3,2))
    white_pieces.append(Pawn("white","P",4,2))
    white_pieces.append(Pawn("white","P",5,2))
    white_pieces.append(Pawn("white","P",6,2))
    white_pieces.append(Pawn("white","P",7,2))
    white_pieces.append(Pawn("white","P",8,2))
    return white_pieces

def start_black_pieces(black_pieces):
    black_pieces.append(Pawn("black","p",1,7))
    black_pieces.append(Pawn("black","p",2,7))
    black_pieces.append(Pawn("black","p",3,7))
    black_pieces.append(Pawn("black","p",4,7))
    black_pieces.append(Pawn("black","p",5,7))
    black_pieces.append(Pawn("black","p",6,7))
    black_pieces.append(Pawn("black","p",7,7))
    black_pieces.append(Pawn("black","p",8,7))
    return black_pieces

class Piece:

    def __init__(self, color, name, column, row):
        self.color = color
        self.name = name
        self.column = column
        self.row = row

class Pawn(Piece):

    def get_moves(self,board):
        self.moves = []
        
        # For white
        if self.color == "white":
            
            # Checking en passant
            # if self.row == 5 and moves_history[-1] == [Pawn, any column, from row 7 to 5]:
            #   self.moves.append([moves_history[-1][column],6])

            # Checking capture
            if self.column > 1 and board[self.column - 1][self.row + 1][0] == "black":
                self.moves.append([self.column - 1, self.row + 1])
            if self.column < 8 and board[self.column + 1][self.row + 1][0] == "black":
                self.moves.append([self.column + 1, self.row + 1])

            # Checking advance
            if board[self.column][self.row + 1] == ["",""]: 
                self.moves.append([self.column, self.row + 1])
            if self.row == 2 and board[self.column][self.row + 1] == ["",""] and board[self.column][self.row + 2] == ["",""]: 
                self.moves.append([self.column, self.row + 2])


        # For black
        else:
            # Checking en passant
            # if self.row == 4 and moves_history[-1] == [Pawn, any column, from row 2 to 4]:
            #   self.moves.append([moves_history[-1][column],3])

            # Checking capture
            # if self.column > 1 and board.get_occupation(self.column - 1, self.row - 1) == "white":
                self.moves.append([self.column - 1, self.row - 1])
            # if self.column < 8 and board.get_occupation(self.column + 1, self.row - 1) == "white":
                self.moves.append([self.column + 1, self.row - 1])

            # Checking advance 1
            # if board.get_occupation(self.column, self.row - 1) == "empty": 
                self.moves.append([self.column, self.row - 1])
            # if self.row == 7 and board.get_occupation(self.column, self.row - 1) == "empty" and board.get_occupation(self.column, self.row - 2) == "empty": 
                self.moves.append([self.column, self.row - 2])


        return self.moves
    



# pawn1 = Pawn("pawn1", "white",1 ,2 ,0)
# print(pawn1.get_moves())

#input("Enter piece", x, "and enter your move", y)

#    if y in x.get_moves():
#        board.update = y
class Piece:

    def __init__(self,name, color, column, row):
        self.name = name
        self.color = color
        self.column = column
        self.row = row
        self.alive = True

class Pawn(Piece):

    def get_moves(self):
        self.moves = []
        
        # For white
        if self.color == "white":
            
            # Checking en passant
            # if self.row == 5 and moves_history[-1] == [Pawn, any column, from row 7 to 5]
            # self.moves.append([6, moves_history[-1][column])

            # Checking capture

            # Checking advance
            # if self.row + 1 < 9 and board.get_occupation(pawn.column, pawn.row + 1) == "empty": 
            self.moves.append([self.column, self.row + 1])


        # For black
        else:
            # Checking en passant

            # Checking capture

            # Checking advance
            # if self.row - 1 > 0 and board.get_occupation(pawn.column, pawn.row - 1) == "empty": 
            self.moves.append([self.column, self.row - 1])



        return self.moves
    



pawn1 = Pawn("pawn1", "white", 1,2)
print(pawn1.get_moves())

#input("Enter piece", x, "and enter your move", y)

#    if y in x.get_moves():
#        board.update = y
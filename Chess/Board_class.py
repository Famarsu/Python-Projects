class Board:

    def __init__(self, move_num):
        self.move = move_num
        self.occupation = [["empty" for _ in range(8)] for _ in range(8)]

    def get_occupation(self, column, row):
        return self.occupation[column-1][row-1]

    def start_game():
        pawn1 = Pawn("pawn1","white",1,2)
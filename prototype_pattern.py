from typing import List
import copy

class ChessPiece:
    def __init__(self,name:str, position:str, color:str):
        self.name = name
        self.position = position
        self.color = color

    def display_piece(self):
        return f"{self.name} of {self.color}color is at {self.position} position"

    def clone(self):
        return copy.deepcopy(self)
        #other way to clone
        #ChessPiece(self.name,self.position,self.color)

class ChessBoard:
    def __init__(self,):
        self.pieces:List[ChessPiece] = []

    def add_piece(self,new_piece:"ChessPiece"):
        self.pieces.append(new_piece)

    def display_board(self):
        print("current state of board")
        for piece in self.pieces:
            print(f"  {piece.display_piece()}")

    def clone_board(self):
        return copy.deepcopy(self)


piece1= ChessPiece("king","e4","white")

piece2= ChessPiece.clone(piece1)

piece3= ChessPiece("Queen","d3","black")

#print(id(piece1))
#print(id(piece2))

board=ChessBoard()
board.add_piece(piece1)
board.add_piece(piece2)
board.add_piece(piece3)


board.display_board()
print("-------new board-------")

new_board= board.clone_board()
new_board.display_board()
p3 = ChessPiece("bishop","a3","black")
new_board.add_piece(p3)


print("-----cloned board----")

new_board.display_board()

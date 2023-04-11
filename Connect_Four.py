import numpy

def create_board():
  board = numpy.zeros((6,7))
  return board
def drop_piece():
  pass
def is_valid_location(board, selection):
  pass
def get_next_open_row():
  pass
  
board =  create_board()
game_over = False
turn = 0
while not game_over:
  #Ask for player 1 input
  if turn == 0:
    selection = int(input("Player 1 make your selection (0-6):"))

  else:
    selection = int(input("Player 2 make your selection (0-6): "))
  turn += 1
  turn = turn % 2
  

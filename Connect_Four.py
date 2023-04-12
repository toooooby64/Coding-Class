import numpy
ROW_COUNT = 6
COL_COUNT = 7
def create_board():
  board = numpy.zeros((6,7))
  return board
def drop_piece(board,row,col,piece):
  board[row][col] = piece
def is_valid_location(board, selection):
  return board[5][selection] == 0
def get_next_open_row(board,selection):
  for r in range(ROW_COUNT):
    if board[r][selection] == 0:
      return r 
board =  create_board()
print(board)
game_over = False
turn = 0
while not game_over:
  #Ask for player 1 input
  if turn == 0:
    selection = int(input("Player 1 make your selection (0-6):"))
    if is_valid_location(board,selection):
      row = get_next_open_row(board,selection)
      drop_piece(board,row,selection,1)

  else:
    selection = int(input("Player 2 make your selection (0-6): "))
    if is_valid_location(board,selection):
      row = get_next_open_row(board,selection)
      drop_piece(board,row,selection,2)
  print(board)

  turn += 1
  turn = turn % 2
  
  


  

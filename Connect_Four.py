import numpy
import pygame
import sys
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

def winning_move(board,piece):
  for c in range(COL_COUNT):
    for r in range(ROW_COUNT):
      if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
        return True

  for c in range(COL_COUNT):
    for r in range(ROW_COUNT):
      if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
        return True

  for c in range(COL_COUNT):
    for r in range (ROW_COUNT):
      if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
        return True

  for c in range(COL_COUNT):
    for r in range (ROW_COUNT):
      if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] and board[r-3][c+3] == piece:
        return True
  
def draw_board(board):
  


def print_board(board):
  print(numpy.flip(board,0))
  
board =  create_board()
print(board)
game_over = False
turn = 0

pygame.init()
SQUARESIZE = 100
witdh  =  COL_COUNT = SQUARESIZE
height =   ROW_COUNT = SQUARESIZE
size = (witdh,height)
screen = pygame.display.set_mode(size)

while not game_over:

  for event in pygame.event.get():
    if event.type == pygame.QUIT():
      sys.exit()
    if event.type == pygame.MOUSEDBUTTONDOWN:
      continue
  
  #Ask for player 1 input
  if turn == 0:
    selection = int(input("Player 1 make your selection (0-6):"))
    if is_valid_location(board,selection):
      row = get_next_open_row(board,selection)
      drop_piece(board,row,selection,1)
      if winning_move(board,1):
        print("PLAYER 1 WINS!!! :D")
        game_over = True

  else:
    selection = int(input("Player 2 make your selection (0-6): "))
    if is_valid_location(board,selection):
      row = get_next_open_row(board,selection)
      drop_piece(board,row,selection,2)
      if winning_move(board,2):
        print("PLAYER 2 WINS!!! :D")
        game_over = True
  print_board(board)

  turn += 1
  turn = turn % 2
  
  
  




    
  


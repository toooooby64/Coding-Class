import pygame
import pygame.gfxdraw

pygame.init()

screen_width = 700
screen_height = 500

#Defining colors
white = (255, 255, 255)
blue = (67, 238, 250)
red = (255, 0, 0)
black = (0, 0, 0)
pink = (255, 192, 203)
orange = (255, 165, 0)
yellow = (255, 255, 0)
violet = (177, 3, 252)
green = (38,245,45)

penColor = black

drawingWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Paint")
drawingWindow.fill((255, 255, 255))

backimg = pygame.image.load("white.jpg").convert_alpha()
drawingWindow.blit(backimg, (0, 0))

clearRect = (119, 17, 562, 456)

col1 = (22, 81, 30, 34)
col2 = (56, 81, 34, 34)
col3 = (22, 120, 30, 33)
col4 = (56, 120, 34, 32)
col5 = (22, 156, 30, 33)
col6 = (56, 156, 34, 32)
col7 = (22, 192, 30, 33)
col8 = (56, 192, 34, 32)

buttonSelect = (22, 81, 30, 34)


def drawRectangle():
    pygame.gfxdraw.box(drawingWindow, col1, black)
    pygame.gfxdraw.box(drawingWindow, col2, blue)
    pygame.gfxdraw.box(drawingWindow, col3, red)
    pygame.gfxdraw.box(drawingWindow, col4, green)
    pygame.gfxdraw.box(drawingWindow, col5, pink)
    pygame.gfxdraw.box(drawingWindow, col6, orange)
    pygame.gfxdraw.box(drawingWindow, col7, yellow)
    pygame.gfxdraw.box(drawingWindow, col8, violet)


drawRectangle()

pygame.mouse.set_cursor(*pygame.cursors.broken_x)
exit_game = False

while not exit_game:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit_game = True
pygame.display.update()

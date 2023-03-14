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

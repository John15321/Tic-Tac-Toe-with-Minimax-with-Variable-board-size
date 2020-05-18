'''
Module responsible for  configuring screen graphics like color, width, height etc.
'''
import pygame

# Initializing PyGame
pygame.init()

# Title and Icon
pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(pygame.image.load("./Resources/game_icon.png"))

# screen color (in RGB)
screen_color = (245, 167, 167)  # very darker blue/purple
hover_color_for_buttons = (249, 216, 156)
background_color_for_buttons = (130, 196, 195)
# Creating the screen
# screen size (has to be a tuple: width x height)
screen_width = 800
screen_height = 600
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)

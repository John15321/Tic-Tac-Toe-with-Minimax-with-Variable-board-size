#!/usr/bin/python

import pygame
import buttons

# Initializing PyGame
pygame.init()



# Creating the screen
# screen size (has to be a tuple: width x height)
screen_width = 800
screen_height = 600
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
# screen color (in RGB)
screen_color = (245, 167, 167)  # very darker blue/purple
hover_color_for_buttons = (249, 216, 156)
background_color_for_buttons = (130, 196, 195)

# Title and Icon
pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(pygame.image.load("./Resources/game_icon.png"))


def game_main_menu():
    MAIN_MENU = True
    button = ButtonWithText(0, 0, 100, 50,
                            background_color_for_buttons, hover_color_for_buttons, "TEST", (0, 0, 0), 10, 10)
    button2 = ButtonWithImage(
        100, 100, 64, 64, background_color_for_buttons, hover_color_for_buttons, "./Resources/cross_icon.png")
    buttons = [button, button2]

    while MAIN_MENU:
        screen.fill(screen_color)
        # for loop for catching evvents for PyGame
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MAIN_MENU = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for each in buttons:
                    if each.is_over(mouse_position):
                        each.is_clicked()

        # Checking if buttons are hovered over
        # and if yes then change background button color
        for each in buttons:
            if each.is_over(mouse_position):
                each.is_hovered()
            else:
                each.show_button()

        pygame.display.update()


game_main_menu()

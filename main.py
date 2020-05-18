#!/usr/bin/python
import pygame
from config import *
from buttons import *

def game_main_menu():
    MAIN_MENU = True
    button = ButtonWithText(0, 0, 100, 50,
                            background_color_for_buttons, "TEST", (0, 0, 0), 10, 10)
    button2 = ButtonWithImage(
        100, 100, 64, 64, background_color_for_buttons, "./Resources/cross_icon.png")
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


def main_game_loop():
    pass


game_main_menu()

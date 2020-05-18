#!/usr/bin/python
import pygame
from config import *
from buttons import *
from board import *


def game_main_menu():
    '''
    Main Menu function for choosing boards size and games row win
    '''
    main_menu = True
    button_board_size_show = ButtonWithText(350, 357, 100, 64,
                                            background_color_for_buttons, str(Board.get_board_size()), (0, 0, 0), 32, 16)

    button_win_size_show = ButtonWithText(350, 478, 100, 64,
                                          background_color_for_buttons, str(Board.get_row_win()), (0, 0, 0), 32, 16)

    button_board_size_minus = ButtonWithImageMinusBoardSize(
        286, 357, 64, 64, background_color_for_buttons, "./Resources/minus_icon.png")

    button_board_size_plus = ButtonWithImagePlusBoardSize(
        450, 357, 64, 64, background_color_for_buttons, "./Resources/plus_icon.png")

    button_row_size_minus = ButtonWithImageMinusRowWin(
        286, 478, 64, 64, background_color_for_buttons, "./Resources/minus_icon.png")

    button_row_size_plus = ButtonWithImagePlusRowWin(
        450, 478, 64, 64, background_color_for_buttons, "./Resources/plus_icon.png")

    buttons = [button_board_size_minus, button_board_size_plus,
               button_row_size_minus, button_row_size_plus]

    while main_menu:
        screen.fill(screen_color)
        # for loop for catching events for PyGame
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu = False
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

        if button_board_size_show.is_over(mouse_position):
            button_board_size_show.is_hovered(str(Board.get_board_size()))
        else:
            button_board_size_show.show_button(str(Board.get_board_size()))

        if button_win_size_show.is_over(mouse_position):
            button_win_size_show.is_hovered(str(Board.get_row_win()))
        else:
            button_win_size_show.show_button(str(Board.get_row_win()))

        pygame.display.update()


def main_game_loop():
    pass


if __name__ == "__main__":
    game_main_menu()

#!/usr/bin/python
import sys
import pygame
from config import *
from buttons import *
from board import *


def game_main_menu():
    '''
    Main Menu function for choosing boards size and games row win
    '''
    main_menu = True

    button_board_size_show = ButtonWithText(350, 557, 100, 64,
                                            background_color_for_buttons, (0, 0, 0), 32, 16)

    button_win_size_show = ButtonWithText(350, 678, 100, 64,
                                          background_color_for_buttons, (0, 0, 0), 32, 16)

    button_board_size_minus = ButtonWithImageMinusBoardSize(
        286, 557, 64, 64, background_color_for_buttons, "./Resources/minus_icon.png")

    button_board_size_plus = ButtonWithImagePlusBoardSize(
        450, 557, 64, 64, background_color_for_buttons, "./Resources/plus_icon.png")

    button_row_size_minus = ButtonWithImageMinusRowWin(
        286, 678, 64, 64, background_color_for_buttons, "./Resources/minus_icon.png")

    button_row_size_plus = ButtonWithImagePlusRowWin(
        450, 678, 64, 64, background_color_for_buttons, "./Resources/plus_icon.png")

    start = ButtonWithText(
        275, 350, 250, 100, background_color_for_buttons, (0, 0, 0), 75, 35)

    buttons = [button_board_size_minus, button_board_size_plus,
               button_row_size_minus, button_row_size_plus]

    while main_menu:
        screen.fill(screen_color)
        # for loop for catching events for PyGame
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for each in buttons:
                    if each.is_over(mouse_position):
                        each.clicked()

                if start.is_over(mouse_position):
                    main_menu = False

        # Checking if buttons are hovered over
        # and if yes then change background button color
        for each in buttons:
            if each.is_over(mouse_position):
                each.hovered()
            else:
                each.show_button()

        if start.is_over(mouse_position):
            start.hovered("START")
        else:
            start.show_button("START")

        # Checking if buttons that show board_size and row_win
        # are either hovered over or clicked
        if button_board_size_show.is_over(mouse_position):
            button_board_size_show.hovered(str(Board.get_board_size()))
        else:
            button_board_size_show.show_button(str(Board.get_board_size()))

        if button_win_size_show.is_over(mouse_position):
            button_win_size_show.hovered(str(Board.get_row_win()))
        else:
            button_win_size_show.show_button(str(Board.get_row_win()))

        if start.is_over(mouse_position):
            start.hovered("START")
        else:
            start.show_button("START")

        pygame.display.update()


def main_game_loop():
    '''
    Main Game loop. Function where the player is going to play against teh Minimax algorithm
    '''

    board = Setup_board()
    board.draw_board()


if __name__ == "__main__":

    game_main_menu()
    main_game_loop()

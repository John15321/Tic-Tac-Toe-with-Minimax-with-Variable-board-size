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


class Board:
    '''
    This class describes properties of the game board like its size and the number of
    rows required to "paint" in order to win
    '''

    board_size = 1
    row_win = 1

    @classmethod
    def get_board_size(cls):
        '''
        Get board_size value (int)
        It is a @classmethod, meaning you get the class variable value
        '''
        return cls.board_size

    @classmethod
    def get_row_win(cls):
        '''
        Get row_win value (int)
        It is a @classmethod, meaning you get the class variable value
        '''
        return cls.row_win

    @classmethod
    def set_board_size(cls, new_board_size):
        '''
        Set board_size (int)
        It is a @classmethod, meaning you set the class variable value
        '''
        cls.board_size = new_board_size

    @classmethod
    def set_row_win(cls, new_row_win):
        '''
        Set row_win value (int)
        It is a @classmethod, meaning you set the class variable value
        '''
        cls.row_win = new_row_win

    @classmethod
    def increment_board_size(cls):
        '''
        Increment board_size value by 1
        It is a @classmethod, meaning you increment the class variable value
        '''
        cls.board_size += 1

    @classmethod
    def increment_row_win(cls):
        '''
        Increment row_win value by 1
        It is a @classmethod, meaning you increment the class variable value
        '''
        cls.row_win += 1

    @classmethod
    def decrement_board_size(cls):
        '''
        Decrement board_size value by 1
        It is a @classmethod, meaning you decrement the class variable value
        '''
        if (cls.board_size-1) != 0:
            cls.board_size -= 1

    @classmethod
    def decrement_row_win(cls):
        '''
        Decrement row_win value by 1
        It is a @classmethod, meaning you decrement the class variable value
        '''
        if (cls.row_win-1) != 0:
            cls.row_win -= 1

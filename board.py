'''
Python module with Board class. There is going to be only one board therefore it operattes on
class variables.
'''
import pygame
from config import *


class Board:
    '''
    This class describes properties of the game board like its size and the number of
    rows required to "paint" in order to win
    '''

    max_board_size = 8
    min_board_size = 3

    board_size = 3
    row_win = 3

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
        if cls.board_size < cls.max_board_size:
            cls.board_size += 1
            cls.increment_row_win()

    @classmethod
    def increment_row_win(cls):
        '''
        Increment row_win value by 1
        It is a @classmethod, meaning you increment the class variable value
        '''
        if cls.row_win < cls.board_size:
            cls.row_win += 1

    @classmethod
    def decrement_board_size(cls):
        '''
        Decrement board_size value by 1
        It is a @classmethod, meaning you decrement the class variable value
        '''
        if cls.board_size > cls.min_board_size:
            cls.board_size -= 1
            if cls.row_win - 1 == cls.board_size:
                cls.decrement_row_win()

    @classmethod
    def decrement_row_win(cls):
        '''
        Decrement row_win value by 1
        It is a @classmethod, meaning you decrement the class variable value
        '''
        if cls.row_win > cls.min_board_size:
            cls.row_win -= 1

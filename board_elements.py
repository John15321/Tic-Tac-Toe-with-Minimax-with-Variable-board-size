'''
Python module with Board class elements like tiles.
'''
import pygame
import sys
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


class Tile:
    '''
    A class for tiles on game board
    '''

    def __init__(self, x, y, width, height, tile_color, tile_image, padding_x=0, padding_y=0):
        self.x_position = x
        self.y_position = y
        self.width = width
        self.height = height
        self.tile_color = tile_color
        self.hover_color = hover_color_for_buttons
        self.tile_image = pygame.image.load(tile_image)
        self.tile_image = pygame.transform.scale(self.tile_image,
                                                 (self.width, self.height))
        self.padding_x = padding_x
        self.padding_y = padding_y

    def get_position(self):
        '''
        Returns given Tiles positions (x, y)
        '''
        return (self.x_position, self.y_position)

    def show_tile(self, hover_color=(-1, -1, -1)):
        '''
        Function for showing a given button with its set positions and values, etc.
        '''
        if hover_color != (-1, -1, -1):
            pygame.draw.rect(screen, hover_color, (self.x_position,
                                                   self.y_position, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.tile_color, (self.x_position,
                                                       self.y_position, self.width, self.height))

    def hovered(self):
        '''
        Draws the button just like show_button() but  with a different color as background when hovered over
        '''
        pygame.draw.rect(screen, self.hover_color, (self.x_position,
                                                    self.y_position, self.width, self.height))
        screen.blit(self.tile_image, (self.x_position + self.padding_x,
                                      self.y_position + self.padding_y))

    def change_image(self, new_image):
        '''
        Function for changing buttons image, takes local image path
        '''
        self.tile_image = pygame.image.load(new_image)

    def is_over(self, mouse_pos):
        '''
        Function returns a boolean if the mouse while being clicked is over the particular button
        '''
        if mouse_pos[0] > self.x_position and mouse_pos[0] < self.x_position + self.width:
            if mouse_pos[1] > self.y_position and mouse_pos[1] < self.y_position + self.height:
                return True
        else:
            return False

    def clicked(self):
        pass


class TileWithSymbol:
    '''
    A class for tiles with placed symbols
    '''

    def __init__(self, x, y, width, height, tile_color, symbol: str, padding_x=0, padding_y=0):
        self.x_position = x
        self.y_position = y
        self.width = width
        self.height = height
        self.tile_color = tile_color
        self.padding_x = padding_x
        self.padding_y = padding_y

        if symbol == 'x':
            self.tile_image = pygame.image.load(
                "./Resources/cross_icon_100px.png")
            self.tile_image = pygame.transform.scale(self.tile_image,
                                                     (self.width, self.height))
        elif symbol == 'o':
            self.tile_image = pygame.image.load(
                "./Resources/circle_icon_100px.png")
            self.tile_image = pygame.transform.scale(self.tile_image,
                                                     (self.width, self.height))
        else:
            print("Incorrect symbol")

    def show_tile(self, hover_color=(-1, -1, -1)):
        '''
        Function for showing a given button with its set positions and values, etc
        '''
        pygame.draw.rect(screen, self.tile_color, (self.x_position,
                                                   self.y_position, self.width, self.height))
        screen.blit(self.tile_image, (self.x_position + self.padding_x,
                                      self.y_position + self.padding_y))

    def get_position(self):
        '''
        Returns given Tiles positions (x, y)
        '''
        return (self.x_position, self.y_position)

    def hovered(self):
        pass

    def is_over(self, mouse_pos=(0, 0)):
        pass

    def clicked(self):
        pass

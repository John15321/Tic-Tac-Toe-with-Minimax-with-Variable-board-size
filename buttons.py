'''
Module responsible for implementing button mechanics using pygame.
'''
import pygame
from config import *
from board import *


class Button:
    '''
    Parent Button class
    '''

    def __init__(self, x, y, width, height, button_color):
        self.x_position = x
        self.y_position = y
        self.width = width
        self.height = height
        self.button_color = button_color
        self.hover_color = hover_color_for_buttons


class ButtonWithText(Button):
    '''
    A class for text that is contained inside buttons
    '''

    def __init__(self, x, y, width, height, button_color, text, text_color=(0, 0, 0), padding_x=0, padding_y=0):
        super().__init__(x, y,
                         width, height, button_color)
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text_render = self.font.render(self.text, True, self.text_color)
        self.padding_x = padding_x
        self.padding_y = padding_y

    def show_button(self, txt_to_show):
        '''
        Function for showing a given button with its set positions and values, etc.
        '''
        pygame.draw.rect(screen, self.button_color, (self.x_position,
                                                     self.y_position, self.width, self.height))
        screen.blit(self.font.render(txt_to_show, True, self.text_color), (self.x_position +
                                                                           self.padding_x, self.y_position + self.padding_y))

    def is_hovered(self, txt_to_show):
        '''
        Draws the button with a different color as background when hovered over
        '''
        pygame.draw.rect(screen, self.hover_color, (self.x_position,
                                                    self.y_position, self.width, self.height))
        screen.blit(self.font.render(txt_to_show, True, self.text_color),
                    (self.x_position + self.padding_x, self.y_position + self.padding_y))

    def is_over(self, mouse_pos):
        '''
        Function return boolean of if the mouse while being clicked is over the particular button
        '''
        if mouse_pos[0] > self.x_position and mouse_pos[0] < self.x_position + self.width:
            if mouse_pos[1] > self.y_position and mouse_pos[1] < self.y_position + self.height:
                return True
        else:
            return False

    def is_clicked(self):
        '''
        Action after the button is clicked
        '''
        print("Clicked")


class ButtonWithImage(Button):
    '''
    A class for text that is contained inside buttons
    '''

    def __init__(self, x, y, width, height, button_color, button_image, padding_x=0, padding_y=0):
        super().__init__(x, y,
                         width, height, button_color)
        self.button_image = pygame.image.load(button_image)
        self.padding_x = padding_x
        self.padding_y = padding_y

    def show_button(self, hover_color=(-1, -1, -1)):
        '''
        Function for showing a given button with its set positions and values, etc.
        '''
        if hover_color != (-1, -1, -1):
            pygame.draw.rect(screen, hover_color, (self.x_position,
                                                   self.y_position, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.button_color, (self.x_position,
                                                         self.y_position, self.width, self.height))
        screen.blit(self.button_image, (self.x_position +
                                        self.padding_x, self.y_position + self.padding_y))

    def is_hovered(self):
        '''
        Draws the button differently if it is hovered over
        '''
        pygame.draw.rect(screen, self.hover_color, (self.x_position,
                                                    self.y_position, self.width, self.height))
        screen.blit(self.button_image, (self.x_position +
                                        self.padding_x, self.y_position + self.padding_y))

    def change_image(self, new_image):
        '''
        Function for changing buttons image, takes local image path
        '''
        self.button_image = pygame.image.load(new_image)

    def is_over(self, mouse_pos):
        '''
        Function return boolean of if the mouse while being clicked is over the particular button
        '''
        if mouse_pos[0] > self.x_position and mouse_pos[0] < self.x_position + self.width:
            if mouse_pos[1] > self.y_position and mouse_pos[1] < self.y_position + self.height:
                return True
        else:
            return False

    def is_clicked(self):
        '''
        Action after the button is clicked
        '''
        print("Clicked")


class ButtonWithImageMinusBoardSize(ButtonWithImage):
    '''
    Special button class for picking the board size
    '''

    def __init__(self, x, y, width, height, button_color, button_image, padding_x=0, padding_y=0):
        super().__init__(x, y, width, height, button_color,
                         button_image, padding_x=0, padding_y=0)

    def is_clicked(self):
        '''
        Action after the button is clicked
        '''
        Board.decrement_board_size()


class ButtonWithImagePlusBoardSize(ButtonWithImage):
    '''
    Special button class for picking the board size
    '''

    def __init__(self, x, y, width, height, button_color, button_image, padding_x=0, padding_y=0):
        super().__init__(x, y, width, height, button_color,
                         button_image, padding_x=0, padding_y=0)

    def is_clicked(self):
        '''
        Action after the button is clicked
        '''
        Board.increment_board_size()


class ButtonWithImageMinusRowWin(ButtonWithImage):
    '''
    Special button class for picking the board size
    '''

    def __init__(self, x, y, width, height, button_color, button_image, padding_x=0, padding_y=0):
        super().__init__(x, y, width, height, button_color,
                         button_image, padding_x=0, padding_y=0)

    def is_clicked(self):
        '''
        Action after the button is clicked
        '''
        Board.decrement_row_win()


class ButtonWithImagePlusRowWin(ButtonWithImage):
    '''
    Special button class for picking the board size
    '''

    def __init__(self, x, y, width, height, button_color, button_image, padding_x=0, padding_y=0):
        super().__init__(x, y, width, height, button_color,
                         button_image, padding_x=0, padding_y=0)

    def is_clicked(self):
        '''
        Action after the button is clicked
        '''
        Board.increment_row_win()

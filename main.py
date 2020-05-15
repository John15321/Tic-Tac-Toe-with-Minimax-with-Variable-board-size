#!/usr/bin/python

import pygame

# Initializing PyGame
pygame.init()

# screen color (in RGB)
screen_color = (245, 167, 167)  # very darker blue/purple
hover_color_for_buttons = (249, 216, 156)
background_color_for_buttons = (130, 196, 195)

class Button:
    '''
    Parent Button class
    '''

    def __init__(self, x, y,  width, height, button_color):
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

    def __init__(self, x, y,  width, height, button_color, text, text_color=(0, 0, 0), padding_x=0, padding_y=0):
        super().__init__(x, y,
                         width, height, button_color)
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.text_render = self.font.render(self.text, True, self.text_color)
        self.padding_x = padding_x
        self.padding_y = padding_y

    def show_button(self):
        '''
        Function for showing a given button with its set positions and values, etc.
        '''
        pygame.draw.rect(screen, self.button_color, (self.x_position,
                                                     self.y_position, self.width, self.height))
        screen.blit(self.text_render, (self.x_position +
                                       self.padding_x, self.y_position+self.padding_y))

    def is_hovered(self):
        '''
        Draws the button with a different color as background when hovered over
        '''
        pygame.draw.rect(screen, self.hover_color, (self.x_position,
                                                     self.y_position, self.width, self.height))
        screen.blit(self.text_render, (self.x_position +
                                       self.padding_x, self.y_position+self.padding_y))

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
        print("Clicked")


class ButtonWithImage(Button):
    '''
    A class for text that is contained inside buttons
    '''

    def __init__(self, x, y,  width, height, button_color, button_image, padding_x=0, padding_y=0):
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
                                        self.padding_x, self.y_position+self.padding_y))

    def is_hovered(self):
        pygame.draw.rect(screen, self.hover_color, (self.x_position,
                                                    self.y_position, self.width, self.height))
        screen.blit(self.button_image, (self.x_position +
                                        self.padding_x, self.y_position+self.padding_y))

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
        print("Clicked")


# Creating the screen
# screen size (has to be a tuple: width x height)
screen_width = 800
screen_height = 600
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)

# Title and Icon
pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(pygame.image.load("./Resources/game_icon.png"))


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


game_main_menu()

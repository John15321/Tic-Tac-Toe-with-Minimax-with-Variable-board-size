#!/usr/bin/python

import pygame

# Initializing PyGame
pygame.init()


class Button:
    '''
    Parent Button class
    '''

    def __init__(self, x_position, y_position,  width, height, button_color):
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.height = height
        self.button_color = button_color


class ButtonWithText(Button):
    '''
    A class for text that is contained inside buttons
    '''

    def __init__(self, x_position, y_position,  width, height, button_color, text, text_color=(0, 0, 0), padding_x=0, padding_y=0):
        super().__init__(x_position, y_position,
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


class ButtonWithImage(Button):
    '''
    A class for text that is contained inside buttons
    '''

    def __init__(self, x_position, y_position,  width, height, button_color, button_image, padding_x=0, padding_y=0):
        super().__init__(x_position, y_position,
                         width, height, button_color)
        self.button_image = pygame.image.load(button_image)
        self.padding_x = padding_x
        self.padding_y = padding_y

    def show_button(self):
        '''
        Function for showing a given button with its set positions and values, etc.
        '''
        pygame.draw.rect(screen, self.button_color, (self.x_position,
                                                     self.y_position, self.width, self.height))
        screen.blit(self.button_image, (self.x_position +
                                        self.padding_x, self.y_position+self.padding_y))

    def change_image(self, new_image):
        '''
        Function for changing buttons image, takes local image path
        '''
        self.button_image = pygame.image.load(new_image)


# Creating the screen
# screen size (has to be a tuple: width x height)
screen_width = 800
screen_height = 600
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
# screen color (in RGB)
screen_color = (27, 27, 47)  # very darker blue/purple

# Title and Icon
pygame.display.set_caption("Tic Tac Toe")
# <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
pygame.display.set_icon(pygame.image.load("./Resources/game_icon.png"))
# Circle and Cross icons:
# <a target="_blank" href="https://icons8.com/icons/set/multiply">Multiply icon</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
# <a target="_blank" href="https://icons8.com/icons/set/minus">Minus icon</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
# <a target="_blank" href="https://icons8.com/icons/set/minus-math">Subtract icon</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
# <a target="_blank" href="https://icons8.com/icons/set/plus-math">Plus Math icon</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>


def game_main_menu():
    MAIN_MENU = True

    while MAIN_MENU:
        # for loop for catching evvents for PyGame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MAIN_MENU = False

        screen.fill(screen_color)
        button = ButtonWithText(0, 0, 100, 50,
                                (255, 255, 255), "TEST", (0, 0, 0), 10, 10)
        button.show_button()

        button2 = ButtonWithImage(100, 100, 64, 64, screen_color, "./Resources/cross_icon.png")
        button2.show_button()
        pygame.display.update()


game_main_menu()

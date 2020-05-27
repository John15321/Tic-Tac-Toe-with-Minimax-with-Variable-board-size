'''
Python module with Board class. There is going to be only one board therefore it operattes on
class variables.
'''
import pygame
import sys
from config import *
from board_elements import *
from game_mechanics import *


class SetupBoard(GameMechanics):
    '''
    This class sets up game board depending on number of tiles
    '''

    def __init__(self):
        super().__init__(Board.get_board_size())
        self.fields = []
        self.tile_size = (0, 0)
        self.fields = [[0 for j in range(0, Board.get_board_size())] for i in range(
            0, Board.get_board_size())]
        self.tile_size = (int((screen_width / Board.get_board_size()) * 0.8),
                          int((screen_height / Board.get_board_size()) * 0.8))
        offset = (int((screen_width / Board.get_board_size())) - self.tile_size[0],
                  int((screen_height / Board.get_board_size())) - self.tile_size[1])

        for x in range(Board.get_board_size()):
            for y in range(Board.get_board_size()):
                if y == 0 and x == 0:
                    tile_pos_x = int(offset[0] / 2)
                    tile_pos_y = int(offset[1] / 2)
                elif y == 0 and x != 0:
                    tile_pos_x = self.tile_size[0] * x + \
                        int(offset[0] / 2) + offset[0] * x
                    tile_pos_y = int(offset[1] / 2)
                elif y != 0 and x == 0:
                    tile_pos_x = int(offset[0] / 2)
                    tile_pos_y = self.tile_size[1] * y + \
                        int(offset[1] / 2) + offset[1] * y
                else:
                    tile_pos_x = self.tile_size[0] * x + \
                        int(offset[0] / 2) + offset[0] * x
                    tile_pos_y = self.tile_size[1] * y + \
                        int(offset[1] / 2) + offset[1] * y

                self.fields[x][y] = Tile(tile_pos_x, tile_pos_y, self.tile_size[0], self.tile_size[1],
                                         background_color_for_buttons, "./Resources/cross_icon_100px.png")

    def update_board(self):
        '''
        Function reponsible for updating fields of the board
        '''
        for y in range(0, Board.get_board_size()):
            for x in range(0, Board.get_board_size()):
                if self.signs[y][x] != '-':
                    pos = self.fields[x][y].get_position()
                    self.fields[x][y] = TileWithSymbol(pos[0], pos[1], self.tile_size[0],
                                                       self.tile_size[1], background_color_for_buttons, str(self.signs[y][x]))

    def print_board_to_console(self):
        '''
        A simple function that prints the list of current objects on the board
        to the console
        '''
        print("")
        for i in range(len(self.signs)):
            print(self.signs[i])

        print("")

    def draw_board(self):
        '''
        This function draws game board
        '''
        game = True
        while game:
            screen.fill(screen_color)
            # for loop for catching events for PyGame
            mouse_position = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for x in range(Board.get_board_size()):
                        for y in range(Board.get_board_size()):
                            if self.fields[x][y].is_over(mouse_position):
                                self.fields[x][y].clicked()
                                self.signs[y][x] = 'x'
                                self.update_board()
                                self.print_board_to_console()
                                self.check_win('x')
                                # self.minimax()
                                self.update_board()
                                self.check_win('o')

            # self.signs = self.best_move(self.signs)
            # Checking if buttons are hovered over
            # and if yes then change background button color
            for each_sublist in self.fields:
                for each in each_sublist:
                    if each.is_over(mouse_position):
                        each.hovered()
                    else:
                        each.show_tile()

            pygame.display.update()

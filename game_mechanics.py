'''
A module containing Game_Mechanics class that is responsible
for handling game logic.
'''


class Game_Mechanics():

    def __init__(self, board_size):

        self.signs = [[-1 for j in range(0, board_size)]
                      for i in range(0, board_size)]

    def minimax(self):
        pass

'''
TODO:
1. Przekazywac Game_Mechanics stan gry i go ogolnie updatowac
2. Na postawie Game_Mechanics(minimax) zrobic prediction gdzie ma byc ruch O
3. O musi zrobic swoj ruch
4. Aktualizacja planszy
5. Patrzymy czy jest wygrana
6. Graczc robi ruch i sie powtarza



'''

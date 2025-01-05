import os
from random import randint
from tile import Tile, plains, forest, pines, mountain, water, player, town, desa

class Map:
    def __init__(self, width: int, height: int, player):
        self.width = width
        self.height = height
        self.player = player
        self.map = self.generate_map()
        self.overridden_tile = None


        self.map_data: list[list[Tile]]

        self.generate_map()
        self.generate_patch(plains, 5, 5, 7)
        self.generate_patch(forest, 3, 5, 7)
        self.generate_patch(pines, 3, 5, 6)
        self.generate_patch(mountain, 3, 4, 4)
        self.generate_patch(water, 3, 4, 4)
        self.generate_patch(town, 2, 3, 4)
        self.generate_patch(desa, 2, 3, 4)
        self.player_pos = self.load_player_position() if os.path.exists('player_position.txt') else (0, 0)
        self.place_player()

    @staticmethod
    def save_player_position(marker_x, marker_y):
        with open('player_position.txt', 'w') as f:
            f.write(f'{marker_x},{marker_y}')

    @staticmethod
    def load_player_position():
        if not os.path.exists('player_position.txt'):
            with open('player_position.txt', 'w') as f:
                f.write('0,0')
        with open('player_position.txt', 'r') as f:
            marker_x, marker_y = map(int, f.read().split(','))
        return marker_x, marker_y

    def place_player(self) -> None:
        self.map_data[self.player_pos[1]][self.player_pos[0]] = self.player

    def remove_player(self) -> None:
        if self.overridden_tile is not None:
            self.map_data[self.player_pos[1]][self.player_pos[0]] = self.overridden_tile
        self.map_data[self.player_pos[1]][self.player_pos[0]] = plains

    def update_player_pos(self, marker_x: int, marker_y: int) -> None:
        self.overridden_tile = self.map_data[marker_y][marker_x]
        self.remove_player()
        if self.overridden_tile is not None:
            old_x, old_y = self.player_pos
            self.map_data[old_y][old_x] = self.overridden_tile
        self.player_pos = (marker_x, marker_y)
        self.place_player()

    def generate_map(self) -> None:
        self.map_data = [[plains for _ in range(self.width)] for _ in range(self.height)]
        self.save_player_position(0, 0)

    def generate_patch(self, tile, min_size, max_size, num_patches):
        for _ in range(num_patches):
            start_x = randint(0, self.width - max_size - 1)
            start_y = randint(0, self.height - max_size - 1)
            patch_width = randint(min_size, max_size)
            patch_height = randint(min_size, max_size)
            for i in range(patch_height):
                for j in range(patch_width):
                    self.map_data[start_y + i][start_x + j] = tile

    def display_map(self, marker_x: int, marker_y: int) -> None:
        frame = "x" + self.width * "=" + "x"
        print(frame)
        for y, row in enumerate(self.map_data):
            row_tiles = [tile.symbol if (x, y) != (marker_x, marker_y) else "\033[31m" + tile.symbol + "\033[0m" for
                         x, tile in enumerate(row)]
            print("|" + "".join(row_tiles) + "|")
        print(frame)

game_map = Map(60, 20, player)


"""
Platformer Template
"""
import arcade
import numpy as np
from plateau import plateau


DIM = 400

PLAT = plateau(DIM)
PLAT.creer_salle((100, 100), (200, 100))
MATRICE_PLAT = PLAT._plat



BACKGROUND = arcade.color.BLACK
X, Y = 600, 600    
DOOR = "door.PNG"
CORRIDOR = "corridor.PNG"
WALL = "walls.PNG"
        
    
class DOORS(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(DOOR)
        print("door", x, y)
        self.center_x, self.center_y = x, y

class CORRIDORS(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(CORRIDOR)
        self.center_x, self.center_y = x, y

class WALLS(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(WALL)
        self.center_x, self.center_y = x, y

        
class Window(arcade.Window):
    
    def __init__(self):
        super().__init__(X, Y, "Donjon")
        arcade.set_background_color(BACKGROUND)
        
        self.walls = arcade.SpriteList()
        self.doors = arcade.SpriteList()
        self.corridors = arcade.SpriteList()


    def setup(self):
        print(np.argwhere(MATRICE_PLAT ==1))
        for coord in np.argwhere(MATRICE_PLAT == 1):
            self.walls.append(WALLS(coord[0], coord[1]))
        
        for coord in np.argwhere(MATRICE_PLAT == 2):
            self.doors.append(DOORS(coord[0], coord[1]))
        
        for coord in np.argwhere(MATRICE_PLAT == 3):
            self.corridors.append(CORRIDORS(coord[0], coord[1]))

    def on_draw(self):
        arcade.start_render()
        self.walls.draw()
        self.corridors.draw()
        self.doors.draw()

window = Window()
window.setup()
arcade.run()
"""
Platformer Template
"""
import arcade
import numpy as np
from plateau import plateau
import matplotlib.pyplot as plt
import resize


DIM = 400

p = plateau(DIM)
p.creer_salle((10, 10), (100, 100))
p.creer_salle((260, 170), (100, 100))
p.inserer_porte((110, 60))
p.inserer_porte((260, 200))
#p.generer_salles(5)
p.generer_couloir((110, 60), (260, 200))
MATRICE_PLAT = p._plat



BACKGROUND = arcade.color.BLACK
X, Y = 600, 600    
DOOR = "blanc.PNG"
CORRIDOR = "violet.png"
WALL = "jaune.png"
INT = "orange.png" 
MINION = "soup3.png"       
    
class DOORS(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(DOOR)
        print("door", x, y)
        self.center_x, self.center_y = x, y

class HERO(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(MINION)
        print("minion", x, y)
        self.center_x, self.center_y = x, y

class CORRIDORS(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(CORRIDOR)
        self.center_x, self.center_y = x, y

class WALLS(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(WALL)
        self.center_x, self.center_y = x, y

class INTS(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(INT)
        self.center_x, self.center_y = x, y

        
class Window(arcade.Window):
    
    def __init__(self):
        super().__init__(X, Y, "Donjon")
        arcade.set_background_color(BACKGROUND)
        
        self.walls = arcade.SpriteList()
        self.doors = arcade.SpriteList()
        self.corridors = arcade.SpriteList()
        self.interiors = arcade.SpriteList()
        self.hero = arcade.SpriteList()


    def setup(self):
        for coord in np.argwhere(MATRICE_PLAT == 1):
            self.walls.append(WALLS(coord[0], coord[1]))
        
        for coord in np.argwhere(MATRICE_PLAT == 2):
            print("coords")
            self.doors.append(DOORS(coord[0], coord[1]))
        
        for coord in np.argwhere(MATRICE_PLAT == 3):
            self.corridors.append(CORRIDORS(coord[0], coord[1]))

        for coord in np.argwhere(MATRICE_PLAT == 4):
            self.interiors.append(INTS(coord[0], coord[1]))

        self.hero.append(HERO(100,100))

    def on_draw(self):
        arcade.start_render()
        self.walls.draw()
        self.corridors.draw()
        self.doors.draw()
        self.interiors.draw()
        self.hero.draw()

        

window = Window()
window.setup()
arcade.run()
"""
Platformer Template
"""
#import des modules de base
import arcade
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import random as rd

#imports de notre code
import perso as Pe
import interface_user as I
import plateau as Pl
import objects as O


DIM = 400

p = Pl.Plateau(DIM)
p.creer_salle((10, 10), (100, 100))
p.creer_salle((260, 170), (100, 100))
p.inserer_porte((100, 60))
p.inserer_porte((260, 200))
# p.generer_salles(5)
p.generer_couloir((100, 60), (260, 200))
MATRICE_PLAT = p._plat



BACKGROUND = arcade.color.BLACK
X, Y = 600, 600    
DOOR = "blanc.PNG"
CORRIDOR = "violet.png"
WALL = "jaune.png"
        
    
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
            print("coords")
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

if __name__ == "main":
    doors = DOORS()
    window = Window()
    walls = WALLS()
    corridors = CORRIDORS()

    perso = Pe.Perso()
    #val= Pe.Monster()

    plateau = Pl.Plateau()

    #initialisation
    pos_init = (random.randrange(X), random.randrange(Y))



    """
    initialiser
    pos_init = 

    demander le nom du joueur 
    afficher tableau ...
    
    while perso vivant : 
        """
    pass
import interface_user
import random as rd

class Perso():
    def __init__(self, name, position, vie, attaque):
        self.name = name
        self.vie = vie
        self.attaque = attaque
        self.vivant = (self.vie > 0)
        self.position = position
        self.vivant = True
        self.position = (0, 0)
        self.bag = dict()
    
    def nouvelle_direction (self, MainGame, key, plateau):
        new_pos = self.position + interface_user.Maingame().on_key_press(key)
        if new_pos in (plateau.get_plat() >= 3 ) :
            self.position = new_pos

    def variation_vie(self, pdv):
        self.vie += pdv
    
    def variation_attaque(self, pdf):
        self.attaque += pdf

    

class monster():
    "valérie, le monstre qui va vite"
    "Thierry, le monstre qui tape fort"
    def __init__(self, name, position, figure, force, vie, speed):
        self.name = name
        self.figure = figure
        self.force = force
        self.vie = vie
        self.vivant = (self.vie > 0)
        self.position = position
        self.speed = speed

    def __repr__(self):
        print(f"le monstre a {self.vie} points de vie et {self.force} points d'attaque")
    
    def follow(self, player):
        if abs(self.position[0]-player.position[0]) + abs(self.position[1] - player.position[1]) == 1:
            #follow
            pass
    
    def move(self, plateau):
        "de simples allers retours pour l'instant"
        while self.vivant :
            while self.position in (plateau == 2):
                self.position[0] += 1
            self.position[0] -=1
            while self.position in (plateau==2): 
                self.position -= 1

#combat : rapport de force; points d'attaque = points de vie en gros

def attaque_combat(vie, attaque):
    vie -= attaque











"""
Platformer Template
"""


import arcade
import numpy as np
from plateau import plateau
import matplotlib.pyplot as plt


DIM = 400

p = plateau(DIM)
p.creer_salle((10, 10), (100, 100))
p.creer_salle((260, 170), (100, 100))
p.inserer_porte((110, 60))
p.inserer_porte((260, 200))
# p.generer_salles(5)
p.generer_couloir((110, 60), (260, 200))
MATRICE_PLAT = p._plat



BACKGROUND = arcade.color.BLACK
X, Y = 600, 600    
DOOR = "blanc.PNG"
CORRIDOR = "violet.png"
WALL = "jaune.png"
INT = "orange.png" 
CHAR = "soup3.png"      

class CHARACTER(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(CHAR)
        self.center_x, self.center_y = x, y


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
        self.character = CHARACTER(50, 50)


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

    def on_draw(self):
        arcade.start_render()
        self.walls.draw()
        self.corridors.draw()
        self.doors.draw()
        self.interiors.draw()
        self.character.draw()
        

window = Window()
window.setup()
arcade.run()

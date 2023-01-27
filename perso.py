import interface_user

class Perso():
    def __init__(self, name, position, vie, attaque, bag):
        self.name = name
        self.vie = vie
        self.attaque = attaque
        self.vivant = True
        self.position = position
        self.bag = dict()
    
    def nouvelle_direction (self, MainGame, key, plateau):
        new_pos = self.position + interface_user.Maingame().on_key_press(key)
        if new_pos in (plateau.get_plat() !=1 ):
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
        self.vivant = True
        self.position = position
        self.speed = speed

    def __repr__(self):
        print(f"le monstre a {self.vie} points de vie et {self.force} points d'attaque")
    
    def follow(self, player):
        if abs(self.position[0]-player.position[0]) + abs(self.position[1] - player.position[1]) == 1:
            #follow
            pass


#combat : rapport de force; points d'attaque = points de vie en gros

def attaque_perso_combat(monster, Perso):
    monster.vie -= Perso.attaque()
    
def attaque_monster_combat(monster, Perso):
    Perso.variation_vie(-monster.force)


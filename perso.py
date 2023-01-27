class Perso():
    def __init__(self, name, position, vie, attaque, bag):
        self.name = name
        self.vie = vie
        self.attaque = attaque
        self.vivant = True
        self.position = position
        self.bag = dict()
    
    def nouvelle_direction (self, MainGame, symbol):
        self.position += Maingame.user_direction(symbol)

    def variation_vie(self, pdv):
        self.vie += pdv
    
    def variation_attaque(self, pdf):
        self.attaque += pdf

    

class monster():
    def __init__(self, name, position, figure, force, vie):
        self.name = name
        self.figure = figure
        self.force = force
        self.vie = vie
        self.vivant = True
        self.position = position   

    def __repr__(self):
        print(f"le monstre a {self.vie} points de vie et {self.force} points d'attaque")

#combat : rapport de force; points d'attaque = points de vie en gros

def attaque_perso_combat(monster, Perso):
    monster.vie -= Perso.attaque()
    
def attaque_monster_combat(monster, Perso):
    Perso.variation_vie(-monster.force)


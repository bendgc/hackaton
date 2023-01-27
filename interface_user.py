import arcade as arc
import perso as P

def near(pos1, pos2):
    if abs(pos1[0]-pos2[0]) + abs(pos1[1]+pos2[1]) == 1 : 
        return True

class MainGame : 
    def __init__(self, width, height):
        self.width = width
        self.height = height
        arc.set_background_color(arc.color.AMAZON)

    def on_key_press(self, key):
        "returns the direction wanted by the player"
        dir = None
        if key == arc.KEY.up:
            dir = (0, -1)
        if key == arc.KEY.down : 
            dir = (0, 1)
        if key == arc.KEY.left : 
            dir= (-1, 0)
        if key == arc.KEY.right : 
            dir = (1, 0)
        return dir

    def fight_monster(self, key, player, monster):
        if monster.position == player.position : 
            P.attaque_perso_combat(player, monster)
        if near(player.position, monster.position):
            if key == arc.KEY.SPACE :
                P.attaque_monstre_perso(player, monster)

    def on_draw(self, player):
        "display life and strenght"
        arc.draw_text('Life :- '+ str(player.vie),150.0,500.0,
                         arc.color.RED, 20, 180, 'left')
        arc.draw_text('Strenght :- '+ str(player.force),150.0,500.0,
                         arc.color.BLUE, 20, 180, 'left')
    
    
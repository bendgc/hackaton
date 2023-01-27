import arcade as arc
import pygame as pg

def near(pos1, pos2):
    if abs(pos1[0]-pos2[0]) + abs(pos1[1]+pos2[1]) == 1 : 
        return True

class MainGame : 
    def __init__(self, width, height):
        self.width = width
        self.height = height
        arc.set_background_color(arc.color.AMAZON)
        
    """def player_pygame(self):
        "returns the direction wanted by the player"
        dir = None
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.stop() #GAME OVER
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        self.stop()
                    elif event.key == pg.K_UP :
                        dir = (0,-1) #the graph is upside down
                    elif event.key == pg.K_DOWN :
                        dir = (0,1)
                    elif event.key == pg.K_LEFT :
                        dir = (-1,0)
                    elif event.key == pg.K_RIGHT :
                        dir = (1,0)
        return dir """

    def user_dir(self, key):
        "return the direction wanted by the player"
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
            attaque_perso_combat(player, monster)
        if near(player.position, monster.position):
            if key == arc.KEY.SPACE :
                attaque_monstre_perso(player, monster)
            
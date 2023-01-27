import numpy as np

class plateau :

    def __init__(self, dim) :
        self._dim = dim
        self._plat = np.zeros((self._dim,self._dim))

    def creer_salle(self, origine, dim) :
        self._plat[origine[0],origine[1]:origine[1]+dim[1]] = 1
        self._plat[origine[0]+dim[0]-1,origine[1]:origine[1]+dim[1]] = 1
        self._plat[origine[0]:origine[0]+dim[0],origine[1]] = 1
        self._plat[origine[0]:origine[0]+dim[0],origine[1]+dim[1]-1] = 1

    def inserer_porte(self, loc) :
        if self._plat[loc] == 1 :
            self._plat[loc] = 2

    def afficher(self) :
        print(self._plat)



p = plateau(20)
p.creer_salle((1,1),(5,5))
p.creer_salle((6,7),(4,5))
p.afficher()


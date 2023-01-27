import numpy as np
import matplotlib.pyplot as plt

class plateau :

    def __init__(self, dim) :
        self._dim = dim
        self._plat = np.zeros((self._dim,self._dim), dtype=int)

    def creer_salle(self, origine, dim) :
        self._plat[origine[0],origine[1]:origine[1]+dim[1]] = 1
        self._plat[origine[0]+dim[0]-1,origine[1]:origine[1]+dim[1]] = 1
        self._plat[origine[0]:origine[0]+dim[0],origine[1]] = 1
        self._plat[origine[0]:origine[0]+dim[0],origine[1]+dim[1]-1] = 1
        self._plat[origine[0]+1:origine[0]+dim[0]-1,origine[1]+1:origine[1]+dim[1]-1] = 4

    '''def generer_salles(self, n) :
        for i in range(n) :
            loc = (np.random.randint(0,self._dim - 3), np.random.randint(0,self._dim - 3))
            while self._plat[loc] != 0 :
                loc = (np.random.randint(0,self._dim - 3), np.random.randint(0,self._dim - 3))
            dim = (np.random.randint(3,10), np.random.randint(3,10))
            j = 0
            while self._plat[loc[0],loc[1]+j] != 1 :
                j+= 1'''




    def inserer_porte(self, loc) :
        if self._plat[loc] == 1 :
            self._plat[loc] = 2

    def afficher(self) :
        plt.imshow(self._plat)
        plt.show()

'''p = plateau(20)
p.creer_salle((1,1),(5,5))
p.creer_salle((6,7),(4,5))
p.inserer_porte((1,1))
p.afficher()
'''


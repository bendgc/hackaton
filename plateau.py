import numpy as np
import matplotlib.pyplot as plt


class Plateau:

    def __init__(self, dim):
        self._dim = dim
        self._plat = np.zeros((self._dim, self._dim), dtype=int)

    def get_plat(self):
        return self._plat

    def creer_salle(self, origine, dim):
        self._plat[origine[0], origine[1]:origine[1]+dim[1]] = 1
        self._plat[origine[0]+dim[0]-1, origine[1]:origine[1]+dim[1]] = 1
        self._plat[origine[0]:origine[0]+dim[0], origine[1]] = 1
        self._plat[origine[0]:origine[0]+dim[0], origine[1]+dim[1]-1] = 1
        self._plat[origine[0]+1:origine[0]+dim[0] -
                   1, origine[1]+1:origine[1]+dim[1]-1] = 4

    def generer_salles(self, n):
        for i in range(n):
            loc = (np.random.randint(0, self._dim - 3),
                   np.random.randint(0, self._dim - 3))
            while self._plat[loc] != 0:
                loc = (np.random.randint(0, self._dim - 3),
                       np.random.randint(0, self._dim - 3))
            dim = [np.random.randint(3, self._dim//2),
                   np.random.randint(3, self._dim//2)]
            j = -1
            test = True
            while test and j < dim[1]:
                j += 1
                if self._plat[loc[0], loc[1]+j] == 1:
                    test = False
                if loc[1]+j+1 == self._dim:
                    test = False
            if not test:
                dim[1] = j
            j = -1
            test = True
            while test and j < dim[0]:
                j += 1
                if self._plat[loc[0]+j, loc[1]] == 1:
                    test = False
                if loc[0]+j+1 == self._dim:
                    test = False
                    j -= 1
            if not test:
                dim[0] = j
            self.creer_salle(loc, dim)

    def inserer_porte(self, loc):
        if self._plat[loc] == 1:
            self._plat[loc] = 2

    def generer_couloir(self, porte1, porte2):
        dx = porte2[0] - porte1[0]
        dy = porte2[1] - porte1[1]
        if dx > 0:
            mx = 1
        else:
            mx = -1
        if dy > 0:
            my = 2
        else:
            my = -2
        l = [mx for k in range(dx)] + [my for k in range(dy)]
        np.random.shuffle(l)
        i, j = porte1
        for mouv in l:
            if mouv == 1:
                i += 1
            elif mouv == -1 : 
                i -= 1
            elif mouv == 2:
                j += 1
            elif mouv == -2:
                j -= 1
            self._plat[i,j] = 3

    def afficher(self):
        plt.imshow(self._plat)
        plt.show()


p = Plateau(50)
p.creer_salle((1, 1), (10, 10))
p.creer_salle((26, 17), (10, 10))
p.inserer_porte((10, 6))
p.inserer_porte((26, 20))
# p.generer_salles(5)
p.generer_couloir((10, 6), (26, 20))
p.afficher()

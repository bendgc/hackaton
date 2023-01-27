import numpy as np

class plateau :

    def __init__(self, dim) :
        _dim = dim
        plat = np.zeros((_dim,_dim))
        plat[0][0] = ','

        
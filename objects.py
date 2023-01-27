from random import randint 

class Object:
    
    cara = {'sword' : '!', 'bow' : ')', 'gold' : '*',
     'potion' : 'j', 'food' : 'f', 'water' : 'w', 'armor' : 'a'}
    
    
    def __init__(self, name, position, value = 1):
        self.position = position
        self.name = name
        self.value = value

    def stack(self, bag):
        if self.name not in bag and self.name != 'potion': 
            bag[self.name] = self.value 
        elif self.name == 'potion' and 'potions' not in bag :
            bag['potions'] = {'potion1' : self.value}
        elif self.name == 'potion' and 'potions' in bag :
            n = len(bag['potions'])
            bag['potions'][f"potion{n+1}"] = self.value
        else : 
            if self.name in ['sword', 'bow', 'armor']:
                if self.value > bag[self.name] :
                    bag[self.name] = self.value
            else :
                bag[self.name] += self.value
    

    def __repr__(self):
        cara = {'sword' : '!', 'bow' : ')', 'gold' : '*',
     'potion' : 'j', 'food' : 'f', 'water' : 'w', 'armor' : 'a'}
        return(cara[self.name])


def generate_obj(coordinates):
    obj = ['sword', 'bow', 'gold', 'potion', 'food', 'water', 'armor']
    xmin, xmax, ymin, ymax = coordinates
    x = randint(xmin, xmax)
    y = randint(ymin, ymax)
    i = randint(0,len(obj)-1) 
    ob = obj[i]
    if ob == 'potion' :
        value = (randint(-5,5), randint(-5,5))
    else : 
        value = randint(1, 8)
   
    return(Object(ob, (x, y),value))



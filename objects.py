
class Object:
    
    cara = {'sword' : '!', 'bow' : ')', 'gold' : '*',
     'potion' : 'j', 'food' : 'f', 'water' : 'w', 'armor' : 'a'}
    
    
    def __init__(self, position, name, value = 1):
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
        global cara
        return(cara[self.name])



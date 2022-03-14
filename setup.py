
class Type:
    def __init__(self, name:str, double:list[str], half:list[str], zero:list[str]):
        self.name = name
        self.double = double
        self.half = half
        self.zero = zero

class Move:
    def __init__(self, name:str, ps:str, moveType:Type, damage:int):
        self.name = name
        self.ps = ps
        self.type = moveType
        self.damage = damage

class Pokemon:
    def __init__(self, name:str, sprite, types:list[Type], moves:list[Move], stats:list):
        self.name = name
        self.sprite = sprite
        self.types = types  #[type1, type2]
        self.moves = moves  #[move1, move2, move3, move4]
        self.stats = stats  #[hp, attack, dedence, spAttack, spDefence, speed]

    def attack(self, opponent, chosenMove):
        if len(opponent.types) == 1:
            multiplier = calculateType(chosenMove.type, opponent.types[0])
        elif len(opponent.types) == 2:
            multiplier = calculateType(chosenMove.type, opponent.types[0]) * calculateType(chosenMove.type, opponent.types[1])
        
        if chosenMove.ps == "physical":
            damage = int(multiplier * ( ( 6*chosenMove.damage*self.stats[1] / (opponent.stats[2]*50) ) + 2 ))
        elif chosenMove.ps == "special":
            damage = int(multiplier * ( ( 6*chosenMove.damage*self.stats[3] / (opponent.stats[4]*50) ) + 2 ))
        
        opponent.stats[0] = opponent.stats[0] - damage

def searchType(myList:list[str], othersType:str):
    tempBool = False
    for i in myList:
        if othersType == i:
            tempBool = True
            break
    return tempBool

def calculateType(player:Type, opponent:Type):
    if searchType(player.zero, opponent.name): return 0
    elif searchType(player.double, opponent.name): return 2
    elif searchType(player.half, opponent.name): return 0.5
    else: return 1
from random import randint

# Soldier

class Soldier:

    def __init__(self, health, strength):
        # add code here
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage

    pass

# Viking


class Viking(Soldier):

    def __init__(self, name, health, strength):

        Soldier.__init__(self, health, strength)

        self.name = name
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):

        self.health = self.health - damage

        if self.health >= 1:

            return (f'{self.name} has received {damage} points of damage')

        elif self.health <= 0:

            return (f'{self.name} has died in act of combat')
    
    def battleCry(self):

        return 'Odin Owns You All!'


    pass

# Saxon


class Saxon(Soldier):

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage (self, damage):

        self.health = self.health - damage

        if self.health >= 1:

            return (f'A Saxon has received {damage} points of damage')

        elif self.health <= 0:

            return('A Saxon has died in combat')



    pass

# War


class War:


    def __init__(self):

        self.vikingArmy = []

        self.saxonArmy = []

    def addViking(self, Viking):

        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):

        self.saxonArmy.append(Saxon)
 
    def vikingAttack(self):

        v = randint(0, len(self.vikingArmy))

        s = randint(0, len(self.saxonArmy))

        a =  self.saxonArmy[s].receiveDamage(self.vikingArmy[v].attack())
        
        if self.saxonArmy[s].health <= 0: 
            self.saxonArmy.pop(s)
            
        return a

    def saxonAttack(self):

        v = randint(0, len(self.vikingArmy))

        s = randint(0, len(self.saxonArmy))

        b =  self.vikingArmy[v].receiveDamage(self.saxonArmy[s].attack())

        
        if self.vikingArmy[v].health <= 0:
            self.vikingArmy.pop(v)
                
        return b
    
    def showStatus(self):

        if self.saxonArmy == None:
            return 'Vikings have won the war of the century'
        
        elif self.vikingArmy == None:
            return 'Saxon have won the war of the century'

        elif self.saxonArmy and self.vikingArmy >= 1:
            return 'Vikings and Saxons are still in the thick of battle'








    pass

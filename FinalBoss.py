import random
import time
import SimpleGUICS2Pygame as simplegui

class Character:
    def __init__(self,health):
        self.health = health

    def attack(self,other):
        raise NotImplementedError

class Player(Character):
    def __init__(self, health=100):
        super().__init__(health)

    def attack(self, other):
        answer = input("what move would you like to make(punch (p), kick (k), headbutt (h)?)")
        if answer.lower() in ('p' , 'k' , 'h'):
            other.health -= int(random.randint(1, 100) /
                                (random.uniform(0,1) * other.defense))
            # the else part is if the user inputs something other than punch, kick or headbutt
        else:
            print("you stumble...")

class Enemy(Character):
    def __init__(self, name, strength, defense, health):
        super().__init__(health)
        self.name = name
        self.strength = strength
        self.defense = defense

    def attack(self, other):
        # {0.name} is the enemies name
        print("The {0.name} attacks...".format(self))
        other.health -= int(self.strength * random.uniform(0.1, 1.4))



def battle(player, enemy):
    print ("An enemy {0.name} appears...".format(enemy))
    # Combat loop; between the battle keeping track of the health
    while player.health > 0 and enemy.health > 0:
        player.attack(enemy)
        print("The health of the {0.name} is now {0.health}.".format(enemy))
        if enemy.health <= 0:
            break
        enemy.attack(player)
        print("Your health is now {0.health}.".format(player))
    # Display outcome
    if player.health > 0:
        print("You killed the {0.name}.".format(enemy))
    elif enemy.health > 0:
        print("The {0.name} killed you.".format(enemy))


def start():
    battle(Player(), Enemy("Donald Trump", 10, 5, 100))
    # random.choice means it will randomly choose the enemies.
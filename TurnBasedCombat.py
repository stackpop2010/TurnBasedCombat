"""
description:
A simple text based Final Fantasy 1 style turn based combat. I built this practice using dictionaries, random numbers, and functions that call other functions.

to do:
1) add arguments so you don't fight high level enemies too early
2) add arguments so you don't go over max hp with potions
3) add arguments so speed factors who attacks first
4) read up and understand global variables better to make sure I'm not overusing them
5) add more levels to leveling system
6) add more monsters and bosses
7) add options to buy armor, weapons, and elixirs

"""



import random
enemy = ['Goblin', 'Lizard','Skeleton', 'Pirate', 'Sahagin', 'Green Slime', 'Mummy', 'Ochu', 'Bloody Eye', 'Pharoh', 'Wolf', 'Cobra']
enemyHP = dict()
enemyAttack = dict()
enemyEXP=dict()
enemyGold=dict()
enemyHP ={'Goblin': 8, 'Lizard': 92,'Skeleton': 10, 'Pirate': 24, 'Sahagin': 28, 'Green Slime': 24, 'Mummy': 80, 'Ochu': 28, 'Bloody Eye': 720, 'Pharoh': 1220, 'Wolf': 20, 'Cobra': 56}
enemyAttack ={'Goblin': 4, 'Lizard': 18, 'Skeleton': 10, 'Pirate': 10, 'Sahagin': 10, 'Green Slime': 1, 'Mummy': 30, 'Ochu': 20, 'Bloody Eye': 100, 'Pharoh': 75, 'Wolf': 8, 'Cobra': 6}
enemyEXP ={'Goblin': 6, 'Lizard': 153, 'Skeleton': 9 , 'Pirate': 40, 'Sahagin': 30, 'Green Slime': 84, 'Mummy': 300, 'Ochu': 1224, 'Bloody Eye': 2000, 'Pharoh': 1542, 'Wolf': 24, 'Cobra':123}
enemyGold ={'Goblin': 6, 'Lizard': 50, 'Skeleton': 3, 'Pirate': 40, 'Sahagin': 30, 'Green Slime': 20, 'Mummy': 300, 'Ochu': 102, 'Bloody Eye': 2, 'Pharoh': 1542, 'Wolf': 6, 'Cobra':50}
gold = 0
xp = 0
level = 1
round = 1

print('Welcome to Penultimate Reality\n')
def combatClassAssign():
    global combatClass
    combatClass =input('Choose a class: \'a\' for red mage, \'b\' for fighter, and \'c\' for theif: ')
    if combatClass == 'a' or combatClass == 'A'or combatClass == 'b' or combatClass == 'B' or combatClass == 'c' or combatClass == 'C':
        if combatClass == 'a' or combatClass == 'A':
                print('Welcome Red Mage!\n')
        elif combatClass == 'b' or combatClass == 'B' :
                print('Welcome Fighter!\n')
        elif combatClass == 'c' or combatClass == 'C' :
                print('Hmm I don\'t see any theives around here...\n')
    else:
        print('Invalid input, choose wisely Warrior of Reality!')
        combatClassAssign()
    return combatClass;


def statsAssign():
    global hp
    hp=0
    global mp
    mp=0
    global speed
    speed=0
    if combatClass == 'a' or combatClass =='A':
        hp = hp + (random.randint(40, 60))
        mp = mp + (random.randint(60, 100))
        speed = speed + (random.randint(15, 20))

    elif combatClass== 'b' or combatClass == "B":
        hp = hp + (random.randint(60, 100))
        mp = mp + (random.randint(0, 5))
        speed = speed + (random.randint(0, 15))

    elif combatClass== 'c' or combatClass == "C":
        hp = hp + (random.randint(45, 75))
        mp = mp + (random.randint(0, 5))
        speed = speed + (random.randint(15, 25))

    return hp, mp, speed;

combatClass=combatClassAssign()
hp, mp, speed =statsAssign()
print('hp is', hp, '\nmp is', mp, '\nspeed is', speed)
print('\nLet\'s fight!')

def combat():
    global hp
    global mp
    global speed
    global dmg
    global enHP
    global round
    global gold
    global xp
    print('hp is currently', hp, 'mp is', mp)
    print('\tRound', round,'!')
    if hp <= 0:
        print('GAME OVER')
        exit()
    else:
        x = random.choice(enemy)
        print('You encounter a(n)', x )
        enHP = enemyHP[x]
        while enHP > 0 and hp > 0:
            dmg = attack()
            enHP = enHP - dmg
            print('Enemy', x, 'attacks for', enemyAttack[x])
            hp = hp - enemyAttack[x]
            if hp <= 0:
                print('GAME OVER')
                exit()
            else:
                print('You have', hp, 'hp left')
            if enHP <= 0:
                print('Victory! You have defeated', x)
                gold = gold + enemyGold[x]
                xp = xp + enemyEXP[x]
    xpCheck()
    round = round +1
    combat()

def attack():
    global hp
    global mp
    global speed
    global dmg
    global combatClass
    if combatClass == 'a' or combatClass == 'A':
        if mp >= 3:
            dmg = (random.randint(6,7))*level
            print('You cast for', dmg, 'damage')
            mp = mp - 3
            return mp;
        if mp < 3:
            dmg = (random.randint(1,3))*level
            print('Out of MP, you swing wildly for', dmg, 'damage')
    elif combatClass == 'b' or combatClass == 'B':
        dmg = (random.randint(5,7))*level
        print('You swing for', dmg, 'damage')
    elif combatClass == 'c' or combatClass == 'C':
        dmg = (random.randint(4,6))*level
        print('You hit for', dmg, 'damage')
    return dmg;

def xpCheck():
    global hp
    global mp
    global speed
    global level
    if xp <= 27:
        level = 1
    elif xp >28 and xp <84:
        level = 2
        hp = hp+5
        mp = mp +2
        speed = speed +1
    elif xp >=84 and xp <196:
        level = 3
        hp = hp+5
        mp = mp +2
        speed = speed +1
    elif xp >=196 and xp <392:
        level = 4
        hp = hp+5
        mp = mp +2
        speed = speed +1
    if hp >100:
        hp = 100
    if mp > 50:
        mp = 50
    print('level is', level, 'hp is', hp, 'mp is', mp,'speed is', speed)
    print('you have', gold, 'gold. your total xp is',xp)
    usePotion =input('would you like to buy a potion y/n for 20 gold?')
    if usePotion == 'y' or usePotion =='Y' or usePotion =='n' or usePotion=='N':
        if gold >= 20:
            print('Potion restores HP to', (hp+20))
        else:
            print('Sorry, insufficent funds, next round')
    else:
        print('Invalid input, answer with single letter')
        xpCheck()
    return hp, mp, speed;


combat()

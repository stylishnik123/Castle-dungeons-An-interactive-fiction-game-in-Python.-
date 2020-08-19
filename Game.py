from os import system
from random import randint

gametitle="Castle Dungeons - an interactive story game"
system("mode 110,30")
system("title "+gametitle)

def cls():
    system ('cls')

character_name = None
character_race = None
character_class = None
character_strength = None
character_magic = None
character_dexterity = None
character_life = None

cls()
print("Castle dungeons - An interactive fiction game in Python.")

def Intro():
    print("")
    print("In this adventure, you are the hero.")
    print("Your choices, skills, and a bit of luck, will influence the outcome of the game.")
    print("")
    print("An evil sorcerer is holding your fellow adventurers prisoners.")
    print("Will you succeed to free your friends from the castle dungeons, or peril trying?")
    print(" ")
    input("Press Enter to start...")

Intro()

def create_character():
    cls()
    global character_name
    character_name=input("""
    Let's begin by creating your character.
    What is your character name?

    >  """)
    global character_race
    while character_race is None:
        race_choice=input("""
        Choose your character race from the list below by entering the relevant number:
        1 - Elf
        2 - Dwarf

        > """)
        if race_choice=="1":
            character_race="Elf"
        elif race_choice=="2":
            character_race="Dwarf"
        else:
             print("Not a valid choice, try again")
    cls()
    global character_class
    while character_class is None:
        class_choice=input("""
        Choose your character class from the list below by entering the relevant number:
        1 - Warrior
        2 - Wizard

        > """)
        if class_choice=="1":
            character_class="Warrior"
        elif class_choice=="2":
            character_class="Wizard"
        else:
             print("Not a valid choice, try again")

create_character()

def create_character_skill_sheet():
    cls()
    global character_name, character_class,character_race,character_strength,character_magic,character_dexterity,character_life
    print("""
    Now let's determine your character's skills, which you will use throughout the game.
    In this game, your character has four skills:

    - Strength, which you will use in combat or any strength test
    - Dexterity, which you will use in any ability test
    - Magic, which you will use whenever you need to cast a spell or use/inspect a magical item or place
    - Life, which determines your life energy, points will be lost when hurt,
      and whenever Life reaches 0, your character dies.


    Depending on your race and class, you will have a certain point-base already calculated by the game.
    You will shortly be able to increase your skills by rolling a 6-face die.

    Here is your base Character Skills Sheet:
    """)
    character_strength=5
    character_magic=0
    character_dexterity=3
    character_life=10
    if character_race=="Elf":
        character_strength=character_strength+3
        character_magic=character_magic+6
        character_dexterity=character_dexterity+4
        character_life=character_life+2
    elif character_race=="Dwarf":
        character_strength=character_strength+5
        character_life=character_life+4
    if character_class=="Warrior":
        character_strength=character_strength+3
        character_life=character_life+3
    elif character_race=="Wizard":
        character_magic=character_magic+4

    print("""
    Name:"""+character_name+
    """
    Race:"""+character_race+
    """
    Class:"""+character_class+
    """

    Strength:"""+str(character_strength)+
    """
    Dexterity:"""+str(character_dexterity)+
    """
    Magic:"""+str(character_magic)+
    """
    Life:"""+str(character_life)+"""

    """)
    input("Press Enter to apply your skills modifiers")

create_character_skill_sheet()

def modify_skills():
    cls()
    global character_strength,character_magic, character_dexterity, character_life
    print("To modify your skills, roll a six face die for each of your skills, and the game will add your score to the relevant skill")
    input("Press Enter to roll for Strength")
    roll=randint(1,6)
    print("You rolled: "+str(roll))
    character_strength = character_strength + roll
    input("Press Enter to roll for Dexterity")
    roll=randint(1,6)
    print("You rolled: "+str(roll))
    character_dexterity = character_dexterity + roll
    input("Press Enter to roll for Life")
    roll=randint(1,6)
    character_life = character_life + roll
    print("You rolled: "+str(roll))
    input("Press Enter to continue...")
    cls()
    print("""
    Congratulations! You have completed your character creation!
    Your final character sheet is:

    Name:"""+character_name+
    """
    Race:"""+character_race+
    """
    Class:"""+character_class+
    """

    Strength:"""+str(character_strength)+
    """
    Dexterity:"""+str(character_dexterity)+
    """
    Magic:"""+str(character_magic)+
    """
    Life:"""+str(character_life)+"""

    """)
    input("Press Enter to begin your adventure, if you dare...")

modify_skills()

def Scene_1():
    cls()
    choice = None
    while choice is None:
        user_input=input("""
    You have entered the Castle Dungeons..
    It is dark, however thankfully your torch is lit and you can see up to 20 feet away from you.
    The stone walls are damp, the smell of rats and orcs is strong.
    You walk down a narrow corridor, until you reach a thick stone wall.

    The corridor continues on the left, and on the right.

    What do you do?

    1 - Turn left
    2 - Turn right
    > """)
        if user_input=="1" or user_input=="turn left":
            choice="1"
            Scene_2()
        elif user_input=="2" or user_input=="turn right":
            choice="2"
            Scene_3()
        else:
            print("""
            Not a valid choice, type a number or "turn left" / "turn right"
            """)

def Scene_2():
    cls()
    choice = None
    while choice is None:
        user_input=input("""
    From the darkness behind you.. you hear a strange noise.

    What do you do?

    1 - Continue walking
    2 - Stop to listen

    > """)
        if user_input=="1" or user_input=="continue":
            choice="1"
            combat()
        elif user_input=="2" or user_input=="stop":
            choice="2"
            skill_check()
        else:
            print("""
            Not a valid choice, type a number or "continue" / "stop"
            """)

def Scene_3():
    cls()
    choice = None
    while choice is None:
        user_input=input("""
    From the darkness ahead of you.. you hear a strange noise.

    What do you do?

    1 - Continue walking
    2 - Stop to listen

    > """)
        if user_input=="1" or user_input=="continue":
            choice="1"
            combat()
        elif user_input=="2" or user_input=="stop":
            choice="2"
            skill_check()
        else:
            print("""
            Not a valid choice, type a number or - "continue" / "stop"
            """)

def skill_check():
    cls()
    print("A giant rock falls from the ceiling, roll a die to see if you can dodge it.. or you will be crashed by it!")
    roll=randint(1,6)
    print("You rolled: "+str(roll))
    if roll+character_dexterity > 10:
        print ("""
        You dodge the stone and survive! Danger is not over though..
        The strange noise in the darkness continues, and it feels a lot closer now..""")
        input("Press Enter to continue...")
        combat()
    else:
        print("You are smashed by the rock.. You die. The game is over.")
        input("Press Enter to exit the game.")

def combat():
    cls()
    global character_life
    print("A horrible orc attacks you!")
    input("Press Enter to combat...")
    orc = [10, 14]
    while orc[1] > 0 or character_life > 0:
        char_roll=randint(1,6)
        print("You rolled: "+str(char_roll))
        monst_roll=randint(1,6)
        print("The monster rolled: "+str(monst_roll))
        if char_roll+character_strength >= monst_roll+orc[0]:
            print("You hit the monster!")
            orc[1] = orc[1] - randint(1,6)
        else:
            print("The monster hits you!")
            character_life = character_life - randint (1,6)
    if character_life > 0:
        print("You defeated the orc, congratulations!")
        input("Press Enter to exit the game")
    else:
        print("You lost.. your friends will never be freed.. and you're dead.")
        input("Press Enter to exit the game")



Scene_1()

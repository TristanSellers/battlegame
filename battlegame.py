# These are the values for the game
wizard = "Wizard"
elf = "Elf"
human = "Human"
dragon = "Dragon"
wizard_HP = 70
wizard_damage = 150
elf_hp = 100
elf_damage = 100
human_hp = 150
human_damage = 20
dragon_HP = 300
dragon_damage = 50

#This is the selection menu
while True:
    
    print("1 Wizard")
    print("2 Elf")
    print("3 Human")
    character = input("Choose your character! ")

    if character == '1' :
        print("You chose Wizard!")
        print("HP: 70")
        print("Damage: 150")
        character = wizard
        my_hp = wizard_HP
        my_damage = wizard_damage
        break
    elif character == '2' :
        print("You chose Elf!")
        print("HP: 100")
        print("Damage: 100")
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == '3' :
        print("You chose Human!")
        print("HP: 150")
        print("Damage: 20")
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Invalid Choice!")

#This is the battle section
while True:
    dragon_HP = dragon_HP - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon has", dragon_HP, "HP left!")
    if dragon_HP <= 0:
        print("The Dragon has lost the battle")
        break
    my_hp = my_hp - dragon_damage
    print("The", character, "has been hit by the Dragon")
    print("The", character,"has", my_hp, "HP left!")
    if my_hp <= 0:
        print(character, "has lost the battle!")
        break

from Character import Character;

yuumi = Character("Yuumi");
akali = Character("Akali");

# Game loop
while(True):
    print(f"{akali.NAME} has {akali.CURRENT_HP} ({akali.getHpPercentage() * 100}%) HP!");
    attackOption = input("Attack? (y/n)");

    if (attackOption == "y"):
        print(f"{yuumi.NAME} attacks for {yuumi.getAttackValue()}!");
        yuumi.attack(akali);

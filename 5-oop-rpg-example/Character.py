class Character:
    hp = 500;
    mana = 200;
    base_attack_damage = 20;
    level = 1;

    def attack(self):
        print(f"I attack for {self.base_attack_damage} damage!");

class Yuumi(Character):
    hp = 200;
    base_attack_damage = 10;

    def attack(self):
        return super().attack();


yuumi = Yuumi();
yuumi.attack();
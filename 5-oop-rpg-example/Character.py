class Character:
    hp = 500;
    mana = 200;
    base_attack_damage = 20;
    level = 1;

    def attack(self):
        print(f"i attack for {self.base_attack_damage} damage!");
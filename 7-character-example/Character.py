class Character: 
    NAME = "";

    MAX_HP = 200;
    CURRENT_HP = 200;
    
    CURRENT_LEVEL = 1;

    ATTACK_DAMAGE = 10;

    def __init__(self, name):
        self.NAME = name;

    def getHpPercentage(self) -> int:
        return self.CURRENT_HP / self.MAX_HP;

    def attack(self, character):
        character.CURRENT_HP = character.CURRENT_HP - self.getAttackValue();

    def getAttackValue(self) -> int:
        attackDamage = self.ATTACK_DAMAGE * (self.CURRENT_LEVEL * 1.2);
        return attackDamage;
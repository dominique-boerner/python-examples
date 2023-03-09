class Character: 
    MAX_HP = 200;
    MAX_MANA = 100;
    
    CURRENT_HP = 200;
    CURRENT_MANA = 100;

    def getHpPercentage(self) -> float:
        return self.CURRENT_HP / self.MAX_HP;
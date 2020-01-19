# Soldier
class Soldier:
    def __init__(self, health, strength):
        
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receive_damage(self, damage):
        self.health -= damage

# Viking
class Viking(Soldier):
    def __init__(self, health, strength, name):
        
        self.health=health
        self.strength=strength
        self.name=name
    def attack(self):
        return self.strength
    def receive_damage(self, damage):
        self.health -= damage
        if self.health>0:
            return f"{self.name} has received {damage} points of damage."
        else:
            return f"{self.name} has dies in combat."
    def battle_cry (self):
        return "Odin Owns You All!"
    
# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receive_damage(self, damage):
        self.health -= damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage."
        else:
            return "A Saxon has dies in combat."
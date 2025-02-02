from abc import ABC, abstractmethod

class AttackStrategy(ABC):
    @abstractmethod
    def attack(self):
        pass

class SwordAttack(AttackStrategy):
    def attack(self):
        print("Attacking with a sword")

class BowAttack(AttackStrategy):
    def attack(self):
        print("Shooting an arrow")

class MagicAttack(AttackStrategy):
    def attack(self):
        print("Casting a spell")

# character class that uses a strategy
class character:
    def __init__(self, strategy: AttackStrategy):
        self.strategy = strategy # Inject strategy

    def set_strategy(self, strategy: AttackStrategy): # change strategy dynamicallu
        self.strategy = strategy
    
    def attack(self):
        self.strategy.attack() # Execute strategy

# Usage
warrior = character(SwordAttack())
warrior.attack() # Output: "Attacking with a sword"

warrior.set_strategy(BowAttack())
warrior.attack() # Output: "Shooting an Arrow"
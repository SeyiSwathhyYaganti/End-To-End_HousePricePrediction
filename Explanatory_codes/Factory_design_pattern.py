from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Warrior(Character):
    def attack(self):
        print("Warrior attacks")

    def defend(self):
        print("Warrior defends")
    
    def move(self):
        print("Warrior moves")

w = Warrior()
w.attack()

# c = Character() doestnot work because you cannot instantiate abstract classes
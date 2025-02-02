from abc import ABC, abstractmethod

class DiningExperience(ABC):
    # The template method defines the skeleton of the dining experience
    def serve_dinner(self):
        self.serve_appetizer()
        self.serve_main_course()
        self.serve_dessert()
        self.serve_beverage()

    @abstractmethod
    def serve_appetizer(self):
        pass

    @abstractmethod
    def serve_main_course(self):
        pass

    @abstractmethod
    def serve_dessert(self):
        pass

    @abstractmethod
    def serve_beverage(self):
        pass

# Create concrete classes that implement the template steps
class ItalianDinner(DiningExperience):
    def serve_appetizer(self):
        print("serving bruschetta as appetizer")
    
    def serve_main_course(self):
        print("serving pasta as main course")
    
    def serve_dessert(self):
        print("serving tiramisu as dessert")
    
    def serve_beverage(self):
        print("serving wine as beverage")

class ChineseDinner(DiningExperience):
    def serve_appetizer(self):
        print("serving spring rolls as appetizer")
    
    def serve_main_course(self):
        print("serving noodles as main course")
    
    def serve_dessert(self):
        print("serving fortune cookies as dessert")
    
    def serve_beverage(self):
        print("serving tea as beverage")

# Client code
if __name__ == "__main__":
    print("Italian Dinner:")
    italian_dinner = ItalianDinner()
    italian_dinner.serve_dinner()

    print("\nChinese Dinner:")
    chinese_dinner = ChineseDinner()
    chinese_dinner.serve_dinner()
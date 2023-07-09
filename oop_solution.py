class Podracer:
    def __init__(self, max_speed, condition,price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"
    

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2 

class SebulasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def flame_jet(self, otherPodracer):
        otherPodracer.condition = "trashed"

#How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

#This uses Inheritance in both AnakinsPod and SebulasPod to inherit the properties of Podracer.
#It uses Polymorphism in the sense that the Podracer can be AnakinsPod or SebulasPod.
#It uses Encapsulation to encapsulate all bits of information for a Podracer into a single super class that can have its properties inherited by other sub classes.

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# It was better to use OOP due to the fact that in these classes the Podracer(s) had specific attributes that were needed for each particular Podracer. It is easier to have these put into classes than to individually assign each one its own attribute or even change it.

# How in particular did Object Oriented Programming assist in the solving of this problem?
# OOP helped due to adding specific and unique attributes and methods to other subclasses that also inherited the properties of the Podracer super class to make it easier when assigning attributes to those classes and overall helped with code reusability.
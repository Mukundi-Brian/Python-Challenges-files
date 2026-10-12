# A spaceship simulator
# Lore: You have been sent to explore a distant planet. Your spaceship has a name, fuel, health and a way to report status. However you get stranded and end up in a hostile space vacuum environment and the only way out is to try your luck.

# Imports
import random

# Spaceship
class Spaceship:
    """Blueprint for Spaceships"""
    # Variable for number of ships created
    no_of_ships = 0

    def __init__(self, name, fuel, health):
        self.name = name
        self.fuel = fuel
        self.health = health
        Spaceship.no_of_ships += 1

    def ship_status(self):
        """Function that monitors and prints the ship status"""
        print(f"Ship Name: {self.name}")
        print(f"Fuel Level: {self.fuel}")
        print(f"Health Level: {self.health}")

        if self.fuel > 100 or self.health > 100:
            print("Defective Ship! Fuel and health cannot be above 100%!")
            exit()

        elif self.fuel < 0 or self.health < 0:
            print("Defective Ship! Fuel or health cannot be below 100%!")
            exit()

        if 20 < self.fuel < 40 or 20 < self.health < 40:
            print("Systems are in poor capacity.\n")
        elif 40 <= self.fuel < 70 or 40 <= self.health < 70:
            print("Systems in good condition")
        elif 70 <= self.fuel <= 100 and 70 <= self.health <= 100:
            print("Systems in full capacity")
        else:
            print("System has suffered catastrophic damage!\n")

    def random_events(self):
        """Function that models random events that happen"""
        random_event_prob = random.randint(1, 11)
        if random_event_prob in (1,5):
            print("A mini black hole appears and you suffer catastrophic damage")
            self.health -= 40
            self.fuel -= 30
        elif random_event_prob == 3:
            print("Flying debris hit your ship causing minor damage")
            self.health -= 5
            self.fuel -= 5
        elif random_event_prob == 4:
            print("Squad morale drops and engineers slack in maintenance")
            self.health -= 20
            self.fuel -= 20
        elif random_event_prob == 9:
            print("A space monster chews on one of the ships wings")
            self.health = 20
        else:
            print("Nothing happened ... lucky you!")

class Game(Spaceship):
    """Class that builds the game"""
    # Modelling the random events
    def ship_choices(self):
        """Function for modelling the random events that happen to the ship"""
        # User chooses an option
        print("""You have been sent to explore a distant planet. However, an error occurred and you are now trapped in a hostile space vacuum, you have a few chances to succeed. Good luck. You have 3 options:
        1. You navigate randomly (Consumes 30 fuel and 20 health)
        2. You see a spot that could be safe (Consumes 40 fuel and 10 health)
        3. You hold your position (Consumes 0 fuel but 50 health)""")
        event_chance = int(input("Enter the option you choose! (1-3) : "))
    
        if event_chance == 1:
            print("You have failed and entered a mini-black hole, its not looking good!")
            self.health -= 20
            self.fuel -= 20
            print(f"Ship health is: {self.health}")
            print(f"Ship fuel is: {self.fuel}")
    
        elif event_chance == 2:
            print("You somehow escape the hostile environment yet, your ship tail got stuck on one of the debris, you are not yet out of the woods!\n")
            self.health -= 10
            self.fuel -= 40
            print(f"Ship health is: {self.health}")
            print(f"Ship fuel is: {self.fuel}")
    
        elif event_chance == 3:
            print("You skillfully navigate the hostile environment and emerge victorious at the other side! Excellent work Captain!")
            print("You Won!\n")
            self.fuel -= 50
            print(f"Ship health is: {self.health}")
            print(f"Ship fuel is: {self.fuel}")
            
# mach_1 = Spaceship("Mach1", 40, 40)
# mach_2 = Spaceship("Mach2", 50, 80)
mach_3 = Spaceship("Mach3", 100, 100)

# mach_1.ship_status()
# mach_2.ship_status()
mach_3.ship_status()
mach_3.random_events()
mach_3.ship_status()
new_game = Game("Mach4", 100, 100)

new_game.ship_choices()

# mach_3.ship_choices()

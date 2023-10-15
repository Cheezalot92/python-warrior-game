class Hero:
    def __init__(self, health, power, attack_power):
        self.health = health
        self.power = power
        self.attack_power = attack_power


    def attack(self, goblin):
        goblin.health -= self.power

    
    def alive(self):
        return self.health > 0
            
    
        
    def print_status(self):
        print("The Goblin Slayer has %d health and %d power! GO hero!" % (self.health, self.power)) 


class Goblin:
    def __init__(self, goblin_health, goblin_power, attack_power):
        self.health = goblin_health
        self.power = goblin_power
        self.goblin_attack = attack_power


    def attack(self, hero):
        hero.health -= self.power


    def alive(self):
        return self.health > 0
         
        
    def print_status(self):
        print("The giant hob goblin has %d health and %d power! ATTACK!!" % (self.health, self.power))

hero = Hero(18, 5, 5)
goblin = Goblin(15, 2, 2)


while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. Attack the giant hob goblin")
        print("2. Attack the hero")
        print("3. Do Nothing")
        print("4. Flee")
        print("> ", end ="")
        user_input = input()


        if user_input == "1":
             # Hero attacks goblin
            hero.attack(goblin)
            print("You do %d damage to the hob goblin." % hero.power)
            if not goblin.alive():
                print("The giant hob goblin is dead.")
        elif user_input == "2":
            goblin.attack(hero)
            print("The giant hob goblin slashes Goblin slayer")
        elif user_input == "3":
            pass
        elif user_input == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.alive() and user_input != "2":
            # Goblin attacks hero
            goblin.attack(hero)
            print("The goblin does %d damage to you." % goblin.power)
            if not hero.alive():
                print("You are dead.")














# class Person:
#     def __init__(self, name, email, phone):
#       self.name = name
#       self.email = email
#       self.phone = phone

#     def greet(self, other_person):
#       print('Hello %s, I am %s!' % (other_person.name, self.name))
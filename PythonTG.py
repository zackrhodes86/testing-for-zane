#Classes  

class MyPlayer:
    def __init__(self, name, weapon, health, damage):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.damage = damage

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

 
def introScene(knife):
    directions = ["forward"]
    print("You look around the room you woke up in...")
    print("You see an altar where the object you stole stood...")
    print("There are some deactive traps in the corner...")
    userInput = ""
    while userInput not in directions:
        print("Options: forward")
        userInput = input()
        if userInput == "forward":
            roomTwo(knife)
       # elif userInput == "menu":
        #    menu()
        else:
            print("Please enter a valid option")
            print("It looks like there is not else you can do in this room")
            
def roomTwo(player):
    directions = ["forward, backward"]
    print("Wow you've made it to room 2!")
    if player.weapon == False:
        print("You found your pocket knife on the floor")
        player.weapon = True
        player.damage = 6
        print(f'It looks like you found your weapon {player.name}! This is {player.weapon}. You have {player.health} health and you do {player.damage} damage')
    userInput = ""
    while userInput not in directions:
        print("Options: forward", "backward")
        userInput = input()
        if userInput == "forward":
            roomThree(player)
        elif userInput == "backward":
            introScene(player)
        else:
            print("Please enter a valid option")
            print("It looks like there is not else you can do in this room")


def roomThree(player):
    print("ROooom 3!")
    print("As you enter this room, you see a giant spider fall down from the cieling...")
    print("It noticed you! It seems to be hostile...")
    print("What will you do?")
    bigSpider = Enemy("Giant Spider", 10, 1)

    print(f'The {bigSpider.name} has {bigSpider.health}')

    directions = ["forward", "backward", "right", "attack"]
    userInput = ""
    while userInput not in directions:
        print("Options: forward, backward, left, right, attack")
        userInput = input()
        if (userInput == "forward") and (bigSpider.health <= 0):
            quit()
        elif(userInput == "attack"):
            bigSpider.health -= player.damage
            print(f'You hit the spider for {player.damage} damage!')
        elif userInput == "backward":
            roomTwo(player)
        elif userInput == "left":
            print("You try and make a left")
            print("As you approach the doorway, you notice that it is a 20 meter drop...")
            print("'No way can I go there!' you think to your self")
        elif userInput == "right":
            print("NEW ROOOOOOM")
        
        else:
            print("Please enter a valid option")
            print("It looks like there is not else you can do in this room")

def roomFour(player):   
    print("You have entered room 4!")
    quit()         
#make a menu option
#def menu():
#    options = ["bag", "controls"]
 #   print("You've accessed the menu")
 #   print("You can type 'bag' to access your items")
 #   userInput = ""
 #   userInput = input()
 #    if userInput == "bag":
            
   

if __name__ == "__main__":
    hasKnife = False
    while True:
        print("Welcome to my Python Adventure Game!");
        print("You were tasked with retreieving an ancient objects from an underground cave...")
        print("After finding the object, a lost rock hit your head and you blacked out...")
        print("This game is played using text based responses...")
        print("You can type 'menu' at anytime to access the menu")
        print("Let's start with your name: ")
        title = input()
        ourPlayer = MyPlayer(title, False, 10, 2)
        print("Good luck " + ourPlayer.name + ", I hope you can find your way out! ")
        print(f'It looks like you lost your weapon {ourPlayer.name}! This is {ourPlayer.weapon}. You have {ourPlayer.health} health and you do {ourPlayer.damage} damage')
        introScene(ourPlayer)
        
        
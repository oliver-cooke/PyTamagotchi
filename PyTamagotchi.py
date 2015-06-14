class Creature():
    stats = ("Sick",
             "Bad",
             "Ok",
             "Good",
             "Great")
    
    hunger = ("Starving",
              "Hungry",
              "Satified",
              "Nourished",
              "Full")
    
    rest = ("Sleep Deprived",
            "Tired",
            "Awake",
            "Rested",
            "Energised")
    
    happiness = ("Sad",
                 "Annoyed",
                 "Contempt",
                 "Happy",
                 "Euphoric")    
    
    def __init__(self, name):
        self.name = name
        self.hunger = 12
        self.happiness = 12
        self.rest = 12
        self.age = 1
        self.sick = 0
        
    def __str__(self):
        name = "\n"+ str(self.name) + "'s stats:"
        name += "\nhunger: " + str(Creature.hunger[int(self.hunger /3) ])
        name += "\nrest: " + str(Creature.rest[int(self.rest /3)])
        name += "\nhappiness: " + str(Creature.happiness[int(self.happiness / 3)])
        name += "\nage: " + str(self.age)
        
        total = int((self.hunger + self.happiness + self.rest) / 3)
        overallStats = "\noverall: " + str(Creature.stats[int(total / 3)])
        
        return name + overallStats
    
    def feed(self):
        self.hunger += 2
        
    def nextDay(self):
        if self.hunger > 15:
            self.hunger = 15
        if self.happiness> 15:
            self.happiness = 15
        if self.rest > 15:
            self.rest = 15 
        
        if self.hunger < 0:
                self.hunger = 0
        if self.happiness < 0:
            self.happiness = 0
        if self.rest < 0:
            self.rest = 0
        
        self.hunger -= 2
        self.rest -= 2
        self.happiness -= 2
        self.age += 2
        print(self)
        total = int((self.hunger + self.happiness + self.rest) / 3)
        if total < 3:
            self.sick += 1
        

player = Creature(input("what do you want to name your creature? "))
loop = 1

while loop == 1:
    choice = None
    while choice == None:
        inp = input("\nwhat do you want to do? ")
        
        if inp == "feed":
            player.feed()
            choice = 1
            
        elif inp == "play":
            player.play()
            choice = 1
            
        elif inp == "rest":
            player.rest()
            choice = 1
            
        elif inp == "nothing":
            choice = 1
        
        else:
            print("please select a useful choice") 
    player.nextDay()
    if player.sick == 3:
        loop = 0
        break
    
    
print("---------------------------------------------")
print("you have killed ", player.name, ",you monster")
print("---------------------------------------------")
    
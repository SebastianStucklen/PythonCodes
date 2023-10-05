#seb stuff
def spaces():
    for i in range(20):
        print("-", end="")
    print("-")

import random
class lightbulb():
    def __init__(self,red,green,blue, name):
        self.status = True
        self.color = [
            red,
            green,
            blue
        ]
        self.burntOut = False
        self.name = name
    def burn(self):
        chance = random.randint(0,100)
        if chance <= 5:
            print(f"{self.name} burnt out")
            self.burntOut = True
    def onoff(self):
        if self.burntOut == True:
            print(f"{self.name} is burnt out right now")
        elif self.status == True:
            print(f"{self.name} turning off")
        elif self.status == False:
            print(f"{self.name} turning on")

One = lightbulb(255,255,255, "Andrew")
Two = lightbulb(255,220,100,"Jake")
Three = lightbulb(100,255,90, "Sophie")

for i in range(5):
    One.onoff()
    One.burn()

    spaces()

    Two.onoff()
    Two.burn()

    spaces()

    Three.onoff()
    Three.burn()

    spaces()
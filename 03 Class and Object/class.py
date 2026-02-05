'''defining class & object'''

class Club:
    name = "anything you want"
    phone = "+62"
    email = "realityclub@mail.com"
    buyed = "nothing"

    def sayName (self): 
        print ("My name is...", self.name)

#we can see attrib, method, class, and the results is object

realityClub = Club() #class = car design, attrib = color, method = brake, object = actual car

''''acsessing and changing attribute'''

Club.name #acsessing value
Club.name = "RealityClub" #changing value

'''Creating Method'''
 
class Reality:
    name = "Sorrowful Reunion"

    def sayName (self): 
        print ("My name is...", self.name)

def main ():
    aReality = Reality() #Acsess Value
    aReality.sayName ()  
    aReality.name = "MBG - My Bini Gw" #Changing Value
    aReality.sayName()

main () #Calling Value

'''Creating Constructor'''

class test ():
    def __init__(self, name, company): #init used in constructor
        self.name = name
        self.company = company

    def show(self):
        print("Hello my name is " + self.name + " and I" + " work in " + self.company + ".")

obj = test("Asep", "Roulette")
obj.show()
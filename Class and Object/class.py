'''defining class & object'''

class Club:
    name = "anything you want"
    phone = "+62"
    email = "realityclub@mail.com"
    buyed = "nothing"

#we can see attrib, method, class, and the results is object

realityClub = Club() #class = car design, attrib = color, method = brake, object = actual car

''''acsessing and changing attribute'''

Club.name #acsessing value
Club.name = "RealityClub" #changing value

'''Creating Method'''
 
class Reality:
    name = "Sorrowful Reunion :("
    def sayName (self):
        print ("My name is...", self.name)

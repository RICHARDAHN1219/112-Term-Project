
class Player(App):
    def __init__(self, playerNumber, country, position, number, courtPosition):
        self.playerNumber = playerNumber
        self.country = country
        self.position = position
        self.number = number
        self.courtPosition = courtPosition
    
    def bump(self):
        #reduce ball velocity, hit it like to front or across court
        #send ball to setter
        pass

    def toss(self):
        #this is default set
        #set to person to the right or middle
        pass

class Setter(Player):
    def C_Toss(self):
        if self.courtPosition == 3:
            #Set the ball coordinates to the be within range of the coordinates of the player in position 1
            pass
        elif self.courtPosition == 1:
            #Set the ball coordinates to the be within range of the coordinates of the player in position 1
            pass
    def Default(self):
        pass
    def Dump(self):
        pass
    def A_Toss(self):
        pass
    def diagonal(self):
        pass
    def B_Toss(self):
        pass
    def backRow(self):
        pass

class Spiker(Player):
    def lineShot(self):
        pass

    def crossShot(self):
        pass

class Libero(Player):
    def underhandReceive(self):
        pass

    def overhandReceive(self):
        pass

class MiddleBlocker(Blocker):
    #Main blockers
    def block(self):
        #Jump up and try to stop block
        #RESULTS
        #Kill block
        #Touch
        #Miss
        #Jumping will be estimated through button press
        pass

class MiddleBlocker(Blocker):
    #Main blockers
    def readBlock(self):
        #follow one of the front row opponents
        pass
    def guessBlock(self):
        #guess a direction the ball will go and block in that direction
        pass
    def assistBlock(self):
        #stick next to another blocker
        pass


class Receiver(Libero):
    #Be able to receive, then spike for all number of players modes
    def lineShot(self):
        pass
    def crossShot(self):
        pass

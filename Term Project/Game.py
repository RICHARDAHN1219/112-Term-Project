from cmu_112_graphics import *
from PIL import *
import string, math, random
#from pygame import mixer
from tkinter import *


class HomeScreen(App):
    def appStarted(self):
        self.counter = 0
        self.image1 = self.loadImage('haikyuu gifs.gif')
        self.image2 = self.scaleImage(self.image1, 5)

    def keyPressed(self, event):
        self.counter += 1

    def mousePressed(self, event): 
        if event.x >= self.width/2-125 and event.x <= self.width/2+125:
            if event.y >= self.height/2 - 25 and event.y <= self.height/2 + 25:
                MatchOptions(width=1366, height=705)


    def redrawAll(self, canvas):
        canvas.create_rectangle(0,0,self.width,self.height, fill = "#ffeeda")
        canvas.create_image(self.width/2, self.height/2, image=ImageTk.PhotoImage(self.image2))
        #Title
        canvas.create_rectangle(self.width/2 +500, 10, self.width/2 - 500, 160,
                            fill = "#f49030", width = 3)
        canvas.create_text(self.width/2, 85, text = "VOLLEYBALL 2020", font = "Arial 40 bold")
        #Play button
        playButton = canvas.create_rectangle(self.width/2-125, self.height/2 - 25, self.width/2 + 125, self.height/2 + 25,
                            fill = "#f49030", width = 2)
        canvas.create_text(self.width/2, self.height/2, text = "Play!", font = "Arial 20 bold")
        #Tutorial
        tutorialButton = canvas.create_rectangle(self.width/2-125, self.height/2 + 75, self.width/2 + 125, self.height/2 + 125,
                            fill = "#f49030", width = 2)
        canvas.create_text(self.width/2, self.height/2 + 100, text = "Tutorial", font = "Arial 20 bold")
        #Controls button
        controlsButton = canvas.create_rectangle(self.width/2-125, self.height/2 + 175, self.width/2 + 125, self.height/2 + 225,
                            fill = "#f49030", width = 2)
        canvas.create_text(self.width/2, self.height/2 + 200, text = "Controls", font = "Arial 20 bold")       

class MatchOptions(App):
    def appStarted(self):
        self.PlayerCount = 0
        self.Difficulty = "Easy"
        self.counter = 0
    Teamlist = [
            "America",
            "Karasuno",
            "Brazil",
            "Russia",
            "France",
            "India",
            "Germany"
        ] #expand list later
    Team1 = random.choice(Teamlist)
    Team2 = random.choice(Teamlist)

    def keyPressed(self, event):
        self.counter += 1

    def mousePressed(self, event):
        #### Number of Players ####
        #when clicking on the 1 box
        if event.y >= self.height/2 - 25 and event.y <= self.height/2 + 25:
            if event.x >= self.width/4 and event.x <= int(self.width/3):
                self.PlayerCount = 1
        #when clicking on the 2 box
        if event.y >= self.height/2 - 25 and event.y <= self.height/2 + 25:
            if event.x >= int(self.width/3) and event.x <= int(self.width* 5/12):
                self.PlayerCount = 2
        #when clicking on the 6 box
        if event.y >= self.height/2 - 25 and event.y <= self.height/2 + 25:
            if event.x >= int(self.width* 5/12) and event.x <= self.width/2:
                self.PlayerCount = 6       
        #### Difficulty ####
        #when clicking on the 1 box
        if event.y >= self.height/2 + 75 and event.y <= self.height/2 + 125:
            if event.x >= self.width/4 and event.x <= int(self.width/3):
                self.Difficulty = "Easy"
        #when clicking on the 2 box
        if event.y >= self.height/2 + 75 and event.y <= self.height/2 + 125:
            if event.x >= int(self.width/3) and event.x <= int(self.width* 5/12):
                self.Difficulty = "Medium"
        #when clicking on the 6 box
        if event.y >= self.height/2 + 75 and event.y <= self.height/2 + 125:
            if event.x >= int(self.width* 5/12) and event.x <= self.width/2:
                self.Difficulty = "Hard"     
        #Continue is pressed
        if event.y >= self.height - 100 and event.y <= self.height - 50:
            if event.x >= self.width - 120 and event.x <= self.width - 20:
                Sides(width=1366, height=705)
    def redrawAll(self, canvas):
        canvas.create_rectangle(0,0,self.width,self.height,fill = "#ffeeda")
        #Title
        canvas.create_rectangle(self.width/2 +500, 10, self.width/2 - 500, 160,
                            fill = "#f49030", width = 3)
        canvas.create_text(self.width/2, 85, text = "Match Options", font = "Arial 40 bold")
        #Player counts
        canvas.create_text(self.width/8, self.height/2, text= "Player Count", font = "Arial 20 bold")
        playerCountButton1 = canvas.create_rectangle(self.width/4, self.height/2 - 25, int(self.width/3), self.height/2 + 25,
                            fill = "#f49030", width = 2)
        canvas.create_text((self.width/4 + self.width/3)//2, self.height/2, text = "1", font = "Arial 20 bold")
        playerCountButton2 = canvas.create_rectangle(int(self.width/3), self.height/2 - 25, int(self.width* 5/12), self.height/2 + 25,
                            fill = "#f49030", width = 2)
        canvas.create_text((int(self.width* 5/12) + self.width/3)//2, self.height/2, text = "2", font = "Arial 20 bold")
        playerCountButton6 = canvas.create_rectangle(int(self.width* 5/12), self.height/2 - 25, self.width/2, self.height/2 + 25,
                            fill = "#f49030", width = 2)
        canvas.create_text((int(self.width* 5/12) + self.width/2)//2, self.height/2, text = "6", font = "Arial 20 bold")
        #Difficulty
        canvas.create_text(self.width/8, self.height/2+100, text= "Difficulty", font = "Arial 20 bold")
        playerCountButton1 = canvas.create_rectangle(self.width/4, self.height/2 + 75, int(self.width/3), self.height/2 + 125,
                            fill = "#f49030", width = 2)
        canvas.create_text((self.width/4 + self.width/3)//2, self.height/2 + 100, text = "Easy", font = "Arial 20 bold")
        playerCountButton2 = canvas.create_rectangle(int(self.width/3), self.height/2 + 75, int(self.width* 5/12), self.height/2 + 125,
                            fill = "#f49030", width = 2)
        canvas.create_text((int(self.width* 5/12) + self.width/3)//2, self.height/2 + 100, text = "Medium", font = "Arial 20 bold")
        playerCountButton6 = canvas.create_rectangle(int(self.width* 5/12), self.height/2 + 75, self.width/2, self.height/2 + 125,
                            fill = "#f49030", width = 2)
        canvas.create_text((int(self.width* 5/12) + self.width/2)//2, self.height/2 + 100, text = "Hard", font = "Arial 20 bold")
        canvas.create_text(self.width - 50, 50, text = f"{self.PlayerCount}, \n{self.Difficulty}, \n{MatchOptions.Team1}", font = "Arial 12 bold")        
        #Continue
        canvas.create_rectangle(self.width-120, self.height - 100, self.width-20, self.height-50, fill = "#f49030", width = 2)
        canvas.create_text(self.width-70, self.height-75, text = "Continue", font = "Arial 18 bold")

class Sides(App):
    #In this code, we want the different players to select a certain side of the match,
    #so that it could be a 1 v 1 or 2 v AI
    def appStarted(self):
        self.playersInTeam1 = []
        self.playersInTeam2 = []
        self.Player1 = "Hinata"
        self.Player2 = "Kageyama"
        self.imageNum1 = self.loadImage("number1.png")
        self.imageNum2 = self.loadImage("number2.png")
        self.PlayerIcon1 = self.scaleImage(self.imageNum1, .07)
        self.PlayerIcon2 = self.scaleImage(self.imageNum2, .07)
        self.Teamlist = MatchOptions.Teamlist
        self.Team1 = MatchOptions.Team1
        self.Team2 = MatchOptions.Team2
        self.player1X = self.width/2
        self.player1Y = self.height/2 + 30
        self.player2X = self.width/2
        self.player2Y = self.height/2 + 100
        self.Team1List = ",".join(self.playersInTeam1)
        self.Team2List = ",".join(self.playersInTeam2)


    def keyPressed(self, event):
        if event.key == 'a':
            if self.player1X > 0:
                if self.Player1 not in self.playersInTeam1:
                    if self.Player1 in self.playersInTeam2:
                        self.playersInTeam2.remove(self.Player1)
                        self.player1X -= 500
                        self.player1Y = 705/2 + 30
                    else:
                        self.playersInTeam1.append(self.Player1)
                        if self.Player2 not in self.playersInTeam1:
                            self.player1X -= 500
                            self.player1Y = 705/2
                        else:
                            self.player1X -= 500
                            self.player1Y = 705/2
                            self.player2Y = 705/2 + 135

        if event.key == 'd':
            if self.player1X > self.width/2:
                self.player1X = self.width/2
            if self.player1X <= self.width/2:
                if self.Player1 not in self.playersInTeam2:
                    if self.Player1 in self.playersInTeam1:
                        self.playersInTeam1.remove(self.Player1)
                        self.player1X += 500
                        self.player1Y = 705/2 + 30
                    else:
                        self.playersInTeam2.append(self.Player1)
                        if self.Player2 not in self.playersInTeam1:
                            self.player1X += 500
                            self.player1Y = 705/2
                        else:
                            self.player1X += 500
                            self.player1Y = 705/2
                            self.player2Y = 705/2 + 135

        if event.key == "Left":
            if self.Player2 not in self.playersInTeam1:
                if self.Player2 in self.playersInTeam2:
                    self.playersInTeam2.remove(self.Player2)
                    self.player2X -= 500
                    self.player2Y = 705/2 + 100
                else:    
                    self.playersInTeam1.append(self.Player2)
                    if self.Player1 not in self.playersInTeam1:
                        self.player2X -= 500
                        self.player2Y = 705/2 + 135
                    else:
                        self.player2X -= 500
                        self.player2Y = 705/2 + 135
                        self.player1Y = 705/2
        if event.key == "Right":
            if self.Player2 not in self.playersInTeam2:
                if self.Player2 in self.playersInTeam1:
                    self.playersInTeam1.remove(self.Player2)
                    self.player2X += 500
                    self.player2Y = 705/2 + 100
                else:
                    self.playersInTeam2.append(self.Player2)
                    if self.Player1 not in self.playersInTeam1:
                        self.player2X += 500
                        self.player2Y = 705/2 + 135
                    else:
                        self.player2X += 500
                        self.player2Y = 705/2 + 135
                        self.player1Y = 705/2 
         
    def mousePressed(self, event):
        #Continue is pressed
        if event.y >= self.height - 100 and event.y <= self.height - 50:
            if event.x >= self.width - 120 and event.x <= self.width - 20:
                Match(width=1366, height=705)
    #def moveIconToRight(self):
    #    pass
    def redrawAll(self, canvas):
        canvas.create_rectangle(0,0,self.width,self.height,fill = "#ffeeda")
        #Title
        canvas.create_rectangle(self.width/2 +500, 10, self.width/2 - 500, 160,
                            fill = "#f49030", width = 3)
        canvas.create_text(self.width/2, 85, text = "Choose Sides", font = "Arial 40 bold")
        #Continue
        
        canvas.create_rectangle(self.width-120, self.height - 100, self.width-20, self.height-50, fill = "#f49030", width = 2)
        canvas.create_text(self.width-70, self.height-75, text = "Continue", font = "Arial 18 bold")
        #canvas.create_text(self.width/4, self.height/2 - 50, text = f'{self.Team1}', font = "Arial 25 bold")
        #canvas.create_text((self.width * 3/4), self.height/2 - 50, text = f'{self.Team2}', font = "Arial 25 bold")
        canvas.create_text(self.width/2 - 450, 200, text = f"{self.Team1}", font = "Arial 24 bold")
        #Do the same with Team 2 on the right
        canvas.create_text(self.width/2 + 450, 200, text = f"{self.Team2}", font = "Arial 24 bold")
        canvas.create_image(self.player1X, self.player1Y, image=ImageTk.PhotoImage(self.PlayerIcon1))
        canvas.create_image(self.player2X, self.player2Y, image=ImageTk.PhotoImage(self.PlayerIcon2))

        
        if self.playersInTeam1 == []:
            team1Text = "CPU"
            #now make team1 have only AI's 
        else:
            team1Text = ", ".join(self.playersInTeam1)
        if self.playersInTeam2 == []:
            team2Text = "CPU"
            #now make team2 have only AI's 
        else:
            team2Text = ", ".join(self.playersInTeam2)
        canvas.create_text(self.width/2, self.height - 50, 
                text = f"Team {self.Team1}: " + team1Text, font = "Arial 12 bold", fill = "#B53737")
        canvas.create_text(self.width/2, self.height - 30, 
                text = f"Team {self.Team2}: " + team2Text, font = "Arial 12 bold", fill = "#1338BE")


class Match(App):
    def appStarted(self):
        Match.resetApp(self)
    
    def resetApp(self):
        # This is a helper function for Controllers
        # This initializes most of our model (stored in app.xyz)
        # This is called when they start the app, and also after
        # the game is over when we restart the app.
        self.timerDelay = 500 # milliseconds
        self.score1 = 0
        self.score2 = 0
        self.waitingForKeyPress = True
        self.gameOver = False
        self.paused = False
        Match.resetTeams(self)
        Match.resetCourt(self)
        Match.resetPlayers(self)
        Match.resetBall(self)
        self.dotDx = -5
        self.dotDy = -3
        self.incrementX = 60
        self.incrementY = 3
    
    def resetTeams(self):
        self.imageNum1 = self.loadImage("number1.png")
        self.imageNum2 = self.loadImage("number2.png")
        self.PlayerIcon1 = self.scaleImage(self.imageNum1, 2/3)
        self.PlayerIcon2 = self.scaleImage(self.imageNum2, 2/3)
        self.Team1 = MatchOptions.Team1
        self.Team2 = MatchOptions.Team2

    def resetCourt(self):
        self.imageCourt = self.loadImage("court2dtransparent.png")
        self.courtimage = self.scaleImage(self.imageCourt, 2.2)
        self.ballimage = self.loadImage("volleyballimage.png")
        self.volleyballImage = self.scaleImage(self.ballimage, .04)

    def resetBall(self):
        # This is a helper function for Controllers
        # Get the dot ready for the next round.  Move the dot to
        # the center of the screen and give it an initial velocity.
        self.ballWidth = self.width/2-30
        self.ballHeight = self.height/2 + 30
        self.ballRadius = 15
    
    def resetPlayers(self):
        self.dot1Width = self.width/2-90
        self.dot1Height = self.height/2 + 50
        self.dot2Width = self.width/2+90
        self.dot2Height = self.height/2 + 50
    '''def drawCourt(self, canvas):
        canvas.create_rectangle(0,0,self.width,self.height,fill = "#ffeeda")
        canvas.create_image(1366/2, 705/2 + 30, image=ImageTk.PhotoImage(self.courtimage))

    def drawScoreBoard(self, canvas):
        canvas.create_rectangle(self.width/2 +300, 10, self.width/2 - 300, 100,
                            fill = "#f49030", width = 3)
        canvas.create_text(self.width/2, 55, text = f"{self.score1} - {self.score2}", font = "Arial 40 bold")

    def drawVolleyball(self, canvas):
        cx, cy, r = self.ballWidth, self.ballHeight, self.volleyballRadius
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "pink")'''
    def timerFired(self):
        # This is a Controller
        if (not self.paused):
            Match.doStep(self)

    def doStep(self):
        if not self.waitingForKeyPress and not self.gameOver:
            Match.moveBall(self)

    def keyPressed(self, event):
        if self.gameOver:
            Match.resetApp(self)
        elif self.waitingForKeyPress:
            self.waitingForKeyPress = False
        if event.key == "q":
            #switch control to the player to the left of the current one in back row
            pass
        if event.key == "e":
            #switch control to the player to the left of the current one in front row
            pass
        if event.key == 'a':
            #current player moves left
            self.dot1Width -= 15
        elif event.key == 'd':
            #current player moves right
            self.dot1Width += 15
        elif event.key == "s":
            self.dot1Height += 15
        elif event.key == "w":
            self.dot1Height -= 15
        if event.key == 'Left':
            #current player moves left
            self.dot2Width -= 15 
        elif event.key == 'Right':
            #current player moves right
            self.dot2Width += 15
        elif event.key == "Down":
            self.dot2Height += 15
        elif event.key == "Up":
            self.dot2Height -= 15
        elif event.key == "p":
            #have spike function run
            pass
    '''def mousePressed(self, event):
        #Continue button is pressed
        pass
    def moveIconToRight(self):
        pass'''

    '''def mousePressed(self, event):
        print(event.x, event.y)'''

    def moveBall1(self):       
        self.ballWidth += self.dotDx
        self.ballHeight += self.dotDy 
        if Match.ballIntersects(self):
            if (self.dot1Width <= self.ballWidth <= self.dot1Width + 40 
            or self.dot1Height-40 <= self.ballHeight <= self.dot1Height):
                self.dotDx = 10
                self.dotDy = random.choice([-self.dotDy, self.dotDy])
                self.ballWidth += self.incrementX
                #self.ballHeight += random.choice([-self.incrementY, self.incrementY])
            elif (self.dot2Width <= self.ballWidth <= self.dot2Width + 40 
            or self.dot2Height >= self.ballHeight >= self.dot2Height - 40):
                self.dotDx = -10
                self.dotDy = random.choice([-self.dotDy, self.dotDy])
                self.ballWidth -= self.incrementX
                #self.ballHeight += random.choice([-self.incrementY, self.incrementY])
        if (self.ballHeight + self.ballRadius >= self.height): #self.height
            # The dot went off the bottom!
            self.ballHeight = self.height - self.ballRadius
            self.dotDy = -self.dotDy
        elif (self.ballHeight - self.ballRadius <= 0): #0
            # The dot went off the top!
            self.ballHeight = self.ballRadius
            self.dotDy = -self.dotDy
        if (self.ballWidth + self.ballRadius >= self.width): #self.width
            # The dot went off the right!
            self.ballWidth = self.width - self.ballRadius
            self.dotDx = -self.dotDx
        elif (self.ballWidth - self.ballRadius <= 0): #0
            # The dot went off the top!
            self.ballWidth = self.ballRadius
            self.dotDx = -self.dotDx
            #self.score += 1 # hurray!
            #self.dotDx = -self.dotDx
            #dToMiddleY = self.ballHeight - (self.dot1Height * 2 - 40)/2
            #dampeningFactor = 3 # smaller = more extreme bounces
            #self.dotDy = dToMiddleY / dampeningFactor
            '''if self.speedMode:
                self.dotDx *= 1.5
                self.dotDy *= 1.5'''

    def moveBall(self):    
        self.ballWidth += self.dotDx
        self.ballHeight += self.dotDy 
        if (self.ballHeight + self.ballRadius >= self.height): #self.height
                # The dot went off the bottom!
                self.ballHeight = self.height - self.ballRadius
                self.dotDy = -self.dotDy
        if (self.ballHeight - self.ballRadius <= 0): #0
                # The dot went off the top!
                self.ballHeight = self.ballRadius
                self.dotDy = -self.dotDy
        if (self.ballWidth + self.ballRadius >= self.width): #self.width
                # The dot went off the right!
                self.ballWidth = self.width - self.ballRadius
                self.dotDx = -self.dotDx
        elif (self.ballWidth - self.ballRadius <= 0): #0
            # The dot went off the top!
            self.ballWidth = self.ballRadius
            self.dotDx = -self.dotDx
        elif Match.ballIntersects(self):
            # The dot hit the paddle!
            #self.score += 1 # hurray!
            self.dotDx = -self.dotDx
            self.ballWidth = self.ballWidth + self.ballRadius
            dToMiddleY = self.ballHeight - (self.ballHeight - self.ballRadius + self.ballHeight + self.ballRadius)/2
            dampeningFactor = 3 # smaller = more extreme bounces
            self.dotDy = dToMiddleY / dampeningFactor



    def ballIntersects(self):
        return (self.dot1Width < self.ballWidth < self.dot1Width + 40 
        or self.dot1Height - 40 < self.ballHeight < self.dot1Height or
        self.dot2Width < self.ballWidth < self.dot2Width + 40  
        or self.dot2Height-40 < self.ballHeight < self.dot2Height)
    
    def drawCourt(self, canvas):
        canvas.create_rectangle(0,0,self.width,self.height,fill = "#ffeeda")
        canvas.create_image(self.width/2, self.height/2 + 30, image = ImageTk.PhotoImage(self.courtimage))

    def drawScoreBoard(self, canvas):
        canvas.create_rectangle(self.width/2 +300, 10, self.width/2 - 300, 100,
                            fill = "#f49030", width = 3)
        canvas.create_text(self.width/2, 55, text = f"{self.score1} - {self.score2}", font = "Arial 40 bold")

    def drawTeam1(self, canvas):
        canvas.create_oval(self.dot1Width, self.dot1Height, self.dot1Width + 40, self.dot1Height - 40, fill = "red")

    def drawTeam2(self, canvas):
        canvas.create_oval(self.dot2Width, self.dot2Height, self.dot2Width + 40, self.dot2Height - 40, fill = "blue")

    def drawVolleyBall(self, canvas):
        '''canvas.create_oval(self.ballWidth-self.ballRadius, 
            self.ballHeight-self.ballRadius, self.ballWidth+self.ballRadius, 
            self.ballHeight+self.ballRadius, fill = "pink")'''
        canvas.create_image(self.ballWidth, self.ballHeight, 
           image=ImageTk.PhotoImage(self.volleyballImage))

    def redrawAll(self, canvas):
        Match.drawCourt(self, canvas)
        Match.drawScoreBoard(self, canvas)
        #for now, have score be increased whenever the ball lands not in where player's head is
        #On the left side of the score board, have the Team 1 flag/icon in the background
        #canvas.create_image(width1, width2, image = ImageTk.PhotoImage(self.player1Country))
        canvas.create_text(self.width/2 - 450, 55, text = f"{self.Team1}", font = "Arial 24 bold")
        #Do the same with Team 2 on the right
        canvas.create_text(self.width/2 + 450, 55, text = f"{self.Team2}", font = "Arial 24 bold")
        Match.drawVolleyBall(self, canvas)
        Match.drawTeam1(self, canvas)
        Match.drawTeam2(self, canvas)

class Player(App):
    def __init__(self, playerNumber, country, position, number):
        self.playerNumber = playerNumber
        self.country = country
        self.position = position
        self.number = number
    
    def bump(self):
        #reduce ball velocity, hit it like to front or across court
        #send ball to setter
        pass

    def toss(self):
        #this is default set
        #set to person to the right or middle
        pass

    

        
HomeScreen(width=1366, height=705)

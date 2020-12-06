from cmu_112_graphics import *
from PIL import *
import string, math, random
#from pygame import mixer
from tkinter import *


class HomeScreen(App):
    def appStarted(self):
        self.image1 = self.loadImage('background1.jpg') #Background image for the screen, a person's hand on the volleyball
        self.image2 = self.scaleImage(self.image1, 5)

    def keyPressed(self, event):
        self.counter += 1

    def mousePressed(self, event): 
        if event.x >= self.width/2-125 and event.x <= self.width/2+125:
            if event.y >= self.height/2 - 25 and event.y <= self.height/2 + 25:
                MatchOptions(width=1920, height=1080)
            if event.y >= self.height/2 + 75 and event.y <= self.height/2 + 125:
                Tutorials(width = 1920, height = 1080)
            if  self.height/2 + 175 <= event.y <= self.height/2 + 225:
                Controls(width = 1920, height = 1080)


    def redrawAll(self, canvas):
        canvas.create_rectangle(0,0,self.width,self.height, fill = "#ffeeda")
        canvas.create_image(self.width/2, self.height/2, image=ImageTk.PhotoImage(self.image1))
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
        self.boxFillSelected = "#008080"
        self.boxFillStandard = "#f49030"
        self.image1 = self.loadImage('haikyuubackground2.jpg') #A background of characters playing volleyball
        #Have button change color later

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
    PlayerCount = 0
    Difficulty = "Easy"


    def mousePressed(self, event):
        #### Number of Players ####
        #when clicking on the 1 box
        if event.y >= self.height/2 - 25 and event.y <= self.height/2 + 25:
            if event.x >= self.width/4 and event.x <= int(self.width/3):
                MatchOptions.PlayerCount = 1
        #when clicking on the 2 box
        if event.y >= self.height/2 - 25 and event.y <= self.height/2 + 25:
            if event.x >= int(self.width/3) and event.x <= int(self.width* 5/12):
                MatchOptions.PlayerCount = 2
        #when clicking on the 6 box
        if event.y >= self.height/2 - 25 and event.y <= self.height/2 + 25:
            if event.x >= int(self.width* 5/12) and event.x <= self.width/2:
                MatchOptions.PlayerCount = 6       
        #### Difficulty ####
        #when clicking on the 1 box
        if event.y >= self.height/2 + 75 and event.y <= self.height/2 + 125:
            if event.x >= self.width/4 and event.x <= int(self.width/3):
                MatchOptions.Difficulty = "Easy"
        #when clicking on the 2 box
        if event.y >= self.height/2 + 75 and event.y <= self.height/2 + 125:
            if event.x >= int(self.width/3) and event.x <= int(self.width* 5/12):
                MatchOptions.Difficulty = "Medium"
        #when clicking on the 6 box
        if event.y >= self.height/2 + 75 and event.y <= self.height/2 + 125:
            if event.x >= int(self.width* 5/12) and event.x <= self.width/2:
                MatchOptions.Difficulty = "Hard"     
        #Continue is pressed
        if event.y >= self.height - 100 and event.y <= self.height - 50:
            if event.x >= self.width - 120 and event.x <= self.width - 20:
                Sides(width=1920, height=1080)
    
    def drawTitle(self, canvas):
        #Title
        canvas.create_rectangle(self.width/2 +500, 10, self.width/2 - 500, 160,
                            fill = "#f49030", width = 3)
        canvas.create_text(self.width/2, 85, text = "Match Options", font = "Arial 40 bold")


    def drawPlayerCount(self, canvas):
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


    def drawDifficulty(self, canvas):
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

    def drawContinueButton(self, canvas):
        #Continue
        canvas.create_rectangle(self.width-120, self.height - 100, self.width-20, self.height-50, fill = "#f49030", width = 2)
        canvas.create_text(self.width-70, self.height-75, text = "Continue", font = "Arial 18 bold")

    def redrawAll(self, canvas):
        canvas.create_rectangle(0,0,self.width,self.height,fill = "#ffeeda")
        canvas.create_image(self.width/2, self.height/2, image=ImageTk.PhotoImage(self.image1))
        MatchOptions.drawTitle(self, canvas)
        MatchOptions.drawPlayerCount(self, canvas)
        MatchOptions.drawDifficulty(self, canvas)
        MatchOptions.drawContinueButton(self, canvas)
    

class Sides(App):
    #In this code, we want the different players to select a certain side of the match,
    #so that it could be a 1 v 1 or 2 v AI
    playersInTeam1 = []
    playersInTeam2 = []
    team1Text = ""
    team2Text = ""
    def appStarted(self):
        self.Player1 = "player1"
        self.Player2 = "player2"
        self.imageNum1 = self.loadImage("number1.png") #The player1 icon
        self.imageNum2 = self.loadImage("number2.png") #The player 2 icon
        self.PlayerIcon1 = self.scaleImage(self.imageNum1, .07)
        self.PlayerIcon2 = self.scaleImage(self.imageNum2, .07)
        self.Teamlist = MatchOptions.Teamlist
        self.Team1 = MatchOptions.Team1
        self.Team2 = MatchOptions.Team2
        self.player1X = self.width/2
        self.player1Y = self.height/2 + 30
        self.player2X = self.width/2
        self.player2Y = self.height/2 + 100
        self.Team1List = ",".join(Sides.playersInTeam1)
        self.Team2List = ",".join(Sides.playersInTeam2)
        self.image1 = self.loadImage('brazilVolley.jpg') #The background screen of a Brazilian volleyball player

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
                Match(width=1920, height=1080)



    def redrawAll(self, canvas):
        canvas.create_rectangle(0,0,self.width,self.height,fill = "#ffeeda")
        canvas.create_image(self.width/2, self.height/2, image=ImageTk.PhotoImage(self.image1))
        #Title
        canvas.create_rectangle(self.width/2 +500, 10, self.width/2 - 500, 160,
                            fill = "#f49030", width = 3)
        canvas.create_text(self.width/2, 85, text = "Choose Sides", font = "Arial 40 bold")
        #Continue
        canvas.create_rectangle(self.width-120, self.height - 100, self.width-20, self.height-50, fill = "#f49030", width = 2)
        canvas.create_text(self.width-70, self.height-75, text = "Continue", font = "Arial 18 bold")
        #canvas.create_text(self.width/4, self.height/2 - 50, text = f'{self.Team1}', font = "Arial 25 bold")
        #canvas.create_text((self.width * 3/4), self.height/2 - 50, text = f'{self.Team2}', font = "Arial 25 bold")
        canvas.create_text(self.width/2 - 450, 200, text = f"{self.Team1}", font = "Arial 30 bold")
        #Do the same with Team 2 on the right
        canvas.create_text(self.width/2 + 450, 200, text = f"{self.Team2}", font = "Arial 30 bold")
        canvas.create_image(self.player1X, self.player1Y, image=ImageTk.PhotoImage(self.PlayerIcon1))
        canvas.create_image(self.player2X, self.player2Y, image=ImageTk.PhotoImage(self.PlayerIcon2))

        
        if self.playersInTeam1 == []:
            Sides.team1Text = "CPU"
            #now make team1 have only AI's 
        else:
            Sides.team1Text = ", ".join(self.playersInTeam1)
        if self.playersInTeam2 == []:
            Sides.team2Text = "CPU"
            #now make team2 have only AI's 
        else:
            Sides.team2Text = ", ".join(self.playersInTeam2)
        canvas.create_text(self.width/2, self.height - 70, 
                text = f"Team {self.Team1}: " + Sides.team1Text, font = "Arial 30 bold", fill = "#B53737")
        canvas.create_text(self.width/2, self.height - 30, 
                text = f"Team {self.Team2}: " + Sides.team2Text, font = "Arial 30 bold", fill = "#1338BE")


class Match(App):
    score1 = 0
    score2 = 0
    def appStarted(self):
        self.gameReset = False
        Match.resetApp(self)
        self.gageActivates = False
    
    def resetApp(self):
        # This is a helper function for Controllers
        # This initializes most of our model (stored in app.xyz)
        # This is called when they start the app, and also after
        # the game is over when we restart the app.
        self.notServed = True
        self.rallyStarts = False
        self.gageValue = 0
        self.gageSD = 0
        self.serveOption = 0
        self.topCount = 0
        self.bottomCount = 0
        self.rowCount = 0
        self.row2Count = 0
        self.top2Count = 0
        self.bottom2Count = 0
        self.dotOutline = "green"
        self.timerDelay = 50 # milliseconds
        self.waitingForKeyPress = True
        self.gameOver = False
        self.paused = False
        self.servingSide = 1
        self.touchCount = 0
        self.team1TouchCount = 0
        self.team2TouchCount = 0
        self.serveGoesOverNet = False
        self.gapsTeam1 = []
        self.gapsTeam2 = []
        Match.resetTeams(self)
        Match.resetCourt(self)
        Match.resetPlayer1(self)
        Match.resetPlayer2(self)
        Match.resetBall(self)
        if MatchOptions.Difficulty == "Easy":
            self.ballSpeed = 10
        elif MatchOptions.Difficulty == "Intermediate":
            self.ballSpeed = 15
        else:
            self.ballSpeed = 30
        Match.resetGage(self)

    
    def resetTeams(self):
        self.imageNum1 = self.loadImage("number1.png") #Player 1 icon
        self.imageNum2 = self.loadImage("number2.png") #Player 2 Icon
        self.PlayerIcon1 = self.scaleImage(self.imageNum1, 2/3)
        self.PlayerIcon2 = self.scaleImage(self.imageNum2, 2/3)
        self.Team1 = MatchOptions.Team1
        self.Team2 = MatchOptions.Team2

    def resetCourt(self):
        self.imageCourt = self.loadImage("court2dtransparent.png") #picture of the court
        self.courtimage = self.scaleImage(self.imageCourt, 2.2)
        self.ballimage = self.loadImage("volleyballimage.png") #picture of volleyball
        self.volleyballImage = self.scaleImage(self.ballimage, .04)
        self.courtNetX = self.width/2
        self.courtNetBottom = self.height - 750
        self.courtNetTop = self.height - 250
        self.topLineXR = self.width - 300
        self.topLineXL = self.width - 1600
        self.topLineY = self.height - 750
        self.bottomLineR = self.width - 300
        self.bottomLineL = self.width - 1600
        self.bottomLineY = self.height - 250

    def resetBall(self):
        # This is a helper function for Controllers
        # Get the dot ready for the next round.  Move the dot to
        # the center of the screen and give it an initial velocity.
        self.ballWidth = self.bottomLineL-30
        self.ballHeight = self.bottomLineY - 50
        self.ballRadius = 15
        self.dotDx = -10
        self.dotDy = -3
        self.originalDx = -10
        self.originalDy = -3
        self.dotGageDx = -5 #Switch speed of this for different difficulties
        self.dotGageDy = -5
    
    def resetPlayer1(self):
        #### 1 Player #####
        if self.servingSide != 1:
            self.dot1Width = self.width/2-90
            self.dot1Height = self.height/2 + 50
            self.dot2Width = self.topLineXR + 90
            self.dot2Height = self.bottomLineY - 50
        else:
            self.dot1Width = self.bottomLineL-90
            self.dot1Height = self.bottomLineY - 50

        #### 2 Players ####
        if self.servingSide != 1:
            self.dot1WidthFront = self.width/2-90
            self.dot1HeightFront = self.height/2 + 50
            self.dot1WidthBack = self.width/2-380
            self.dot1HeightBack = self.height/2 + 50

        else:
            self.dot1WidthFront = self.width/2-90
            self.dot1HeightFront = self.height/2 + 50
            self.dot1WidthBack = self.bottomLineL-90
            self.dot1HeightBack =  self.bottomLineY - 50
        
        #### 6 Players ####
        if self.servingSide != 1:
            self.player1WidthTM = self.width/2-90
            self.player1HeightTM = self.height/2 + 50
            self.player1WidthTL = self.width/2-90
            self.player1HeightTL = self.height/2 - 70
            self.player1WidthTR = self.width/2 - 90
            self.player1HeightTR = self.height/2 + 210
            self.player1WidthBM = self.width/2-380
            self.player1HeightBM = self.height/2 + 50
            self.player1WidthBL = self.width/2-380
            self.player1HeightBL = self.height/2 - 70
            self.player1WidthBR = self.width/2-380
            self.player1HeightBR = self.height/2 + 210


        else:
            self.player1WidthTM = self.width/2-90
            self.player1HeightTM = self.height/2 + 50
            self.player1WidthTL = self.width/2-90
            self.player1HeightTL = self.height/2 - 70
            self.player1WidthTR = self.width/2 - 90
            self.player1HeightTR = self.height/2 + 210
            self.player1WidthBM = self.width/2-380
            self.player1HeightBM = self.height/2 + 50
            self.player1WidthBL = self.width/2-380
            self.player1HeightBL = self.height/2 - 70
            self.player1WidthBR = self.bottomLineL-90
            self.player1HeightBR = self.bottomLineY - 50

    def resetPlayer2(self):
        #### 1 Player #####
        if self.servingSide != 1:
            self.dot2Width = self.topLineXR + 90
            self.dot2Height = self.bottomLineY - 50
        else:
            self.dot2Width = self.width/2+90
            self.dot2Height = self.height/2 + 50

        #### 2 Players ####
        if self.servingSide != 1:
            self.dot2WidthFront = self.width/2+90
            self.dot2HeightFront = self.height/2 + 50
            self.dot2WidthBack = self.topLineXR + 90
            self.dot2HeightBack = self.bottomLineY - 50
        else:
            self.dot2WidthFront = self.width/2+90
            self.dot2HeightFront = self.height/2 + 50
            self.dot2WidthBack = self.width/2+300
            self.dot2HeightBack = self.height/2 + 50


        #### 6 Players ####
        if self.servingSide != 1:
            self.player2WidthTM = self.width/2+90
            self.player2HeightTM = self.height/2 + 50
            self.player2WidthTL = self.width/2+90
            self.player2HeightTL = self.height/2 - 70
            self.player2WidthTR = self.width/2+90
            self.player2HeightTR = self.height/2 + 170
            self.player2WidthBM = self.width/2+300
            self.player2HeightBM = self.height/2 + 50
            self.player2WidthBL = self.width/2+300
            self.player2HeightBL = self.height/2 - 70
            self.player2WidthBR = self.topLineXR + 90
            self.player2HeightBR = self.bottomLineY - 50
        else:
            self.player2WidthTM = self.width/2+90
            self.player2HeightTM = self.height/2 + 50
            self.player2WidthTL = self.width/2+90
            self.player2HeightTL = self.height/2 - 70
            self.player2WidthTR = self.width/2+90
            self.player2HeightTR = self.height/2 + 170
            self.player2WidthBM = self.width/2+300
            self.player2HeightBM = self.height/2 + 50
            self.player2WidthBL = self.width/2+300
            self.player2HeightBL = self.height/2 - 70
            self.player2WidthBR = self.width/2+300
            self.player2HeightBR = self.height/2 + 170

    def resetGage(self):
        self.gageX0_1 = self.dot1Width - 80
        self.gageX1_1 = self.gageX0_1 + 30
        self.gageY0_1 = self.dot1Height - 180
        self.gageY1_1 = self.dot1Height + 180
        self.gageDotWidth = self.gageX0_1 + (self.gageX1_1 - self.gageX0_1)/2
        self.gageDotHeight = self.dot1Height
        self.gageDotRadius = 15
        self.gagePressCount = 0
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
        if (not self.paused): #and not self.notServed
            Match.doStep(self)

    def doStep(self):
        if self.notServed == False:
            Match.doGage(self)
        elif self.rallyStarts == True and not self.gameOver:
            Match.moveBall(self)
            Match.doMoveP2AI(self)
            Match.doMoveP1AI(self)
    def doGage(self):
        if self.gageActivates == True:
            Match.moveGageDot(self)
    def doMoveP2AI(self):
        if Sides.playersInTeam2 == []:
            Match.movePlayer2AI(self)

    def doMoveP1AI(self):
        if Sides.playersInTeam1 == []:
            if self.touchCount > 0:
                Match.movePlayer1AI(self)
    
    def keyPressed(self, event):
        if self.gameReset:
            Match.resetApp(self)
            self.gameReset = False
        elif self.gameOver:
            MatchIsOver(width = 1920, height = 1028)
        elif self.waitingForKeyPress:
            self.waitingForKeyPress = False
        if event.key == "q":
            #switch control to the player to the left of the current one in back row
            self.rowCount = 1
            self.topCount += 1
        elif event.key == "e":
            #switch control to the player to the left of the current one in front row
            self.bottomCount += 1
            self.rowCount = 0
        if event.key == "j":
            self.row2Count = 1
            self.top2Count += 1
        elif event.key == "l":
            self.bottom2Count += 1
            self.row2Count = 0
        if event.key == 'a':
            #current player moves left
            #### 1 player ####
            if MatchOptions.PlayerCount == 1:            
                self.dot1Width -= 25
            #### 2 players ####
            elif MatchOptions.PlayerCount == 2:
                if self.topCount % 2 == 1:
                    self.dot1WidthFront -= 25
                else:
                    self.dot1WidthBack -= 25
            #### 6 players ####
            else:
                if self.rowCount %2 == 1:
                    if self.topCount % 3 == 0:
                        self.player1WidthTL -= 25
                    elif self.topCount % 3 == 1:
                        self.player1WidthTM -= 25
                    elif self.topCount % 3 == 2:
                        self.player1WidthTR -= 25
                else:
                    if self.bottomCount % 3 == 0:
                        self.player1WidthBL -= 25
                    elif self.bottomCount % 3 == 1:
                        self.player1WidthBM -= 25
                    elif self.bottomCount % 3 == 2:
                        self.player1WidthBR -= 25
        elif event.key == 'd':
            #current player moves right
            #### 1 player ####1
            if MatchOptions.PlayerCount == 1:            
                self.dot1Width += 25
            #### 2 players ####
            elif MatchOptions.PlayerCount == 2:
                if self.topCount % 2 == 1:
                    self.dot1WidthFront += 25
                else:
                    self.dot1WidthBack += 25
            #### 6 players ####
            else:
                if self.rowCount % 2 == 1:
                    if self.topCount % 3 == 0:
                        self.player1WidthTL += 25
                    elif self.topCount % 3 == 1:
                        self.player1WidthTM += 25
                    elif self.topCount % 3 == 2:
                        self.player1WidthTR += 25
                else:
                    if self.bottomCount % 3 == 0:
                        self.player1WidthBL += 25
                    elif self.bottomCount % 3 == 1:
                        self.player1WidthBM += 25
                    elif self.bottomCount % 3 == 2:
                        self.player1WidthBR += 25
            
        elif event.key == "s":
            #### 1 player ####1
            if MatchOptions.PlayerCount == 1:            
                self.dot1Height += 25
            #### 2 players ####
            elif MatchOptions.PlayerCount == 2:
                if self.topCount % 2 == 1:
                    self.dot1HeightFront += 25
                else:
                    self.dot1HeightBack += 25
            #### 6 players ####
            else:
                if self.rowCount % 2 == 1:
                    if self.topCount % 3 == 0:
                        self.player1HeightTL += 25
                    elif self.topCount % 3 == 1:
                        self.player1HeightTM += 25
                    elif self.topCount % 3 == 2:
                        self.player1HeightTR += 25
                else:
                    if self.bottomCount % 3 == 0:
                        self.player1HeightBL += 25
                    elif self.bottomCount % 3 == 1:
                        self.player1HeightBM += 25
                    elif self.bottomCount % 3 == 2:
                        self.player1HeightBR += 25
        elif event.key == "w":
            #### 1 player ####1
            if MatchOptions.PlayerCount == 1:            
                self.dot1Height -= 25
            #### 2 players ####
            elif MatchOptions.PlayerCount == 2:
                if self.topCount % 2 == 1:
                    self.dot1HeightFront -= 25
                else:
                    self.dot1HeightBack -= 25
            #### 6 players ####
            else:
                if self.rowCount % 2 == 1:
                    if self.topCount % 3 == 0:
                        self.player1HeightTL -= 25
                    elif self.topCount % 3 == 1:
                        self.player1HeightTM -= 25
                    elif self.topCount % 3 == 2:
                        self.player1HeightTR -= 25
                else:
                    if self.bottomCount % 3 == 0:
                        self.player1HeightBL -= 25
                    elif self.bottomCount % 3 == 1:
                        self.player1HeightBM -= 25
                    elif self.bottomCount % 3 == 2:
                        self.player1HeightBR -= 25

        if event.key == 'Left':
            #### 1 player ####
            if MatchOptions.PlayerCount == 1:            
                self.dot2Width -= 15
            #### 2 players ####
            elif MatchOptions.PlayerCount == 2:
                if self.top2Count % 2 == 1:
                    self.dot2WidthFront -= 15
                else:
                    self.dot2WidthBack -= 15
            #### 6 players ####
            else:
                if self.row2Count %2 == 1:
                    if self.top2Count % 3 == 0:
                        self.player2WidthTL -= 15
                    elif self.top2Count % 3 == 1:
                        self.player2WidthTM -= 15
                    elif self.top2Count % 3 == 2:
                        self.player2WidthTR -= 15
                else:
                    if self.bottom2Count % 3 == 0:
                        self.player2WidthBL -= 15
                    elif self.bottom2Count % 3 == 1:
                        self.player2WidthBM -= 15
                    elif self.bottom2Count % 3 == 2:
                        self.player2WidthBR -= 15
        elif event.key == 'Right':
            #### 1 player ####
            if MatchOptions.PlayerCount == 1:            
                self.dot2Width += 15
            #### 2 players ####
            elif MatchOptions.PlayerCount == 2:
                if self.top2Count % 2 == 1:
                    self.dot2WidthFront += 15
                else:
                    self.dot2WidthBack += 15
            #### 6 players ####
            else:
                if self.row2Count %2 == 1:
                    if self.top2Count % 3 == 0:
                        self.player2WidthTL += 15
                    elif self.top2Count % 3 == 1:
                        self.player2WidthTM += 15
                    elif self.top2Count % 3 == 2:
                        self.player2WidthTR += 15
                else:
                    if self.bottom2Count % 3 == 0:
                        self.player2WidthBL += 15
                    elif self.bottom2Count % 3 == 1:
                        self.player2WidthBM += 15
                    elif self.bottom2Count % 3 == 2:
                        self.player2WidthBR += 15
        elif event.key == "Down":
            #### 1 player ####
            if MatchOptions.PlayerCount == 1:            
                self.dot2Height += 15
            #### 2 players ####
            elif MatchOptions.PlayerCount == 2:
                if self.top2Count % 2 == 1:
                    self.dot2HeightFront += 15
                else:
                    self.dot2HeightBack += 15
            #### 6 players ####
            else:
                if self.row2Count % 2 == 1:
                    if self.top2Count % 3 == 0:
                        self.player2HeightTL += 15
                    elif self.top2Count % 3 == 1:
                        self.player2HeightTM += 15
                    elif self.top2Count % 3 == 2:
                        self.player2HeightTR += 15
                else:
                    if self.bottom2Count % 3 == 0:
                        self.player2HeightBL += 15
                    elif self.bottom2Count % 3 == 1:
                        self.player2HeightBM += 15
                    elif self.bottom2Count % 3 == 2:
                        self.player2HeightBR += 15
        elif event.key == "Up":
            #### 1 player ####1
            if MatchOptions.PlayerCount == 1:            
                self.dot2Height -= 15
            #### 2 players ####
            elif MatchOptions.PlayerCount == 2:
                if self.top2Count % 2 == 1:
                    self.dot2HeightFront -= 15
                else:
                    self.dot2HeightBack -= 15
            #### 6 players ####
            else:
                if self.row2Count % 2 == 1:
                    if self.top2Count % 3 == 0:
                        self.player2HeightTL -= 15
                    elif self.top2Count % 3 == 1:
                        self.player2HeightTM -= 15
                    elif self.top2Count % 3 == 2:
                        self.player2HeightTR -= 15
                else:
                    if self.bottom2Count % 3 == 0:
                        self.player2HeightBL -= 15
                    elif self.bottom2Count % 3 == 1:
                        self.player2HeightBM -= 15
                    elif self.bottom2Count % 3 == 2:
                        self.player2HeightBR -= 15
        elif event.key == "p":
            #have spike function run
            if self.paused == False:
                self.paused = True
            else:
                self.paused = False
        elif event.key == "r":
            self.gameReset = True
        elif event.key == "0":
            self.gameOver = True
        elif event.key == "o":
            self.gageActivates = not self.gageActivates
            self.notServed = not self.notServed
            self.gagePressCount += 1
            if self.gagePressCount % 2==0 and self.gagePressCount > 0:
                Match.resetGage(self)
        elif event.key == "Space":
            self.gageActivates = not self.gageActivates
            Match.gageDotPositioncalculator(self)
            self.notServed = not self.notServed
        elif event.key == "1":
            self.serveOption = 1
            Match.topSpinServe(self,event)
        elif event.key == "2":
            self.serveOption = 2
            Match.topSpinServe(self,event)
        elif event.key == "3":
            Match.floaterServe(self,event)
        elif event.key == "4":
            Match.toss(self)
        elif event.key == "5":
            Match.spike(self)
    '''def mousePressed(self, event):
        #Continue button is pressed
        pass
    def moveIconToRight(self):
        pass'''

    def mousePressed(self, event):
        if event.x >= self.width/2 - 90 and event.x <= self.width/2 + 90:
            if event.y >= self.height/2 - 160 and event.y <= self.height/2 - 100:
                Match.resetApp(self)
            if event.y >= self.height/2 - 60 and event.y <= self.height/2:
                MatchOptions(width=1920, height=1080)
            if event.y >= self.height/2 + 40 and event.y <= self.height/2 + 100:
                HomeScreen(width=1920, height=1080)

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
        elif Match.ballIntersectsTeam1(self):
            if MatchOptions.PlayerCount == 1:
                self.dotDx = -self.originalDx
                self.ballWidth = self.dot1Width + 40 + self.ballRadius
                dToMiddleY = self.ballHeight - (self.dot1Height-40 + self.dot1Height)/2
                dampeningFactor = 3 # smaller = more extreme bounces
                self.dotDy = dToMiddleY / dampeningFactor
            elif MatchOptions.PlayerCount == 2:
                if (self.dot1WidthFront < self.ballWidth < self.dot1WidthFront + 40  
                        and self.dot1HeightFront-40 < self.ballHeight < self.dot1HeightFront):
                    self.dotDx = -self.originalDx * .15
                    self.ballWidth = self.dot1WidthFront + 40 + self.ballRadius
                    dToMiddleY = self.ballHeight - (self.dot1HeightFront-40 + self.dot1HeightFront)/2
                    dampeningFactor = 3 # smaller = more extreme bounces
                    self.dotDy = dToMiddleY / dampeningFactor
                    self.touchCount += 1
                    self.team1TouchCount += 1
                else:
                    self.dotDx = -self.originalDx * .15
                    self.ballWidth = self.dot1WidthBack + 40 + self.ballRadius
                    dToMiddleY = self.ballHeight - (self.dot1HeightBack-40 + self.dot1HeightBack)/2
                    dampeningFactor = 3 # smaller = more extreme bounces
                    self.dotDy = dToMiddleY / dampeningFactor
                    self.touchCount += 1
                    self.team1TouchCount += 1
            elif MatchOptions.PlayerCount == 6:
                if ((self.player1WidthTL < self.ballWidth < self.player1WidthTL + 40  
                    and self.player1HeightTL-40 < self.ballHeight < self.player1HeightTL) or 
                    (self.player1WidthTM < self.ballWidth < self.player1WidthTM + 40  
                    and self.player1HeightTM-40 < self.ballHeight < self.player1HeightBM) or 
                    (self.player1WidthTR < self.ballWidth < self.player1WidthTR + 40  
                    and self.player1HeightTR-40 < self.ballHeight < self.player1HeightTR)):
                    self.dotDx = -self.originalDx * .15

                    if (self.player1WidthTL < self.ballWidth < self.player1WidthTL + 40  
                    and self.player1HeightTL-40 < self.ballHeight < self.player1HeightTL):
                        self.ballWidth = self.player1WidthTL - self.ballRadius
                        dToMiddleY = self.ballHeight - (self.player1HeightTL-40 + self.player1HeightTL)/2
                    if (self.player1WidthTM < self.ballWidth < self.player1WidthTM + 40  
                    and self.player1HeightTM-40 < self.ballHeight < self.player1HeightTM):
                        self.ballWidth = self.player1WidthTM - self.ballRadius
                        dToMiddleY = self.ballHeight - (self.player1HeightTM-40 + self.player1HeightTM)/2
                    if (self.player1WidthTR < self.ballWidth < self.player1WidthTR + 40  
                    and self.player1HeightTR-40 < self.ballHeight < self.player1HeightTR):
                        self.ballWidth = self.player1WidthTR - self.ballRadius
                        dToMiddleY = self.ballHeight - (self.player1HeightTR-40 + self.player1HeightTR)/2

                    dampeningFactor = 3 # smaller = more extreme bounces
                    self.dotDy = dToMiddleY / dampeningFactor
                    self.touchCount += 1
                    self.team1TouchCount += 1
                elif ((self.player1WidthBL < self.ballWidth < self.player1WidthBL + 40  
                    and self.player1HeightBL-40 < self.ballHeight < self.player1HeightBL) or 
                    (self.player1WidthBM < self.ballWidth < self.player1WidthBM + 40  
                    and self.player1HeightBM-40 < self.ballHeight < self.player1HeightBM) or 
                    (self.player1WidthBR < self.ballWidth < self.player1WidthBR + 40  
                    and self.player1HeightBR-40 < self.ballHeight < self.player1HeightBR)):
                    self.dotDx = -self.originalDx * .15

                    if (self.player1WidthBL < self.ballWidth < self.player1WidthBL + 40  
                    and self.player1HeightBL-40 < self.ballHeight < self.player1HeightBL):
                        self.ballWidth = self.player1WidthBL - self.ballRadius
                        dToMiddleY = self.ballHeight - (self.player1HeightBL-40 + self.player1HeightBL)/2
                    if (self.player1WidthBM < self.ballWidth < self.player1WidthBM + 40  
                    and self.player1HeightBM-40 < self.ballHeight < self.player1HeightBM):
                        self.ballWidth = self.player1WidthBM - self.ballRadius
                        dToMiddleY = self.ballHeight - (self.player1HeightBM-40 + self.player1HeightBM)/2
                    if (self.player1WidthBR < self.ballWidth < self.player1WidthBR + 40  
                    and self.player1HeightBR-40 < self.ballHeight < self.player1HeightBR):
                        self.ballWidth = self.player1WidthBR - self.ballRadius
                        dToMiddleY = self.ballHeight - (self.player1HeightBR-40 + self.player1HeightBR)/2

                    dampeningFactor = 3 # smaller = more extreme bounces
                    self.dotDy = dToMiddleY / dampeningFactor
                    self.touchCount += 1
                    self.team1TouchCount += 1
            if Sides.playersInTeam1 == []:
                    if MatchOptions.Difficulty == "Easy":
                        self.dotDx *= .75
                        self.dotDy *= .75
                    elif MatchOptions.Difficulty == "Hard":
                        self.dotDx *= .9
                        self.dotDy *= .9
                    else:
                        self.dotDx *= 1.5
                        self.dotDy *= 1.5    

            if self.ballWidth > self.width/2:
                self.team1TouchCount = 0
            if self.courtNetBottom <=  self.ballHeight <= self.courtNetTop:
                if ((self.ballWidth + self.ballRadius >= self.width) or 
                    (self.team2TouchCount > 3)):
                    Match.score1 += 1
                    self.gameReset = True
                    self.servingSide = 0
                else:
                    if self.team1TouchCount == 0:
                        Match.score1 += 1
                        self.servingSide = 0
                    if ((self.team1TouchCount > 0 
                    and self.ballHeight + self.ballRadius >= self.height) or
                    (self.ballHeight - self.ballRadius <= 0 and self.team1TouchCount > 0 )):
                        Match.score2 += 1
                        self.servingSide = 1
                    self.gameReset = True


        elif Match.ballIntersectsTeam2(self):
            if MatchOptions.PlayerCount == 1:
                self.dotDx = self.originalDx * .15
                self.ballWidth = self.dot2Width - self.ballRadius
                dToMiddleY = self.ballHeight - (self.dot2Height-40 + self.dot2Height)/2
                dampeningFactor = 3 # smaller = more extreme bounces
                self.dotDy = dToMiddleY / dampeningFactor
            elif MatchOptions.PlayerCount == 2:
                if (self.dot2WidthFront < self.ballWidth < self.dot2WidthFront + 40  
                        and self.dot2HeightFront-40 < self.ballHeight < self.dot2HeightFront):
                    self.dotDx = self.originalDx * .15
                    self.ballWidth = self.dot2WidthFront - self.ballRadius
                    dToMiddleY = self.ballHeight - (self.dot2HeightFront-40 + self.dot2HeightFront)/2
                    dampeningFactor = 3 # smaller = more extreme bounces
                    self.dotDy = dToMiddleY / dampeningFactor
                    self.touchCount += 1
                    self.team2TouchCount += 1
                else:
                    self.dotDx = self.originalDx * .15
                    self.ballWidth = self.dot2WidthBack - self.ballRadius
                    dToMiddleY = self.ballHeight - (self.dot2HeightBack-40 + self.dot2HeightBack)/2
                    dampeningFactor = 3 # smaller = more extreme bounces
                    self.dotDy = dToMiddleY / dampeningFactor
                    self.touchCount += 1
                    self.team2TouchCount += 1
            elif MatchOptions.PlayerCount == 6:
                if ((self.player2WidthTL < self.ballWidth < self.player2WidthTL + 40  
                    and self.player2HeightTL-40 < self.ballHeight < self.player2HeightTL) or
                    (self.player2WidthTM < self.ballWidth < self.player2WidthTM + 40  
                    and self.player2HeightTM-40 < self.ballHeight < self.player2HeightBM) or
                    (self.player2WidthTR < self.ballWidth < self.player1WidthTR + 40  
                    and self.player2HeightTR-40 < self.ballHeight < self.player2HeightTR)):
                    self.dotDx = self.originalDx * .15

                    if (self.player2WidthTL < self.ballWidth < self.player2WidthTL + 40  
                    and self.player2HeightTL-40 < self.ballHeight < self.player2HeightTL):
                        self.ballWidth = self.player2WidthTL - self.ballRadius
                        dToMiddleY = self.ballHeight - (self.player2HeightTL-40 + self.player2HeightTL)/2
                    if (self.player2WidthTM < self.ballWidth < self.player2WidthTM + 40  
                    and self.player2HeightTM-40 < self.ballHeight < self.player2HeightTM):
                        self.ballWidth = self.player2WidthTL - self.ballRadius
                        dToMiddleY = self.ballHeight - (self.player2HeightTM-40 + self.player2HeightTM)/2
                    if (self.player2WidthTR < self.ballWidth < self.player2WidthTR + 40  
                    and self.player2HeightTR-40 < self.ballHeight < self.player1HeightTR):
                        self.ballWidth = self.player2WidthTR - self.ballRadius
                        dToMiddleY = self.ballHeight - (self.player2HeightTR-40 + self.player2HeightTR)/2

                    dampeningFactor = 3 # smaller = more extreme bounces
                    self.dotDy = dToMiddleY / dampeningFactor
                    self.touchCount += 1
                    self.team2TouchCount += 1
                elif ((self.player2WidthBL < self.ballWidth < self.player2WidthBL + 40  
                    and self.player2HeightBL-40 < self.ballHeight < self.player2HeightBL) or 
                    (self.player2WidthBM < self.ballWidth < self.player2WidthBM + 40  
                    and self.player2HeightBM-40 < self.ballHeight < self.player2HeightBM) or 
                    (self.player2WidthBR < self.ballWidth < self.player2WidthBR + 40  
                    and self.player2HeightBR-40 < self.ballHeight < self.player2HeightBR)):
                    self.dotDx = self.originalDx * .15

                    if (self.player2WidthBL < self.ballWidth < self.player2WidthBL + 40  
                    and self.player2HeightBL-40 < self.ballHeight < self.player2HeightBL):
                        self.ballWidth = self.player2WidthBL - self.ballRadius
                        dToMiddleY = self.ballHeight - (self.player2HeightBL-40 + self.player2HeightBL)/2
                    if (self.player2WidthBM < self.ballWidth < self.player2WidthBM + 40  
                    and self.player2HeightBM-40 < self.ballHeight < self.player2HeightBM):
                        self.ballWidth = self.player2WidthBM - self.ballRadius
                        dToMiddleY = self.ballHeight - (self.player2HeightBM-40 + self.player2HeightBM)/2
                    if (self.player2WidthBR < self.ballWidth < self.player2WidthBR + 40  
                    and self.player2HeightBR-40 < self.ballHeight < self.player2HeightBR):
                        self.ballWidth = self.player2WidthBR - self.ballRadius
                        dToMiddleY = self.ballHeight - (self.player2HeightBR-40 + self.player2HeightBR)/2
                    dampeningFactor = 3 # smaller = more extreme bounces
                    self.dotDy = dToMiddleY / dampeningFactor
                    self.touchCount += 1
                    self.team2TouchCount += 1
            if Sides.playersInTeam2 == []:
                    if MatchOptions.Difficulty == "Easy":
                        self.dotDx *= .75
                        self.dotDy *= .75
                    elif MatchOptions.Difficulty == "Hard":
                        self.dotDx *= .9
                        self.dotDy *= .9
                    else:
                        self.dotDx *= 1.5
                        self.dotDy *= 1.5   

            if self.ballWidth < self.width/2:
                self.team2TouchCount = 0
            if self.ballWidth < self.width/2:
                if ((self.ballWidth - self.ballRadius <= 0) or
                    (self.ballHeight + self.ballRadius >= self.height) or 
                    (self.ballWidth - self.ballRadius <= 0) or 
                    (self.team1TouchCount > 3)):
                    Match.score2 += 1
                    self.gameReset = True
                    self.servingSide = 1

 

    def ballIntersectsTeam1(self):
        if MatchOptions.PlayerCount == 1:
            return ((self.dot1Width <= self.ballWidth <= self.dot1Width + 40) 
            and (self.dot1Height - 40 <= self.ballHeight <= self.dot1Height))
        elif MatchOptions.PlayerCount == 2:
            return ((self.dot1WidthFront < self.ballWidth < self.dot1WidthFront + 40  
            and self.dot1HeightFront-40 < self.ballHeight < self.dot1HeightFront) or 
            (self.dot1WidthBack < self.ballWidth < self.dot1WidthBack + 40  
            and self.dot1HeightBack-40 < self.ballHeight < self.dot1HeightBack))
        elif MatchOptions.PlayerCount == 6:
            return ((self.player1WidthTL < self.ballWidth < self.player1WidthTL + 40  
            and self.player1HeightTL-40 < self.ballHeight < self.player1HeightTL) or 
            (self.player1WidthBL < self.ballWidth < self.player1WidthBL + 40  
            and self.player1HeightBL-40 < self.ballHeight < self.player1HeightBL) or 
            (self.player1WidthTM < self.ballWidth < self.player1WidthTM + 40  
            and self.player1HeightTM-40 < self.ballHeight < self.player1HeightBM) or 
            (self.player1WidthBM < self.ballWidth < self.player1WidthBM + 40  
            and self.player1HeightBM-40 < self.ballHeight < self.player1HeightBM) or 
            (self.player1WidthTR < self.ballWidth < self.player1WidthTR + 40  
            and self.player1HeightTR-40 < self.ballHeight < self.player1HeightTR) or 
            (self.player1WidthBR < self.ballWidth < self.player1WidthBR + 40  
            and self.player1HeightBR-40 < self.ballHeight < self.player1HeightBR))
    
    def ballIntersectsTeam2(self):
        if MatchOptions.PlayerCount == 1:
            return (self.dot2Width < self.ballWidth < self.dot2Width + 40  
            and self.dot2Height-40 < self.ballHeight < self.dot2Height)
        elif MatchOptions.PlayerCount == 2:
            return ((self.dot2WidthFront < self.ballWidth < self.dot2WidthFront + 40  
            and self.dot2HeightFront-40 < self.ballHeight < self.dot2HeightFront) or 
            (self.dot2WidthBack < self.ballWidth < self.dot2WidthBack + 40  
            and self.dot2HeightBack-40 < self.ballHeight < self.dot2HeightBack))
        elif MatchOptions.PlayerCount == 6:
            return ((self.player2WidthTL < self.ballWidth < self.player2WidthTL + 40  
            and self.player2HeightTL-40 < self.ballHeight < self.player2HeightTL) or 
            (self.player2WidthBL < self.ballWidth < self.player2WidthBL + 40  
            and self.player2HeightBL-40 < self.ballHeight < self.player2HeightBL) or 
            (self.player2WidthTM < self.ballWidth < self.player1WidthTM + 40  
            and self.player2HeightTM-40 < self.ballHeight < self.player2HeightBM) or 
            (self.player2WidthBM < self.ballWidth < self.player2WidthBM + 40  
            and self.player2HeightBM-40 < self.ballHeight < self.player2HeightBM) or 
            (self.player2WidthTR < self.ballWidth < self.player2WidthTR + 40  
            and self.player2HeightTR-40 < self.ballHeight < self.player2HeightTR) or 
            (self.player2WidthBR < self.ballWidth < self.player2WidthBR + 40  
            and self.player2HeightBR-40 < self.ballHeight < self.player2HeightBR))

    def moveGageDot(self):
        self.gageDotHeight += self.dotGageDy 
        if (self.gageDotHeight + self.gageDotRadius >= self.gageY0_1 + (self.gageY1_1-self.gageY0_1)): #self.height
                # The dot went off the bottom!
                self.gageDotHeight = self.gageY0_1 + (self.gageY1_1-self.gageY0_1) - self.gageDotRadius
                self.dotGageDy = -self.dotGageDy 
        if (self.gageDotHeight - self.gageDotRadius <= self.gageY0_1): #0
                # The dot went off the top!
                self.gageDotHeight = self.gageY0_1 + self.gageDotRadius
                self.dotGageDy = -self.dotGageDy 

    def gageDotPositioncalculator(self):
        if self.gageActivates == False and self.notServed == False:
            if  (self.gageY0_1 < self.gageDotHeight < self.gageY0_1 + 
                (self.gageY1_1-self.gageY0_1)/12) or (self.gageY0_1 + 
                11*(self.gageY1_1-self.gageY0_1)/12 < self.gageDotHeight <
                self.gageY1_1): #red
                    self.dotDx *= .5
                    self.dotDy *= .5
            elif (self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/12 < self.gageDotHeight 
                    < self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/6) or (self.gageY0_1 + 
                    5*(self.gageY1_1-self.gageY0_1)/6 < self.gageDotHeight < 
                    self.gageY0_1 + 11*(self.gageY1_1-self.gageY0_1)/12): #dark orange
                self.dotDx *= .6
                self.dotDy *= .6

            elif (self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/6 < self.gageDotHeight 
                    < self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/4) or (self.gageY0_1 + 
                    3*(self.gageY1_1-self.gageY0_1)/4 < self.gageDotHeight < self.gageY0_1 + 
                    5*(self.gageY1_1-self.gageY0_1)/6): #light orange
                self.dotDx *= .7
                self.dotDy *= .7

            elif (self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/4 < self.gageDotHeight
                    < self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/3) or (self.gageY0_1 + 
                    2*(self.gageY1_1-self.gageY0_1)/3 < self.gageDotHeight 
                    < self.gageY0_1 + 2*(self.gageY1_1-self.gageY0_1)/3): #Light yellow
                self.dotDx *= .8
                self.dotDy *= .8

            elif (self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/3 < self.gageDotHeight 
                    < self.gageY0_1 + 5*(self.gageY1_1-self.gageY0_1)/12) or (self.gageY0_1 + 
                    7*(self.gageY1_1-self.gageY0_1)/12 < self.gageDotHeight
                    < self.gageY0_1 + 2*(self.gageY1_1-self.gageY0_1)/3): #Dark Yellow
                self.dotDx *= .9
                self.dotDy *= .9

            elif (self.gageY0_1 + 5*(self.gageY1_1-self.gageY0_1)/12 < self.gageDotHeight
                     < self.gageY0_1 + 7*(self.gageY1_1-self.gageY0_1)/12): #Green
                self.dotDx *= 1.1
                self.dotDy *= 1.1


    def movePlayer1AI(self):
            if MatchOptions.PlayerCount == 1:
                if self.dot1Width <self.ballWidth < self.courtNetX: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.dot1Width += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.dot1Width += 5
                    else:
                        self.dot1Width += 3
                elif self.topLineXL <self.ballWidth < self.dot1Width: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.dot1Width -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.dot1Width -= 5
                    else:
                        self.dot1Width -= 3
                if self.courtNetBottom < self.ballHeight < self.dot1Height:
                    if MatchOptions.Difficulty == "Easy":
                        self.dot1Height -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.dot1Height -= 5
                    else:
                        self.dot1Height -= 3
                elif self.dot1Height < self.ballHeight < self.courtNetTop:
                    if MatchOptions.Difficulty == "Easy":
                        self.dot1Height += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.dot1Height += 5
                    else:
                        self.dot1Height += 3
            elif MatchOptions.PlayerCount == 2:
                if self.dot1WidthFront <self.ballWidth < self.courtNetX: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.dot1WidthFront += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.dot1WidthFront += 5
                    else:
                        self.dot1WidthFront += 3
                elif self.dot1WidthBack < self.ballWidth < self.dot1WidthFront:
                    if MatchOptions.Difficulty == "Easy":
                        self.dot1WidthFront -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.dot1WidthFront -= 5
                    else:
                        self.dot1WidthFront -= 3
                if self.dot1WidthBack <self.ballWidth < self.dot1WidthFront: 
                    if MatchOptions.Difficulty == "Easy":
                        self.dot1WidthBack += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.dot1WidthBack += 5
                    else:
                        self.dot1WidthBack += 3
                elif self.topLineXL <self.ballWidth < self.dot1WidthBack: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.dot1WidthBack -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.dot1WidthBack -= 5
                    else:
                        self.dot1WidthBack -= 3
                if self.courtNetBottom < self.ballHeight < self.dot1HeightFront:
                    if MatchOptions.Difficulty == "Easy":
                        self.dot1HeightFront -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.dot1HeightFront -= 5
                    else:
                        self.dot1HeightFront -= 3
                elif self.dot1HeightFront < self.ballHeight < self.courtNetTop:
                    if MatchOptions.Difficulty == "Easy":
                        self.dot1HeightFront += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.dot1HeightFront += 5
                    else:
                        self.dot1HeightFront += 3
                if self.courtNetBottom < self.ballHeight < self.dot1HeightBack:
                    if MatchOptions.Difficulty == "Easy":
                        self.dot1HeightBack -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.dot1HeightBack -= 5
                    else:
                        self.dot1HeightBack -= 3
                elif self.dot1HeightBack < self.ballHeight < self.courtNetTop:
                    if MatchOptions.Difficulty == "Easy":
                        self.dot1HeightBack += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.dot1HeightBack += 5
                    else:
                        self.dot1HeightBack += 3
                if self.team1TouchCount == 0:
                    if Match.ballIntersectsTeam1(self):
                        self.dotDx *= .15
                        self.dotDy *= .15
                elif self.team1TouchCount == 1:
                    if Match.ballIntersectsTeam1(self):
                        Match.toss(self)
                elif self.team1TouchCount == 2:
                    if Match.ballIntersectsTeam1(self):
                        Match.spike(self)             
            elif MatchOptions.PlayerCount == 6:
                if self.player1WidthTL <self.ballWidth < self.courtNetX: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.player1WidthTL += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1WidthTL += 5
                    else:
                        self.player1WidthTL += 3
                elif self.player1WidthBL <self.ballWidth < self.player1WidthTL: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.player1WidthTL -= 1
                        self.player1WidthBL += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1WidthTL -= 5
                        self.player1WidthBL += 5
                    else:
                        self.player1WidthTL -= 3
                        self.player1WidthBL += 3
                elif self.topLineXL <self.ballWidth < self.player1WidthBL: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.player1WidthBL -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1WidthBL -= 5
                    else:
                        self.player1WidthBL -= 3
                if self.player1WidthTM <self.ballWidth < self.courtNetX: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.player1WidthTM += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1WidthTM += 5
                    else:
                        self.player1WidthTM += 3
                elif self.player1WidthBM <self.ballWidth < self.player1WidthTM: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.player1WidthTM -= 1
                        self.player1WidthBM += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1WidthTM -= 5
                        self.player1WidthBM += 5
                    else:
                        self.player1WidthTM -= 3
                        self.player1WidthBM += 3
                elif self.topLineXL <self.ballWidth < self.player1WidthBM: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.player1WidthBM -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1WidthBM -= 5
                    else:
                        self.player1WidthBM -= 3
                if self.player1WidthTR <self.ballWidth < self.courtNetX: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.player1WidthTR += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1WidthTR += 5
                    else:
                        self.player1WidthTR += 3
                elif self.player1WidthBR <self.ballWidth < self.player1WidthTR: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.player1WidthTR -= 1
                        self.player1WidthBR += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1WidthTR -= 5
                        self.player1WidthBR += 5
                    else:
                        self.player1WidthTR -= 3
                        self.player1WidthBR += 3
                elif self.topLineXL <self.ballWidth < self.player1WidthBR: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.player1WidthBR -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1WidthBR -= 5
                    else:
                        self.player1WidthBR -= 3
                if self.courtNetBottom < self.ballHeight < self.player1HeightTM:
                    if MatchOptions.Difficulty == "Easy":
                        self.player1HeightTM -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1HeightTM -= 5
                    else:
                        self.player1HeightTM -= 3
                elif self.player1HeightTM < self.ballHeight < self.courtNetTop:
                    if MatchOptions.Difficulty == "Easy":
                        self.player1HeightTM += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1HeightTM += 5
                    else:
                        self.player1HeightTM += 3
                if self.courtNetBottom < self.ballHeight < self.player1HeightTL:
                    if MatchOptions.Difficulty == "Easy":
                        self.player1HeightTL -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1HeightTL -= 5
                    else:
                        self.player1HeightTL -= 3
                elif self.player1HeightTL < self.ballHeight < self.courtNetTop:
                    if MatchOptions.Difficulty == "Easy":
                        self.player1HeightTL += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1HeightTL += 5
                    else:
                        self.player1HeightTL += 3
                if self.courtNetBottom < self.ballHeight < self.player1HeightTR:
                    if MatchOptions.Difficulty == "Easy":
                        self.player1HeightTR -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1HeightTR -= 5
                    else:
                        self.player1HeightTR -= 3
                elif self.player1HeightTR < self.ballHeight < self.courtNetTop:
                    if MatchOptions.Difficulty == "Easy":
                        self.player1HeightTR += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1HeightTR += 5
                    else:
                        self.player1HeightTR += 3
                if self.courtNetBottom < self.ballHeight < self.player1HeightBR:
                    if MatchOptions.Difficulty == "Easy":
                        self.player1HeightBR -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1HeightBR -= 5
                    else:
                        self.player1HeightBR -= 3
                elif self.player1HeightBR < self.ballHeight < self.courtNetTop:
                    if MatchOptions.Difficulty == "Easy":
                        self.player1HeightBR += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1HeightBR += 5
                    else:
                        self.player1HeightBR += 3
                if self.courtNetBottom < self.ballHeight < self.player1HeightBL:
                    if MatchOptions.Difficulty == "Easy":
                        self.player1HeightBL -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1HeightBL -= 5
                    else:
                        self.player1HeightBL -= 3
                elif self.player1HeightBL < self.ballHeight < self.courtNetTop:
                    if MatchOptions.Difficulty == "Easy":
                        self.player1HeightBL += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1HeightBL += 5
                    else:
                        self.player1HeightBL += 3
                if self.courtNetBottom < self.ballHeight < self.player1HeightBM:
                    if MatchOptions.Difficulty == "Easy":
                        self.player1HeightBM -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1HeightBM -= 5
                    else:
                        self.player1HeightBM -= 3
                elif self.player1HeightBM < self.ballHeight < self.courtNetTop:
                    if MatchOptions.Difficulty == "Easy":
                        self.player1HeightBM += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player1HeightBM += 5
                    else:
                        self.player1HeightBM += 3
                if self.ballWidth > self.width/2:
                    Match.resetPlayer1(self)


    def movePlayer2AI(self):
        if MatchOptions.PlayerCount == 1:
            if self.courtNetX <self.ballWidth < self.dot2Width: #If the ball is on the left side of the player on screen
                if MatchOptions.Difficulty == "Easy":
                    self.dot2Width -= 2
                elif MatchOptions.Difficulty == "Hard":
                    self.dot2Width -= 7
                else:
                    self.dot2Width -= 5
            elif self.dot2Width <self.ballWidth < self.topLineXR: #If the ball is on the left side of the player on screen
                if MatchOptions.Difficulty == "Easy":
                    self.dot2Width += 2
                elif MatchOptions.Difficulty == "Hard":
                        self.dot2Width += 7
                else:
                        self.dot2Width += 5
            if self.courtNetBottom < self.ballHeight < self.dot2Height:
                if MatchOptions.Difficulty == "Easy":
                    self.dot2Height -= 2
                elif MatchOptions.Difficulty == "Hard":
                    self.dot2Height -= 7
                else:
                    self.dot2Width -= 5
            elif self.dot2Height < self.ballHeight < self.courtNetTop:
                if MatchOptions.Difficulty == "Easy":
                    self.dot2Height += 2
                elif MatchOptions.Difficulty == "Hard":
                    self.dot2Height += 7
                else:
                    self.dot2Height += 5

        elif MatchOptions.PlayerCount == 2:
            if self.courtNetX <self.ballWidth < self.dot2WidthFront: #If the ball is on the left side of the player on screen
                if MatchOptions.Difficulty == "Easy":
                    self.dot2WidthFront -= 1
                elif MatchOptions.Difficulty == "Hard":
                    self.dot2WidthFront -= 5
                else:
                    self.dot2WidthFront -= 3
            elif self.dot2WidthFront < self.ballWidth < self.dot2WidthBack:
                if MatchOptions.Difficulty == "Easy":
                    self.dot2WidthFront += 1
                elif MatchOptions.Difficulty == "Hard":
                    self.dot2WidthFront += 5
                else:
                    self.dot2WidthFront += 3
            if self.dot2WidthFront <self.ballWidth < self.dot2WidthBack: 
                if MatchOptions.Difficulty == "Easy":
                    self.dot2WidthBack -= 1
                elif MatchOptions.Difficulty == "Hard":
                    self.dot2WidthBack -= 5
                else:
                    self.dot2WidthBack -= 3
            elif self.dot2WidthBack <self.ballWidth < self.topLineXR: #If the ball is on the left side of the player on screen
                if MatchOptions.Difficulty == "Easy":
                    self.dot2WidthBack += 1
                elif MatchOptions.Difficulty == "Hard":
                    self.dot2WidthBack += 5
                else:
                    self.dot2WidthBack += 3
            if self.courtNetBottom < self.ballHeight < self.dot2HeightFront:
                if MatchOptions.Difficulty == "Easy":
                    self.dot2HeightFront -= 1
                elif MatchOptions.Difficulty == "Hard":
                    self.dot2HeightFront -= 5
                else:
                    self.dot2HeightFront -= 3
            elif self.dot2HeightFront < self.ballHeight < self.courtNetTop:
                if MatchOptions.Difficulty == "Easy":
                    self.dot2HeightFront += 1
                elif MatchOptions.Difficulty == "Hard":
                    self.dot2HeightFront += 5
                else:
                    self.dot2HeightFront += 3
            if self.courtNetBottom < self.ballHeight < self.dot2HeightBack:
                if MatchOptions.Difficulty == "Easy":
                    self.dot2HeightBack -= 1
                elif MatchOptions.Difficulty == "Hard":
                    self.dot2HeightBack -= 5
                else:
                    self.dot2HeightBack -= 3
            elif self.dot2HeightBack < self.ballHeight < self.courtNetTop:
                if MatchOptions.Difficulty == "Easy":
                    self.dot2HeightBack += 1
                elif MatchOptions.Difficulty == "Hard":
                    self.dot2HeightBack += 5
                else:
                    self.dot2HeightBack += 3
            if self.team2TouchCount == 0:
                if Match.ballIntersectsTeam2(self):
                    self.dotDx *= .15
                    self.dotDy *= .15
            elif self.team2TouchCount == 1:
                    if Match.ballIntersectsTeam2(self):
                        Match.toss(self)
            elif self.team2TouchCount == 2:
                if Match.ballIntersectsTeam2(self):
                    Match.spike(self)   
        elif MatchOptions.PlayerCount == 6:
                if self.courtNetX <self.ballWidth < self.player2WidthTL: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.player2WidthTL -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2WidthTL -= 5
                    else:
                        self.player2WidthTL -= 3
                elif self.player2WidthBL <self.ballWidth < self.player2WidthTL: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.player2WidthTL += 1
                        self.player2WidthBL -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2WidthTL += 5
                        self.player2WidthBL -= 5
                    else:
                        self.player2WidthTL += 3
                        self.player2WidthBL -= 3
                elif self.player2WidthBL <self.ballWidth < self.topLineXL: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.player2WidthBL += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2WidthBL += 5
                    else:
                        self.player2WidthBL += 3
                if self.courtNetX <self.ballWidth < self.player2WidthTM: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.player2WidthTM -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2WidthTM -= 5
                    else:
                        self.player2WidthTM -= 3
                elif self.player2WidthBM <self.ballWidth < self.player2WidthTM: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.player2WidthTM += 1
                        self.player2WidthBM -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2WidthTM += 5
                        self.player2WidthBM -= 5
                    else:
                        self.player2WidthTM += 3
                        self.player2WidthBM -= 3
                elif self.player2WidthBM <self.ballWidth < self.topLineXL: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.player2WidthBM += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2WidthBM += 5
                    else:
                        self.player2WidthBM += 3
                if  self.courtNetX <self.ballWidth < self.player2WidthTL: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.player2WidthTL -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2WidthTL -= 5
                    else:
                        self.player2WidthTL -= 3
                elif self.player2WidthBR <self.ballWidth < self.player2WidthTR: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.player2WidthTR += 1
                        self.player2WidthBR -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2WidthTR += 5
                        self.player2WidthBR -= 5
                    else:
                        self.player2WidthTR += 3
                        self.player2WidthBR -= 3
                elif self.player2WidthBR <self.ballWidth < self.topLineXL: #If the ball is on the left side of the player on screen
                    if MatchOptions.Difficulty == "Easy":
                        self.player2WidthBR += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2WidthBR += 5
                    else:
                        self.player2WidthBR += 3
                if self.courtNetBottom < self.ballHeight < self.player2HeightTM:
                    if MatchOptions.Difficulty == "Easy":
                        self.player2HeightTM -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2HeightTM -= 5
                    else:
                        self.player2HeightTM -= 3
                elif self.player2HeightTM < self.ballHeight < self.courtNetTop:
                    if MatchOptions.Difficulty == "Easy":
                        self.player2HeightTM += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2HeightTM += 5
                    else:
                        self.player2HeightTM += 3
                if self.courtNetBottom < self.ballHeight < self.player2HeightTL:
                    if MatchOptions.Difficulty == "Easy":
                        self.player2HeightTL -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2HeightTL -= 5
                    else:
                        self.player2HeightTL -= 3
                elif self.player2HeightTL < self.ballHeight < self.courtNetTop:
                    if MatchOptions.Difficulty == "Easy":
                        self.player2HeightTL += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2HeightTL += 5
                    else:
                        self.player2HeightTL += 3
                if self.courtNetBottom < self.ballHeight < self.player2HeightTR:
                    if MatchOptions.Difficulty == "Easy":
                        self.player2HeightTR -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2HeightTR -= 5
                    else:
                        self.player2HeightTR -= 3
                elif self.player2HeightTR < self.ballHeight < self.courtNetTop:
                    if MatchOptions.Difficulty == "Easy":
                        self.player2HeightTR += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2HeightTR += 5
                    else:
                        self.player2HeightTR += 3
                if self.courtNetBottom < self.ballHeight < self.player2HeightBR:
                    if MatchOptions.Difficulty == "Easy":
                        self.player2HeightBR -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2HeightBR -= 5
                    else:
                        self.player2HeightBR -= 3
                elif self.player2HeightBR < self.ballHeight < self.courtNetTop:
                    if MatchOptions.Difficulty == "Easy":
                        self.player2HeightBR += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2HeightBR += 5
                    else:
                        self.player2HeightBR += 3
                if self.courtNetBottom < self.ballHeight < self.player2HeightBL:
                    if MatchOptions.Difficulty == "Easy":
                        self.player2HeightBL -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2HeightBL -= 5
                    else:
                        self.player2HeightBL -= 3
                elif self.player2HeightBL < self.ballHeight < self.courtNetTop:
                    if MatchOptions.Difficulty == "Easy":
                        self.player2HeightBL += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2HeightBL += 5
                    else:
                        self.player2HeightBL += 3
                if self.courtNetBottom < self.ballHeight < self.player2HeightBM:
                    if MatchOptions.Difficulty == "Easy":
                        self.player2HeightBM -= 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2HeightBM -= 5
                    else:
                        self.player2HeightBM -= 3
                elif self.player2HeightBM < self.ballHeight < self.courtNetTop:
                    if MatchOptions.Difficulty == "Easy":
                        self.player2HeightBM += 1
                    elif MatchOptions.Difficulty == "Hard":
                        self.player2HeightBM += 5
                    else:
                        self.player2HeightBM += 3
                if self.ballWidth < self.width/2:
                    Match.resetPlayer2(self)

    def distance(x0,y0,x1,y1):
        return math.sqrt(((x0-x1)**2)+((y0-y1)**2) )
#######Volleyball Moves ##########
    def topSpinServe(self, event):
        self.gageActivates = not self.gageActivates
        self.notServed = not self.notServed
        self.gagePressCount += 1
        if self.gagePressCount % 2==0 and self.gagePressCount > 0:
            Match.resetGage(self)
        #if player 1 is serving
        self.rallyStarts = True
        self.dotDx = -self.dotDx
        if self.serveOption == 1:
            self.dotDy = .85 * self.dotDy
        if self.serveOption == 2:
            self.dotDy = 2 * self.dotDy

    def floaterServe(self, event):
        self.rallyStarts = True
        self.dotDx = -self.dotDx
        self.dotDy = random.randint(-3, -1)
    def toss(self):
        if self.touchCount < 2:
            self.touchCount += 1
        #if setter top or bottom index:
                #ballHeight = middleplayerHeight
                #ballHeight = middleplayerWidth
        #elif setter is middle:
            #randomly select one of the widths for bottom or top
            #randomly select one of the heights for bottom or top
        distanceBallBack1 = Match.distance(self.dot1WidthBack, self.dot1HeightBack, self.ballWidth, self.ballHeight)
        distanceBallFront1 = Match.distance(self.dot1WidthFront, self.dot1HeightFront, self.ballWidth, self.ballHeight)
        distanceBallBack2 = Match.distance(self.dot2WidthBack, self.dot2HeightBack, self.ballWidth, self.ballHeight)
        distanceBallFront2 = Match.distance(self.dot2WidthFront, self.dot2HeightFront, self.ballWidth, self.ballHeight)
        if MatchOptions.PlayerCount == 2:
            if distanceBallFront2 < distanceBallBack2:
                self.ballWidth = self.dot2WidthBack
                self.ballHeight = self.dot2HeightBack
            elif distanceBallFront2 > distanceBallBack2:
                self.ballWidth = self.dot2WidthFront
                self.ballHeight = self.dot2HeightFront
            if distanceBallFront1 < distanceBallBack1:
                self.ballWidth = self.dot1WidthBack
                self.ballHeight = self.dot1HeightBack
            elif distanceBallFront1 > distanceBallBack1:
                self.ballWidth = self.dot1WidthFront
                self.ballHeight = self.dot1HeightFront
            self.dotDx *= .1
            self.dotDy *= .1
    def spike(self):
        if self.touchCount < 3:
            self.touchCount += 1
            
            if MatchOptions.PlayerCount == 2:
                if self.ballWidth > self.width/2:
                    distance = int(Match.distance(self.dot1WidthFront, self.dot1HeightFront,
                                            self.dot1WidthBack, self.dot1HeightBack))
                    self.gapsTeam2.append(((self.dot1WidthFront + self.dot1WidthBack)/2, self.dot1HeightFront))
                    self.gapsTeam2.append(((self.dot1WidthFront + self.dot1WidthBack)/2, (self.dot1HeightFront + self.dot1HeightBack)/2))
                    self.gapsTeam2.append(((self.dot1WidthFront - distance/2, self.dot1HeightFront)))
                    self.gapsTeam2.append(((self.dot1WidthFront + distance/2, self.dot1HeightFront)))
                    self.gapsTeam2.append(((self.dot1WidthFront, self.dot1HeightFront + distance/2)))
                    self.gapsTeam2.append(((self.dot1WidthFront, self.dot1HeightFront - distance/2)))
                    self.gapsTeam2.append(((self.dot1WidthFront, (self.dot1HeightFront + self.dot1HeightBack)/2)))
                    if (self.dot2WidthFront < self.ballWidth < self.dot2WidthFront + 40  
                    and self.dot2HeightFront-40 < self.ballHeight < self.dot2HeightFront):
                        self.ballWidth , self.ballHeight = random.choice(self.gapsTeam2)
                    elif (self.dot2WidthBack < self.ballWidth < self.dot2WidthBack + 40  
                    and self.dot2HeightBack-40 < self.ballHeight < self.dot2HeightBack):
                        self.ballWidth , self.ballHeight = random.choice(self.gapsTeam2)
                else:
                    distance = int(Match.distance(self.dot2WidthFront, self.dot2HeightFront,
                                            self.dot2WidthBack, self.dot2HeightBack))
                    self.gapsTeam1.append(((self.dot2WidthFront + self.dot2WidthBack)/2, self.dot2HeightFront))
                    self.gapsTeam1.append(((self.dot2WidthFront + self.dot2WidthBack)/2, (self.dot2HeightFront + self.dot2HeightBack)/2))
                    self.gapsTeam1.append(((self.dot2WidthFront - distance/2, self.dot2HeightBack)))
                    self.gapsTeam1.append(((self.dot2WidthFront + distance/2, self.dot2HeightBack)))
                    self.gapsTeam1.append(((self.dot2WidthFront, self.dot2HeightFront + distance/2)))
                    self.gapsTeam1.append(((self.dot2WidthFront, self.dot2HeightFront - distance/2)))
                    self.gapsTeam1.append(((self.dot2WidthFront, (self.dot2HeightFront + self.dot2HeightBack)/2)))
                    if (self.dot1WidthFront < self.ballWidth < self.dot1WidthFront + 40  
                    and self.dot1HeightFront-40 < self.ballHeight < self.dot1HeightFront):
                        self.ballWidth , self.ballHeight = random.choice(self.gapsTeam1)
                    elif (self.dot1WidthBack < self.ballWidth < self.dot1WidthBack + 40  
                    and self.dot1HeightBack-40 < self.ballHeight < self.dot1HeightBack):
                        self.ballWidth , self.ballHeight = random.choice(self.gapsTeam1)
                self.dotDx *= 1.3
                self.dotDy *= 1.3

        

#######Drawing#########
    def drawCourt(self, canvas):
        canvas.create_rectangle(0,0,self.width,self.height,fill = "#ffeeda")
        net = canvas.create_line(self.courtNetX, self.courtNetTop, self.courtNetX, self.courtNetBottom, width = 3)
        frontLineR = canvas.create_line(self.courtNetX + 200, self.courtNetTop, self.courtNetX + 200, self.courtNetBottom, width = 2)
        frontLineL = canvas.create_line(self.courtNetX - 200, self.courtNetTop, self.courtNetX - 200, self.courtNetBottom, width = 2)
        topLine = canvas.create_line(self.topLineXR, self.topLineY, self.topLineXL, self.topLineY)
        bottomLine = canvas.create_line(self.bottomLineR, self.bottomLineY, self.bottomLineL, self.bottomLineY)
        rightLine = canvas.create_line(self.topLineXR, self.topLineY, self.topLineXR, self.bottomLineY)
        leftLine = canvas.create_line(self.topLineXL, self.topLineY, self.topLineXL, self.bottomLineY)
        #canvas.create_image(self.width/2, self.height/2 + 30, image = ImageTk.PhotoImage(self.courtimage))

    def drawScoreBoard(self, canvas):
        canvas.create_rectangle(self.width/2 +300, 10, self.width/2 - 300, 100,
                            fill = "#f49030", width = 3)
        canvas.create_text(self.width/2, 55, text = f"{Match.score1} - {Match.score2}", font = "Arial 40 bold")

    def drawTeam1(self, canvas):
        if MatchOptions.PlayerCount == 1:
            canvas.create_oval(self.dot1Width, self.dot1Height, self.dot1Width + 40, self.dot1Height - 40, fill = "red")
        elif MatchOptions.PlayerCount == 2:
            canvas.create_oval(self.dot1WidthFront, self.dot1HeightFront, self.dot1WidthFront + 40, self.dot1HeightFront - 40, fill = "red")
            canvas.create_oval(self.dot1WidthBack, self.dot1HeightBack, self.dot1WidthBack + 40, self.dot1HeightBack - 40, fill = "red")
        elif MatchOptions.PlayerCount == 6:
            canvas.create_oval(self.player1WidthTM, self.player1HeightTM, self.player1WidthTM + 40, self.player1HeightTM - 40, fill = "red") #Top Middle
            canvas.create_oval(self.player1WidthBM, self.player1HeightBM, self.player1WidthBM + 40, self.player1HeightBM - 40, fill = "red") #Back Middle
            canvas.create_oval(self.player1WidthBL, self.player1HeightBL, self.player1WidthBL + 40, self.player1HeightBL - 40, fill = "red") #Back left in court
            canvas.create_oval(self.player1WidthTL, self.player1HeightTL, self.player1WidthTL + 40, self.player1HeightTL - 40, fill = "red") #Top Left
            canvas.create_oval(self.player1WidthTR, self.player1HeightTR, self.player1WidthTR + 40, self.player1HeightTR - 40, fill = "red") #Top Right
            canvas.create_oval(self.player1WidthBR, self.player1HeightBR, self.player1WidthBR + 40, self.player1HeightBR - 40, fill = "red") #Bottom Right

    def drawTeam2(self, canvas):
        if MatchOptions.PlayerCount == 1:
            canvas.create_oval(self.dot2Width, self.dot2Height, self.dot2Width + 40, self.dot2Height - 40, fill = "blue")
        elif MatchOptions.PlayerCount == 2:
            canvas.create_oval(self.dot2WidthFront, self.dot2HeightFront, self.dot2WidthFront + 40, self.dot2HeightFront - 40, fill = "blue")
            canvas.create_oval(self.dot2WidthBack, self.dot2HeightBack, self.dot2WidthBack + 40, self.dot2HeightBack - 40, fill = "blue")
        elif MatchOptions.PlayerCount == 6:
            canvas.create_oval(self.player2WidthTM, self.player2HeightTM, self.player2WidthTM + 40, self.player2HeightTM - 40, fill = "blue") #Top Middle
            canvas.create_oval(self.player2WidthBM, self.player2HeightBM, self.player2WidthBM + 40, self.player2HeightBM - 40, fill = "blue") #Back Middle
            canvas.create_oval(self.player2WidthBL, self.player2HeightBL, self.player2WidthBL + 40, self.player2HeightBL - 40, fill = "blue") #Back left in court
            canvas.create_oval(self.player2WidthTL, self.player2HeightTL, self.player2WidthTL + 40, self.player2HeightTL - 40, fill = "blue") #Top Left
            canvas.create_oval(self.player2WidthTR, self.player2HeightTR, self.player2WidthTR + 40, self.player2HeightTR + 40, fill = "blue") #Top Right
            canvas.create_oval(self.player2WidthBR, self.player2HeightBR, self.player2WidthBR + 40, self.player2HeightBR + 40, fill = "blue") #Bottom Right

    def drawVolleyBall(self, canvas):
        '''canvas.create_oval(self.ballWidth-self.ballRadius, 
            self.ballHeight-self.ballRadius, self.ballWidth+self.ballRadius, 
            self.ballHeight+self.ballRadius, fill = "pink")'''
        canvas.create_image(self.ballWidth, self.ballHeight, 
            image=ImageTk.PhotoImage(self.volleyballImage))
    
    def drawPaused(self, canvas):
        canvas.create_rectangle(self.width/2 - 120, self.height/2 - 200, 
                            self.width/2 + 120, self.height/2 + 200, fill = "#ffeeda")
        #Restart Button
        canvas.create_rectangle(self.width/2 - 90, self.height/2 - 160, 
                                self.width/2 + 90, self.height/2 - 100, fill = "#f49030")
        canvas.create_text(self.width/2, self.height/2 - 130,
                        text='Restart',
                        font='Arial 18 bold')
        #Team Select Button
        canvas.create_rectangle(self.width/2 - 90, self.height/2 - 60,
                                self.width/2 + 90, self.height/2, fill = "#f49030")
        canvas.create_text(self.width/2, self.height/2 - 30,
                        text='Match Options',
                        font='Arial 18 bold')
        #Home Button
        canvas.create_rectangle(self.width/2 - 90, self.height/2 + 40,
                                self.width/2 + 90, self.height/2 + 100, fill = "#f49030")
        canvas.create_text(self.width/2, self.height/2 + 70,
                            text = "Home",
                            font = "Arial 18 bold")                           

    def scoreCalculator(self):
        #if a ball reaches a dotDx or dotDy of 0 in a gap for a certain duration, say t=4
            #if ball.width is between the width of the edge of the left side of court and the net
                #add point to score 2
            #if ball.width is between the width of the edge of the right side of court and the net
                #add point to score 1
        pass

    def hitGageCalculator(self):
        if -.5 < self.gageSD < .5:
            self.ballSpeed *= ((100 - random.randint(0, 19.1))/100)
        elif -1 < self.gageSD < -.5 or .5 < self.gageSD < 1:
            self.ballSpeed *= ((100 - random.randint(19.1, 34))/100)
        elif -1.5 < self.gageSD < -1 or 1 < self.gageSD < 1.5:
            self.ballSpeed *= ((100 - random.randint(34, 43.2))/100)
        elif -2 < self.gageSD < -1.5 or 1.5 < self.gageSD < 2:
            self.ballSpeed *= ((100 - random.randint(43.2, 47.6))/100)
        elif -2.5 < self.gageSD < -2 or 2 < self.gageSD < 2.5:
            self.ballSpeed *= ((100 - random.randint(47.6, 49.3))/100)
        elif -3 < self.gageSD < -2.5 or 2.5 < self.gageSD < 3:
            self.ballSpeed *= ((100 - random.randint(49, 50))/100)
        pass

    def drawHitGage(self, canvas):
        #draw different rectangular regions, and have a dot travel up and down the bounds of the hit gage
        #if hit gage lands in a certain color region, pull a random speed percentage from a range of numbers
            #i.e. if in green, randomly select from 85 - 95
        #have each color region be a rectangle inside the hit gage so that you can use conditional depending on which region the dot coordinates land in

        #have this appear when player is about to spike, serve
        canvas.create_rectangle(self.gageX0_1, self.gageY0_1, self.gageX1_1, self.gageY1_1)
        canvas.create_rectangle(self.gageX0_1, self.gageY0_1, self.gageX1_1, 
                                self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/12, fill = "red", width = 1)

        canvas.create_rectangle(self.gageX0_1, self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/12, self.gageX1_1, 
                                self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/6, fill = "#DD571C", width = 1)#Dark orange

        canvas.create_rectangle(self.gageX0_1, self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/6, self.gageX1_1, 
                                self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/4, fill = "#FC6A03", width = 1) #Light orange

        canvas.create_rectangle(self.gageX0_1, self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/4, self.gageX1_1, 
                                self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/3, fill = "#EFFD5F", width = 1) #Light Yellow

        canvas.create_rectangle(self.gageX0_1, self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/3, self.gageX1_1, 
                                self.gageY0_1 + 5*(self.gageY1_1-self.gageY0_1)/12, fill = "#FEE12B", width = 1) #Dark Yellow

        canvas.create_rectangle(self.gageX0_1, self.gageY0_1 + 5*(self.gageY1_1-self.gageY0_1)/12, self.gageX1_1, 
                                self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/2, fill = "#149414", width = 1) #Green

        canvas.create_rectangle(self.gageX0_1, self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/2, self.gageX1_1, 
                                self.gageY0_1 + 7*(self.gageY1_1-self.gageY0_1)/12, fill = "#149414", width = 1) #Green

        canvas.create_rectangle(self.gageX0_1, self.gageY0_1 + 7*(self.gageY1_1-self.gageY0_1)/12, self.gageX1_1, 
                                self.gageY0_1 + 2*(self.gageY1_1-self.gageY0_1)/3, fill = "#FEE12B", width = 1) #Dark Yellow

        canvas.create_rectangle(self.gageX0_1, self.gageY0_1 + 2*(self.gageY1_1-self.gageY0_1)/3, self.gageX1_1, 
                                self.gageY0_1 + 3*(self.gageY1_1-self.gageY0_1)/4, fill = "#EFFD5F", width = 1) #Light Yellow

        canvas.create_rectangle(self.gageX0_1, self.gageY0_1 + 3*(self.gageY1_1-self.gageY0_1)/4, self.gageX1_1, 
                                self.gageY0_1 + 5*(self.gageY1_1-self.gageY0_1)/6, fill = "#FC6A03", width = 1) #Light Orange

        canvas.create_rectangle(self.gageX0_1, self.gageY0_1 + 5*(self.gageY1_1-self.gageY0_1)/6, self.gageX1_1, 
                                self.gageY0_1 + 11*(self.gageY1_1-self.gageY0_1)/12, fill = "#DD571C", width = 1) #Dark Orange

        canvas.create_rectangle(self.gageX0_1, self.gageY0_1 + 11*(self.gageY1_1-self.gageY0_1)/12, self.gageX1_1, 
                                self.gageY0_1 + (self.gageY1_1-self.gageY0_1), fill = "red", width = 1) #red

        canvas.create_oval(self.gageDotWidth + self.gageDotRadius, self.gageDotHeight + self.gageDotRadius, 
                            self.gageDotWidth - self.gageDotRadius, self.gageDotHeight - self.gageDotRadius, fill = "black")


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
        if self.paused == True:
            Match.drawPaused(self, canvas)
        if self.notServed == False:
            Match.drawHitGage(self, canvas)

class Tutorials(App):
    def appStarted(self):
        self.rules = ""
        Tutorials.rulesVolleyball(self)
    def mousePressed(self, event): 
        if event.x >= self.width/2-125 and event.x <= self.width/2+125:
            if  event.y >= self.height/2 + 175 and event.y <= self.height/2 + 225:
                HomeScreen(width = 1920, height = 1080)
    def rulesVolleyball(self):
        self.rules = "In volleyball, there are 3 moves that make up the basic playing of volleyball. \
                    \nThis includes the bump, set, and spike. \
                    \n The bump will be the receiving end of a spike or serve, and often reduces the overall velocity of the ball \
                    \n The set, or toss as others call it, will reduce the velocity even more and is performed to allow a more effective spike to take place \
                    \n The spike is the most powerful and offensive move, as it enables the team to make it extremely hard for the other team to receive due to the speed and angles \
                    \n There can only be up to 3 touches of the ball, and a point is only scored for outs and when the ball hits the floor"
    def drawRules(self, canvas):
        canvas.create_text(self.width/2, self.height/2 + 100, text = f"{self.rules}", font = "Arial 16 bold")
    def drawHomeButton(self, canvas):
        homeButton = canvas.create_rectangle(self.width/2-125, self.height/2 + 175, self.width/2 + 125, self.height/2 + 225,
                            fill = "#f49030", width = 2)
        canvas.create_text(self.width/2, self.height/2 + 200, text = "Home", font = "Arial 20 bold")
    def redrawAll(self, canvas):
        canvas.create_rectangle(0,0,self.width,self.height, fill = "#ffeeda")
        Tutorials.drawRules(self, canvas)
        Tutorials.drawHomeButton(self, canvas)

class Controls(App):
    def appStarted(self):
        self.controls = ""
        Tutorials.rulesVolleyball(self)
    def mousePressed(self, event): 
        if event.x >= self.width/2-125 and event.x <= self.width/2+125:
            if  event.y >= self.height/2 + 175 and event.y <= self.height/2 + 225:
                HomeScreen(width = 1920, height = 1080)
    def drawControls(self, canvas):
        canvas.create_text(self.width/2, self.height/2 + 100, text = f"{self.controls}", font = "Arial 16 bold")
    def drawHomeButton(self, canvas):
        homeButton = canvas.create_rectangle(self.width/2-125, self.height/2 + 175, self.width/2 + 125, self.height/2 + 225,
                            fill = "#f49030", width = 2)
        canvas.create_text(self.width/2, self.height/2 + 200, text = "Home", font = "Arial 20 bold")
    def redrawAll(self, canvas):
        canvas.create_rectangle(0,0,self.width,self.height, fill = "#ffeeda")
        Controls.drawControls(self, canvas)
        Controls.drawHomeButton(self, canvas)
class MatchIsOver(App):
    def appStarted(self):
        self.message = "Game Over"
        self.message2 = "Player 1 is the WINNER"
        self.message3 = "Player 2 is the WINNER"
        self.background = self.loadImage("SunnyBackground.jpg") #Background of a sunny volleyball court
        self.Team1 = MatchOptions.Team1
        self.Team2 = MatchOptions.Team2
        
    def redrawAll(self, canvas):
        canvas.create_image(self.width/2, self.height/2, image=ImageTk.PhotoImage(self.background))
        if Match.score1 > Match.score2:
            canvas.create_text(self.width/2, self.height/2, 
                text = self.message + f"\nTeam {self.Team1} wins." + self.message2, font = "Arial 30 bold", fill = "#B53737")
        elif Match.score2 > Match.score1:
            canvas.create_text(self.width/2, self.height/2, 
                text = self.message + f"\nTeam {self.Team2} wins." + self.message3, font = "Arial 30 bold", fill = "#1338BE")
        else:
            canvas.create_text(self.width/2, self.height/2, 
                text = self.message + "\nNeither Team Wins", font = "Arial 30 bold", fill = "black")

HomeScreen(width=1920, height=1080)

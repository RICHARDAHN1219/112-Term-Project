from cmu_112_graphics import *
from PIL import *
import string, math, random
#from pygame import mixer
from tkinter import *


class HomeScreen(App):
    def appStarted(self):
        self.image1 = self.loadImage('background1.jpg')
        self.image2 = self.scaleImage(self.image1, 5)

    def keyPressed(self, event):
        self.counter += 1

    def mousePressed(self, event): 
        if event.x >= self.width/2-125 and event.x <= self.width/2+125:
            if event.y >= self.height/2 - 25 and event.y <= self.height/2 + 25:
                MatchOptions(width=1920, height=1080)


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
        self.image1 = self.loadImage('haikyuubackground2.jpg')
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
        self.Team1List = ",".join(Sides.playersInTeam1)
        self.Team2List = ",".join(Sides.playersInTeam2)
        self.image1 = self.loadImage('brazilVolley.jpg')

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
    
    def resetApp(self):
        # This is a helper function for Controllers
        # This initializes most of our model (stored in app.xyz)
        # This is called when they start the app, and also after
        # the game is over when we restart the app.
        self.notServed = True
        self.gageValue = 0
        self.gageSD = 0
        self.topCount = 0
        self.bottomCount = 0
        self.rowCount = 0
        self.row2Count = 0
        self.top2Count = 0
        self.bottom2Count = 0
        self.dotOutline = "green"
        self.timerDelay = 200 # milliseconds
        self.waitingForKeyPress = True
        self.gameOver = False
        self.paused = False
        Match.resetTeams(self)
        Match.resetCourt(self)
        Match.resetPlayers(self)
        Match.resetBall(self)
        if MatchOptions.Difficulty == "Easy":
            self.ballSpeed = 10
        elif MatchOptions.Difficulty == "Intermediate":
            self.ballSpeed = 15
        else:
            self.ballSpeed = 30

    
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
        self.dotDx = -10
        self.dotDy = -3
    
    def resetPlayers(self):
        #### 1 Player #####
        self.dot1Width = self.width/2-90
        self.dot1Height = self.height/2 + 50
        self.dot2Width = self.width/2+90
        self.dot2Height = self.height/2 + 50

        #### 2 Players ####
        self.dot1WidthFront = self.width/2-90
        self.dot1HeightFront = self.height/2 + 50
        self.dot1WidthBack = self.width/2-340
        self.dot1HeightBack = self.height/2 + 50
        self.dot2WidthFront = self.width/2+90
        self.dot2HeightFront = self.height/2 + 50
        self.dot2WidthBack = self.width/2+340
        self.dot2HeightBack = self.height/2 + 50

        #### 6 Players ####
        self.player1WidthTM = self.width/2-90
        self.player1HeightTM = self.height/2 + 50
        self.player1WidthTL = self.width/2-90
        self.player1HeightTL = self.height/2 - 70
        self.player1WidthTR = self.width/2 - 90
        self.player1HeightTR = self.height/2 + 170
        self.player1WidthBM = self.width/2-340
        self.player1HeightBM = self.height/2 + 50
        self.player1WidthBL = self.width/2-340
        self.player1HeightBL = self.height/2 - 70
        self.player1WidthBR = self.width/2-340
        self.player1HeightBR = self.height/2 + 170

        self.player2WidthTM = self.width/2+90
        self.player2HeightTM = self.height/2 + 50
        self.player2WidthTL = self.width/2+90
        self.player2HeightTL = self.height/2 - 70
        self.player2WidthTR = self.width/2+90
        self.player2HeightTR = self.height/2 + 170
        self.player2WidthBM = self.width/2+340
        self.player2HeightBM = self.height/2 + 50
        self.player2WidthBL = self.width/2+340
        self.player2HeightBL = self.height/2 - 70
        self.player2WidthBR = self.width/2+340
        self.player2HeightBR = self.height/2 + 170


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
        if (not self.paused and not self.notServed):
            Match.doStep(self)

    def doStep(self):
        if not self.waitingForKeyPress and not self.gameOver:
            Match.moveBall(self)

    def keyPressed(self, event):
        if self.gameReset:
            Match.resetApp(self)
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
                self.dot1Width -= 15
            #### 2 players ####
            elif MatchOptions.PlayerCount == 2:
                if self.topCount % 2 == 1:
                    self.dot1WidthFront -= 15
                else:
                    self.dot1WidthBack -= 15
            #### 6 players ####
            else:
                if self.rowCount %2 == 1:
                    if self.topCount % 3 == 0:
                        self.player1WidthTL -= 15
                    elif self.topCount % 3 == 1:
                        self.player1WidthTM -= 15
                    elif self.topCount % 3 == 2:
                        self.player1WidthTR -= 15
                else:
                    if self.bottomCount % 3 == 0:
                        self.player1WidthBL -= 15
                    elif self.bottomCount % 3 == 1:
                        self.player1WidthBM -= 15
                    elif self.bottomCount % 3 == 2:
                        self.player1WidthBR -= 15
        elif event.key == 'd':
            #current player moves right
            #### 1 player ####1
            if MatchOptions.PlayerCount == 1:            
                self.dot1Width += 15
            #### 2 players ####
            elif MatchOptions.PlayerCount == 2:
                if self.topCount % 2 == 1:
                    self.dot1WidthFront += 15
                else:
                    self.dot1WidthBack += 15
            #### 6 players ####
            else:
                if self.rowCount % 2 == 1:
                    if self.topCount % 3 == 0:
                        self.player1WidthTL += 15
                    elif self.topCount % 3 == 1:
                        self.player1WidthTM += 15
                    elif self.topCount % 3 == 2:
                        self.player1WidthTR += 15
                else:
                    if self.bottomCount % 3 == 0:
                        self.player1WidthBL += 15
                    elif self.bottomCount % 3 == 1:
                        self.player1WidthBM += 15
                    elif self.bottomCount % 3 == 2:
                        self.player1WidthBR += 15
            
        elif event.key == "s":
            #### 1 player ####1
            if MatchOptions.PlayerCount == 1:            
                self.dot1Height += 15
            #### 2 players ####
            elif MatchOptions.PlayerCount == 2:
                if self.topCount % 2 == 1:
                    self.dot1HeightFront += 15
                else:
                    self.dot1HeightBack += 15
            #### 6 players ####
            else:
                if self.rowCount % 2 == 1:
                    if self.topCount % 3 == 0:
                        self.player1HeightTL += 15
                    elif self.topCount % 3 == 1:
                        self.player1HeightTM += 15
                    elif self.topCount % 3 == 2:
                        self.player1HeightTR += 15
                else:
                    if self.bottomCount % 3 == 0:
                        self.player1HeightBL += 15
                    elif self.bottomCount % 3 == 1:
                        self.player1HeightBM += 15
                    elif self.bottomCount % 3 == 2:
                        self.player1HeightBR += 15
        elif event.key == "w":
            #### 1 player ####1
            if MatchOptions.PlayerCount == 1:            
                self.dot1Height -= 15
            #### 2 players ####
            elif MatchOptions.PlayerCount == 2:
                if self.topCount % 2 == 1:
                    self.dot1HeightFront -= 15
                else:
                    self.dot1HeightBack -= 15
            #### 6 players ####
            else:
                if self.rowCount % 2 == 1:
                    if self.topCount % 3 == 0:
                        self.player1HeightTL -= 15
                    elif self.topCount % 3 == 1:
                        self.player1HeightTM -= 15
                    elif self.topCount % 3 == 2:
                        self.player1HeightTR -= 15
                else:
                    if self.bottomCount % 3 == 0:
                        self.player1HeightBL -= 15
                    elif self.bottomCount % 3 == 1:
                        self.player1HeightBM -= 15
                    elif self.bottomCount % 3 == 2:
                        self.player1HeightBR -= 15

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
            if (self.dot1Width <= self.ballWidth <= self.dot1Width + 40 
            or self.dot1Height-40 <= self.ballHeight <= self.dot1Height):
                self.dotDx = -self.dotDx
                self.ballWidth = self.dot1Width + 40 + self.ballRadius
                dToMiddleY = self.ballHeight - (self.dot1Height-40 + self.dot1Height)/2
                dampeningFactor = 3 # smaller = more extreme bounces
                self.dotDy = dToMiddleY / dampeningFactor
        elif Match.ballIntersectsTeam2(self):
            if (self.dot2Width <= self.ballWidth <= self.dot2Width + 40 
            or self.dot2Height >= self.ballHeight >= self.dot2Height - 40):
                self.dotDx = -self.dotDx
                self.ballWidth = self.dot2Width - self.ballRadius
                dToMiddleY = self.ballHeight - (self.dot2Height-40 + self.dot2Height)/2
                dampeningFactor = 3 # smaller = more extreme bounces
                self.dotDy = dToMiddleY / dampeningFactor

    def ballIntersectsTeam1(self):
        return (self.dot1Width < self.ballWidth < self.dot1Width + 40 
        or self.dot1Height - 40 < self.ballHeight < self.dot1Height)
    
    def ballIntersectsTeam2(self):
        return (self.dot2Width < self.ballWidth < self.dot2Width + 40  
        or self.dot2Height-40 < self.ballHeight < self.dot2Height)

    def drawCourt(self, canvas):
        canvas.create_rectangle(0,0,self.width,self.height,fill = "#ffeeda")
        canvas.create_image(self.width/2, self.height/2 + 30, image = ImageTk.PhotoImage(self.courtimage))

    def drawScoreBoard(self, canvas):
        canvas.create_rectangle(self.width/2 +300, 10, self.width/2 - 300, 100,
                            fill = "#f49030", width = 3)
        canvas.create_text(self.width/2, 55, text = f"{self.score1} - {self.score2}", font = "Arial 40 bold")

    def drawTeam1(self, canvas):
        if MatchOptions.PlayerCount == 1:
            canvas.create_oval(self.dot1Width, self.dot1Height, self.dot1Width + 40, self.dot1Height - 40, fill = "red")
        elif MatchOptions.PlayerCount == 2:
            canvas.create_oval(self.dot1WidthFront, self.dot1HeightFront, self.dot1WidthFront + 40, self.dot1HeightFront - 40, fill = "red")
            canvas.create_oval(self.dot1WidthBack, self.dot1HeightBack, self.dot1WidthBack - 40, self.dot1HeightBack - 40, fill = "red")
        elif MatchOptions.PlayerCount == 6:
            canvas.create_oval(self.player1WidthTM, self.player1HeightTM, self.player1WidthTM + 40, self.player1HeightTM - 40, fill = "red") #Top Middle
            canvas.create_oval(self.player1WidthBM, self.player1HeightBM, self.player1WidthBM - 40, self.player1HeightBM - 40, fill = "red") #Back Middle
            canvas.create_oval(self.player1WidthBL, self.player1HeightBL, self.player1WidthBL - 40, self.player1HeightBL - 40, fill = "red") #Back left in court
            canvas.create_oval(self.player1WidthTL, self.player1HeightTL, self.player1WidthTL + 40, self.player1HeightTL - 40, fill = "red") #Top Left
            canvas.create_oval(self.player1WidthTR, self.player1HeightTR, self.player1WidthTR + 40, self.player1HeightTR + 40, fill = "red") #Top Right
            canvas.create_oval(self.player1WidthBR, self.player1HeightBR, self.player1WidthBR - 40, self.player1HeightBR + 40, fill = "red") #Bottom Right

    def drawTeam2(self, canvas):
        if MatchOptions.PlayerCount == 1:
            canvas.create_oval(self.dot2Width, self.dot2Height, self.dot2Width + 40, self.dot2Height - 40, fill = "blue")
        elif MatchOptions.PlayerCount == 2:
            canvas.create_oval(self.dot2WidthFront, self.dot2HeightFront, self.dot2WidthFront + 40, self.dot2HeightFront - 40, fill = "blue")
            canvas.create_oval(self.dot2WidthBack, self.dot2HeightBack, self.dot2WidthBack - 40, self.dot2HeightBack - 40, fill = "blue")
        elif MatchOptions.PlayerCount == 6:
            canvas.create_oval(self.player2WidthTM, self.player2HeightTM, self.player2WidthTM + 40, self.player2HeightTM - 40, fill = "blue") #Top Middle
            canvas.create_oval(self.player2WidthBM, self.player2HeightBM, self.player2WidthBM - 40, self.player2HeightBM - 40, fill = "blue") #Back Middle
            canvas.create_oval(self.player2WidthBL, self.player2HeightBL, self.player2WidthBL - 40, self.player2HeightBL - 40, fill = "blue") #Back left in court
            canvas.create_oval(self.player2WidthTL, self.player2HeightTL, self.player2WidthTL + 40, self.player2HeightTL - 40, fill = "blue") #Top Left
            canvas.create_oval(self.player2WidthTR, self.player2HeightTR, self.player2WidthTR + 40, self.player2HeightTR + 40, fill = "blue") #Top Right
            canvas.create_oval(self.player2WidthBR, self.player2HeightBR, self.player2WidthBR - 40, self.player2HeightBR + 40, fill = "blue") #Bottom Right

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
            self.ballSpeed *= ((100 - random.randint(19.1, 34))/100)
        pass

    def drawHitGage(self):
        #draw different rectangular regions, and have a dot travel up and down the bounds of the hit gage
        #if hit gage lands in a certain color region, pull a random speed percentage from a range of numbers
            #i.e. if in green, randomly select from 85 - 95
        #have each color region be a rectangle inside the hit gage so that you can use conditional depending on which region the dot coordinates land in

        #have this appear when player is about to spike, serve
        pass





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

class MatchIsOver(App):
    def appStarted(self):
        self.message = "Game Over"
        self.message2 = "Player 1 is the WINNER"
        self.message3 = "Player 2 is the WINNER"
        self.background = self.loadImage("SunnyBackground.jpg")
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

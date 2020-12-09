import math
import random
import string
#from pygame import mixer
from tkinter import *

import pygame
from PIL import *

from cmu_112_graphics import *


class HomeScreen(App):
    def appStarted(self):
        self.image1 = self.loadImage('background1.jpg')
        #Background image for the screen, a person's hand on the volleyball
        #Taken from a wallpaper website
        #t.ly/QjRE is the link
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
        #Taken from Pinterest
        #Link: t.ly/L3jS
        #Have button change color later

    Teamlist = [
            "America",
            "Karasuno",
            "Brazil",
            "Russia",
            "Japan"
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
        #The player1 icon taken from a png image site
        #t.ly/AqHF
        self.imageNum2 = self.loadImage("number2.png") 
        #The player 2 icon take from a png image site
        #t.ly/Gr5S
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
        #The background screen of a Brazilian volleyball player
        #Taken from a wallpaper website
        #t.ly/nQ4U

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
        Match.resetApp(self)
        
        
    
    def resetApp(self):
        # This is a helper function for Controllers
        # This initializes most of our model (stored in app.xyz)
        # This is called when they start the app, and also after
        # the game is over when we restart the app.
        self.rallyReset = False
        self.notServed = True
        self.gameReset = False
        self.rallyStarts = False
        self.gageActivates = False
        self.jumpIsPressed = False
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
        self.servingSide = 0
        self.touchCount = 0
        self.team1TouchCount = 0
        self.team2TouchCount = 0
        self.serveGoesOverNet = False
        self.gapsTeam1 = []
        self.gapsTeam2 = []
        self.fillTeam1 = "red"
        self.fillTeam2 = "blue"
        self.topSpinServe = False
        self.topSpinServeLeft = False
        self.topSpinServeRight = False
        self.floaterServe = False
        self.tossC = False
        self.toss = False
        self.tossBack = False
        self.toss2Tempo = False
        self.toss1Tempo = False
        self.toss0Tempo = False
        Match.resetTeams(self)
        Match.resetCourt(self)
        Match.resetPlayer1(self)
        Match.resetPlayer2(self)
        Match.resetBall(self)
        Match.resetGage(self)

    
    def resetTeams(self):
        self.imageNum1 = self.loadImage("number1.png") 
        #Same player1 icon
        self.imageNum2 = self.loadImage("number2.png")
        #Same player 2 Icon
        self.PlayerIcon1 = self.scaleImage(self.imageNum1, 2/3)
        self.PlayerIcon2 = self.scaleImage(self.imageNum2, 2/3)
        self.Team1 = MatchOptions.Team1
        self.Team2 = MatchOptions.Team2

    def resetCourt(self):
        self.imageCourt = self.loadImage("court2dtransparent.png") #picture of the court
        #Took original image from t.ly/eQY0, made it transparent myself
        self.courtimage = self.scaleImage(self.imageCourt, 2.2)
        self.ballimage = self.loadImage("volleyballimage.png") #picture of volleyball
        #Found image of mikasa v200w volleyball and made it transparent
        #t.ly/BfeN
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
        self.ballInBounds = True

    def resetBall(self):
        # This is a helper function for Controllers
        # Get the dot ready for the next round.  Move the dot to
        # the center of the screen and give it an initial velocity.
        if self.servingSide == 0:
            self.ballWidth = self.bottomLineL-30
            self.ballHeight = self.bottomLineY - 50
        else:
            self.ballWidth = self.bottomLineR + 30
            self.ballHeight = self.bottomLineY - 50
        self.ballRadius = 15
        self.dotDx = -10
        self.dotDy = -3
        self.originalDx = -10
        self.originalDy = -3
        self.dotGageDx = -30 #Switch speed of this for different difficulties
        self.dotGageDy = -30
        if MatchOptions.Difficulty == "Easy":
            self.ballSpeed = 25
            self.ballAngle = 50
        elif MatchOptions.Difficulty == "Hard":
            self.ballSpeed = 35
            self.ballAngle = 30
        else:
            self.ballSpeed = 30
            self.ballAngle = 40
        Match.resetBallCalculation(self)
        
    def resetBallCalculation(self):
        self.ballVx = self.ballSpeed*math.cos(math.radians(self.ballAngle))
        self.ballVy = self.ballSpeed*math.sin(math.radians(self.ballAngle))
        self.ballAx   = 0
        self.ballAy   = -9.8 #Gravity
        self.ballTime = 0
        self.ballDt = .05
        self.ballX = self.ballWidth
        self.ballY = self.ballHeight
        if self.servingSide == 1:
            self.ballVx = -self.ballVx

    def resetPlayer1(self):
        #### 1 Player #####
        if self.servingSide == 1:
            self.dot1Width = self.width/2-90
            self.dot1Height = self.height/2 + 50
        elif self.servingSide == 0:
            self.dot1Width = self.bottomLineL-90
            self.dot1Height = self.bottomLineY - 50

        #### 2 Players ####
        if self.servingSide == 1:
            self.dot1WidthFront = self.width/2-90
            self.dot1HeightFront = self.height/2 + 50
            self.dot1WidthBack = self.width/2-380
            self.dot1HeightBack = self.height/2 + 50

        elif self.servingSide == 0:
            self.dot1WidthFront = self.width/2-90
            self.dot1HeightFront = self.height/2 + 50
            self.dot1WidthBack = self.bottomLineL-90
            self.dot1HeightBack =  self.bottomLineY - 50

        self.fillTeam1Front = self.fillTeam1
        self.fillTeam1Back = self.fillTeam1
        if MatchOptions.PlayerCount == 2:
            if Sides.playersInTeam1 != []: 
                if self.topCount % 2 == 1:
                    self.fillTeam1Front = "pink"
                    self.fillTeam1Back = "red"
                elif self.topCount % 2 == 0:
                    self.fillTeam1Back = "pink"
                    self.fillTeam1Front = "Red"

        
        #### 6 Players ####
        self.fillTeam1TM = "red"
        self.fillTeam1TL = "red"
        self.fillTeam1TR = "red"
        self.fillTeam1BM = "red"
        self.fillTeam1BL = "red"
        self.fillTeam1BR = "red"
        self.fillTeam2TM = "blue"
        self.fillTeam2TL = "blue"
        self.fillTeam2TR = "blue"
        self.fillTeam2BM = "blue"
        self.fillTeam2BL = "blue"
        self.fillTeam2BR = "blue"

        if self.servingSide == 1:
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


        elif self.servingSide == 0:
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
           
    def resetPlayer1TouchCount(self):
        self.team1TouchCount = 0
    
    def resetPlayer2(self):
        #### 1 Player #####
        if self.servingSide == 1:
            self.dot2Width = self.topLineXR + 90
            self.dot2Height = self.bottomLineY - 50
        else:
            self.dot2Width = self.width/2+90
            self.dot2Height = self.height/2 + 50

        #### 2 Players ####
        if self.servingSide == 1:
            self.dot2WidthFront = self.width/2+90
            self.dot2HeightFront = self.height/2 + 50
            self.dot2WidthBack = self.topLineXR + 90
            self.dot2HeightBack = self.bottomLineY - 50
        else:
            self.dot2WidthFront = self.width/2+90
            self.dot2HeightFront = self.height/2 + 50
            self.dot2WidthBack = self.width/2+300
            self.dot2HeightBack = self.height/2 + 50


        self.fillTeam2Front = self.fillTeam2
        self.fillTeam2Back = self.fillTeam2
        if MatchOptions.PlayerCount == 2:
            if Sides.playersInTeam2 != []:
                if self.top2Count % 2 == 1:
                    self.fillTeam2Front = "purple"
                    self.fillTeam2Back = "blue"
                else:
                    self.fillTeam2Back = "purple"
                    self.fillTeam2Front = "blue"


        #### 6 Players ####
        if self.servingSide == 1:
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

    def resetPlayer2TouchCount(self):
        self.team2TouchCount = 0

    def resetGage(self):
        if self.servingSide == 0:
            self.gageX0_1 = self.dot1Width - 80
            self.gageX1_1 = self.gageX0_1 + 30
            self.gageY0_1 = self.dot1Height - 180
            self.gageY1_1 = self.dot1Height + 180
            self.gageDotWidth = self.gageX0_1 + (self.gageX1_1 - self.gageX0_1)/2
            self.gageDotHeight = self.dot1Height
        if self.servingSide == 1:
            self.gageX0_1 = self.dot2Width + 80
            self.gageX1_1 = self.gageX0_1 - 30
            self.gageY0_1 = self.dot2Height - 180
            self.gageY1_1 = self.dot2Height + 180
            self.gageDotWidth = self.gageX0_1 + (self.gageX1_1 - self.gageX0_1)/2
            self.gageDotHeight = self.dot2Height
        self.gageDotRadius = 15
        self.gagePressCount = 0
    
    def resetRally(self):
        Match.resetPlayer1(self)
        Match.resetPlayer2(self)
        Match.resetBall(self)
        Match.resetGage(self)
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
            Match.moveBall1(self)
            Match.doMoveP2AI(self)
            Match.doMoveP1AI(self)
            if self.ballTime < 4:
                Match.step(self)
    def doGage(self):
        if self.gageActivates == True:
            Match.moveGageDot(self)
    def doMoveP2AI(self):
        if Sides.playersInTeam2 == []:
            Match.movePlayer2AI(self)

    def doMoveP1AI(self):
        Match.movePlayer1AI(self)
    
    def keyPressed(self, event):
        if Match.score1 == 25 and Match.score2 < 24:
            self.gameOver = True
        elif Match.score2 == 25 and Match.score1 < 24:
            self.gameOver = True
        elif Match.score1>25 and Match.score2 > 25:
            if Match.score1 > Match.score2 + 1 or Match.score2 > Match.score1 + 1:
                self.gameOver = True
        if self.gameReset:
            Match.resetApp(self)
        elif self.gameOver:
            MatchIsOver(width = 1920, height = 1028)
        elif self.waitingForKeyPress:
            self.waitingForKeyPress = False
        elif self.rallyReset:
            Match.resetRally(self)
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
            if self.servingSide == 1:
                self.ballVx = -self.ballVx
            Match.topSpinServe(self,event)
        elif event.key == "2":
            self.serveOption = 2
            if self.servingSide == 1:
                self.ballVx = -self.ballVx
            Match.topSpinServe(self,event)
        elif event.key == "3":
            if self.servingSide == 1:
                self.ballVx = -self.ballVx
            Match.floaterServe(self,event)
        elif event.key == "4":
            Match.toss(self)
        elif event.key == "5":
            Match.spike(self)
        elif event.key == "i":
            self.jumpIsPressed = True
        if self.jumpIsPressed == True:
            if event.key == "1":
                Match.toss(self)
            elif event.key == "2":
                Match.spike(self)
        if MatchOptions.PlayerCount == 2:
            if Sides.playersInTeam1 != []: 
                if self.topCount % 2 == 1:
                    self.fillTeam1Front = "purple"
                    self.fillTeam1Back = "red"
                elif self.topCount % 2 == 0:
                    self.fillTeam1Back = "purple"
                    self.fillTeam1Front = "Red"
            if Sides.playersInTeam1 != []:
                if self.top2Count % 2 == 1:
                    self.fillTeam2Front = "purple"
                    self.fillTeam2Back = "blue"
                else:
                    self.fillTeam2Back = "purple"
                    self.fillTeam2Front = "blue"
            if Sides.playersInTeam2 != []:
                if self.top2Count % 2 == 1:
                    self.fillTeam2Front = "purple"
                    self.fillTeam2Back = "blue"
                else:
                    self.fillTeam2Back = "purple"
                    self.fillTeam2Front = "blue"
        elif MatchOptions.PlayerCount == 6:
            if Sides.playersInTeam1 != []: 
                if self.rowCount % 2 == 1:
                    if self.topCount % 3 == 0:
                        self.fillTeam1TM = "red"
                        self.fillTeam1TL = "purple"
                        self.fillTeam1TR = "red"
                        self.fillTeam1BM = "red"
                        self.fillTeam1BL = "red"
                        self.fillTeam1BR = "red"
                    elif self.topCount % 3 == 1:
                        self.fillTeam1TM = "purple"
                        self.fillTeam1TL = "red"
                        self.fillTeam1TR = "red"
                        self.fillTeam1BM = "red"
                        self.fillTeam1BL = "red"
                        self.fillTeam1BR = "red"
                    elif self.topCount % 3 == 2:
                        self.fillTeam1TM = "red"
                        self.fillTeam1TL = "red"
                        self.fillTeam1TR = "purple"
                        self.fillTeam1BM = "red"
                        self.fillTeam1BL = "red"
                        self.fillTeam1BR = "red"
                else:
                    if self.bottomCount % 3 == 0:
                        self.fillTeam1TM = "red"
                        self.fillTeam1TL = "red"
                        self.fillTeam1TR = "red"
                        self.fillTeam1BM = "red"
                        self.fillTeam1BL = "purple"
                        self.fillTeam1BR = "red"
                    elif self.bottomCount % 3 == 1:
                        self.fillTeam1TM = "red"
                        self.fillTeam1TL = "red"
                        self.fillTeam1TR = "red"
                        self.fillTeam1BM = "purple"
                        self.fillTeam1BL = "red"
                        self.fillTeam1BR = "red"
                    elif self.bottomCount % 3 == 2:
                        self.fillTeam1TM = "red"
                        self.fillTeam1TL = "red"
                        self.fillTeam1TR = "red"
                        self.fillTeam1BM = "red"
                        self.fillTeam1BL = "red"
                        self.fillTeam1BR = "purple"
            if Sides.playersInTeam2 != []: 
                if self.row2Count % 2 == 1:
                    if self.top2Count % 3 == 0:
                        self.fillTeam2TM = "blue"
                        self.fillTeam2TL = "purple"
                        self.fillTeam2TR = "blue"
                        self.fillTeam2BM = "blue"
                        self.fillTeam2BL = "blue"
                        self.fillTeam2BR = "blue"
                    elif self.top2Count % 3 == 1:
                        self.fillTeam2TM = "purple"
                        self.fillTeam2TL = "blue"
                        self.fillTeam2TR = "blue"
                        self.fillTeam2BM = "blue"
                        self.fillTeam2BL = "blue"
                        self.fillTeam2BR = "blue"
                    elif self.top2Count % 3 == 2:
                        self.fillTeam2TM = "blue"
                        self.fillTeam2TL = "blue"
                        self.fillTeam2TR = "purple"
                        self.fillTeam2BM = "blue"
                        self.fillTeam2BL = "blue"
                        self.fillTeam2BR = "blue"
                else:
                    if self.bottom2Count % 3 == 0:
                        self.fillTeam2TM = "blue"
                        self.fillTeam2TL = "blue"
                        self.fillTeam2TR = "blue"
                        self.fillTeam2BM = "blue"
                        self.fillTeam2BL = "purple"
                        self.fillTeam2BR = "blue"
                    elif self.bottom2Count % 3 == 1:
                        self.fillTeam2TM = "blue"
                        self.fillTeam2TL = "blue"
                        self.fillTeam2TR = "blue"
                        self.fillTeam2BM = "purple"
                        self.fillTeam2BL = "blue"
                        self.fillTeam2BR = "blue"
                    elif self.bottom2Count % 3 == 2:
                        self.fillTeam2TM = "blue"
                        self.fillTeam2TL = "blue"
                        self.fillTeam2TR = "blue"
                        self.fillTeam2BM = "blue"
                        self.fillTeam2BL = "blue"
                        self.fillTeam2BR = "purple"
        #if (self.ballY < self.ballHeight):
        
        #insert score calculation here if not working in separate function 
        
    '''def mousePressed(self, event):
        #Continue button is pressed
        pass
    def moveIconToRight(self):
        pass'''


    def scoreCalculator(self):
        pass
            
        

    def moveBall(self):
        #Edge calculation similar to pong    
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
        
    def moveBall1(self):
        #Edge calculation similar to pong    
        #self.ballWidth += self.dotDx
        #self.ballHeight += self.dotDy
        '''if (self.ballHeight + self.ballRadius >= self.height): #self.height
                # The dot went off the bottom!
                self.ballHeight = self.height - self.ballRadius
                self.ballVy = -self.ballVy
        if (self.ballHeight - self.ballRadius <= 0): #0
                # The dot went off the top!
                self.ballHeight = self.ballRadius
                self.ballVy = -self.ballVy
        if (self.ballWidth + self.ballRadius >= self.width): #self.width
                # The dot went off the right!
                self.ballWidth = self.width - self.ballRadius
                self.ballVx = -self.ballVx
        elif (self.ballWidth - self.ballRadius <= 0): #0
            # The dot went off the top!
            self.ballWidth = self.ballRadius
            self.ballVx = -self.ballVx'''
        if (self.ballTime < 4): 
        #if self.ballY >= self.ballHeight:       
            self.ballWidth += Match.VxCalculator(self, self.ballDt)
            self.ballHeight -= Match.VyCalculator(self, self.ballDt)
            if self.ballWidth > self.width/2:
                self.team1TouchCount = 0
            elif self.ballWidth < self.width/2:
                self.team2TouchCount = 0
            if Match.ballIntersectsTeam1(self):
                Match.resetBallCalculation(self)
                self.ballTime = 0
                if MatchOptions.PlayerCount == 1:
                    self.ballVx = self.ballVx

                elif MatchOptions.PlayerCount == 2:
                    if (self.dot1WidthFront < self.ballWidth < self.dot1WidthFront + 40  
                            and self.dot1HeightFront-40 < self.ballHeight < self.dot1HeightFront):
                        self.team1TouchCount += 1
                        self.touchCount += 1
                        if self.team1TouchCount == 1:
                            Match.receive(self)
                        if self.team1TouchCount == 2:
                            Match.toss(self)
                        elif self.team1TouchCount == 3:
                            Match.spike(self)
                    elif (self.dot1WidthBack < self.ballWidth < self.dot1WidthBack + 40  
                            and self.dot1HeightBack-40 < self.ballHeight < self.dot1HeightBack):
                        self.team1TouchCount += 1
                        self.touchCount += 1
                        if self.team1TouchCount == 1:
                            Match.receive(self)
                        if self.team1TouchCount == 2:
                            Match.toss(self)
                        elif self.team1TouchCount == 3:
                            Match.spike(self)
                        '''self.dotDx = -self.originalDx * .15
                        self.ballWidth = self.dot1WidthBack + 40 + self.ballRadius
                        dToMiddleY = self.ballHeight - (self.dot1HeightBack-40 + self.dot1HeightBack)/2
                        dampeningFactor = 3 # smaller = more extreme bounces
                        self.dotDy = dToMiddleY / dampeningFactor
                        self.touchCount += 1
                        self.team1TouchCount += 1'''

                elif MatchOptions.PlayerCount == 6:
                    if ((self.player1WidthTL < self.ballWidth < self.player1WidthTL + 40  
                        and self.player1HeightTL-40 < self.ballHeight < self.player1HeightTL) or 
                        (self.player1WidthTM < self.ballWidth < self.player1WidthTM + 40  
                        and self.player1HeightTM-40 < self.ballHeight < self.player1HeightBM) or 
                        (self.player1WidthTR < self.ballWidth < self.player1WidthTR + 40  
                        and self.player1HeightTR-40 < self.ballHeight < self.player1HeightTR)):
                        self.ballVx = self.ballVx
                        self.touchCount += 1
                        self.team1TouchCount += 1

                        if (self.player1WidthTL < self.ballWidth < self.player1WidthTL + 40  
                        and self.player1HeightTL-40 < self.ballHeight < self.player1HeightTL):
                            self.ballWidth = self.player1WidthTL - self.ballRadius
                            if self.team1TouchCount == 1:
                                Match.receive(self)
                            elif self.team1TouchCount == 2:
                                random.choice(Match.toss(self), Match.ctoss(self))
                            elif self.team1TouchCount == 3:
                                Match.spike(self)

                        elif (self.player1WidthTM < self.ballWidth < self.player1WidthTM + 40  
                        and self.player1HeightTM-40 < self.ballHeight < self.player1HeightTM):
                            self.ballWidth = self.player1WidthTM - self.ballRadius
                            if self.team1TouchCount == 1:
                                Match.receive(self)
                            elif self.team1TouchCount == 2:
                                Match.toss(self) 
                            elif self.team1TouchCount == 3:
                                Match.spike(self)

                        elif (self.player1WidthTR < self.ballWidth < self.player1WidthTR + 40  
                        and self.player1HeightTR-40 < self.ballHeight < self.player1HeightTR):
                            self.ballWidth = self.player1WidthTR - self.ballRadius
                            if self.team1TouchCount == 1:
                                Match.receive(self)
                            elif self.team1TouchCount == 2:
                                random.choice(Match.toss(self), Match.ctoss(self))
                            elif self.team1TouchCount == 3:
                                Match.spike(self)
                        
                    elif ((self.player1WidthBL < self.ballWidth < self.player1WidthBL + 40  
                        and self.player1HeightBL-40 < self.ballHeight < self.player1HeightBL) or 
                        (self.player1WidthBM < self.ballWidth < self.player1WidthBM + 40  
                        and self.player1HeightBM-40 < self.ballHeight < self.player1HeightBM) or 
                        (self.player1WidthBR < self.ballWidth < self.player1WidthBR + 40  
                        and self.player1HeightBR-40 < self.ballHeight < self.player1HeightBR)):
                        self.ballVx = self.ballVx * .5

                        if (self.player1WidthBL < self.ballWidth < self.player1WidthBL + 40  
                        and self.player1HeightBL-40 < self.ballHeight < self.player1HeightBL):
                            self.ballWidth = self.player1WidthBL - self.ballRadius
                            if self.team1TouchCount == 1:
                                Match.receive(self)
                            elif self.team1TouchCount == 2:
                                random.choice(Match.toss(self), Match.ctoss(self))
                            elif self.team1TouchCount == 3:
                                Match.spike(self)
                        elif (self.player1WidthBM < self.ballWidth < self.player1WidthBM + 40  
                        and self.player1HeightBM-40 < self.ballHeight < self.player1HeightBM):
                            self.ballWidth = self.player1WidthBM - self.ballRadius
                            if self.team1TouchCount == 1:
                                Match.receive(self)
                            elif self.team1TouchCount == 2:
                                Match.toss(self) 
                            elif self.team1TouchCount == 3:
                                Match.spike(self)
                        elif (self.player1WidthBR < self.ballWidth < self.player1WidthBR + 40  
                        and self.player1HeightBR-40 < self.ballHeight < self.player1HeightBR):
                            self.ballWidth = self.player1WidthBR - self.ballRadius
                            if self.team1TouchCount == 1:
                                Match.receive(self)
                            elif self.team1TouchCount == 2:
                                random.choice(Match.toss(self), Match.ctoss(self)) 
                            elif self.team1TouchCount == 3:
                                Match.spike(self)

            elif Match.ballIntersectsTeam2(self):
                self.ballTime = 0
                Match.resetBallCalculation(self)
                if MatchOptions.PlayerCount == 1:
                    self.ballVx = -self.ballVx

                elif MatchOptions.PlayerCount == 2:
                    if (self.dot2WidthFront < self.ballWidth < self.dot2WidthFront + 40  
                            and self.dot2HeightFront-40 < self.ballHeight < self.dot2HeightFront):
                        self.team2TouchCount += 1
                        self.touchCount += 1
                        if self.team2TouchCount == 1:
                            Match.receive(self)
                        if self.team2TouchCount == 2:
                            Match.toss(self)
                        elif self.team2TouchCount == 3:
                            Match.spike(self)
                    elif (self.dot2WidthBack < self.ballWidth < self.dot2WidthBack + 40  
                            and self.dot2HeightBack-40 < self.ballHeight < self.dot2HeightBack):
                        self.team2TouchCount += 1
                        self.touchCount += 1
                        if self.team2TouchCount == 1:
                            Match.receive(self)
                        if self.team2TouchCount == 2:
                            Match.toss(self)
                        elif self.team2TouchCount == 3:
                            Match.spike(self)

                elif MatchOptions.PlayerCount == 6:
                    if ((self.player2WidthTL < self.ballWidth < self.player2WidthTL + 40  
                        and self.player2HeightTL-40 < self.ballHeight < self.player2HeightTL) or
                        (self.player2WidthTM < self.ballWidth < self.player2WidthTM + 40  
                        and self.player2HeightTM-40 < self.ballHeight < self.player2HeightBM) or
                        (self.player2WidthTR < self.ballWidth < self.player1WidthTR + 40  
                        and self.player2HeightTR-40 < self.ballHeight < self.player2HeightTR)):
                        self.ballVx = -self.ballVx
                        self.touchCount += 1
                        self.team2TouchCount += 1
                        if (self.player2WidthTL < self.ballWidth < self.player2WidthTL + 40  
                        and self.player2HeightTL-40 < self.ballHeight < self.player2HeightTL):
                            self.ballWidth = self.player2WidthTL - self.ballRadius
                            if self.team1TouchCount == 1:
                                Match.receive(self)
                            elif self.team1TouchCount == 2:
                                random.choice(Match.toss(self), Match.ctoss(self))
                            elif self.team1TouchCount == 3:
                                Match.spike(self)
                        if (self.player2WidthTM < self.ballWidth < self.player2WidthTM + 40  
                        and self.player2HeightTM-40 < self.ballHeight < self.player2HeightTM):
                            self.ballWidth = self.player2WidthTL - self.ballRadius
                            if self.team1TouchCount == 1:
                                Match.receive(self)
                            elif self.team1TouchCount == 2:
                                Match.toss(self) 
                            elif self.team1TouchCount == 3:
                                Match.spike(self)
                        if (self.player2WidthTR < self.ballWidth < self.player2WidthTR + 40  
                        and self.player2HeightTR-40 < self.ballHeight < self.player1HeightTR):
                            self.ballWidth = self.player2WidthTR - self.ballRadius
                            if self.team1TouchCount == 1:
                                Match.receive(self)
                            elif self.team1TouchCount == 2:
                                random.choice(Match.toss(self), Match.ctoss(self)) 
                            elif self.team1TouchCount == 3:
                                Match.spike(self)
                        
                    elif ((self.player2WidthBL < self.ballWidth < self.player2WidthBL + 40  
                        and self.player2HeightBL-40 < self.ballHeight < self.player2HeightBL) or 
                        (self.player2WidthBM < self.ballWidth < self.player2WidthBM + 40  
                        and self.player2HeightBM-40 < self.ballHeight < self.player2HeightBM) or 
                        (self.player2WidthBR < self.ballWidth < self.player2WidthBR + 40  
                        and self.player2HeightBR-40 < self.ballHeight < self.player2HeightBR)):
                        self.ballVx = -self.ballVx * .5
                        self.touchCount += 1
                        self.team2TouchCount += 1

                        if (self.player2WidthBL < self.ballWidth < self.player2WidthBL + 40  
                        and self.player2HeightBL-40 < self.ballHeight < self.player2HeightBL):
                            self.ballWidth = self.player2WidthBL - self.ballRadius
                            if self.team1TouchCount == 1:
                                Match.receive(self)
                            elif self.team1TouchCount == 2:
                                random.choice(Match.toss(self), Match.ctoss(self))
                            elif self.team1TouchCount == 3:
                                Match.spike(self)
                        if (self.player2WidthBM < self.ballWidth < self.player2WidthBM + 40  
                        and self.player2HeightBM-40 < self.ballHeight < self.player2HeightBM):
                            self.ballWidth = self.player2WidthBM - self.ballRadius
                            if self.team1TouchCount == 1:
                                Match.receive(self)
                            elif self.team1TouchCount == 2:
                                Match.toss(self) 
                            elif self.team1TouchCount == 3:
                                Match.spike(self)
                        if (self.player2WidthBR < self.ballWidth < self.player2WidthBR + 40  
                        and self.player2HeightBR-40 < self.ballHeight < self.player2HeightBR):
                            self.ballWidth = self.player2WidthBR - self.ballRadius
                            if self.team1TouchCount == 1:
                                Match.receive(self)
                            elif self.team1TouchCount == 2:
                                random.choice(Match.toss(self), Match.ctoss(self))
                            elif self.team1TouchCount == 3:
                                Match.spike(self)
        else:
            self.rallyStarts = False
            if (self.ballTime > 3):         
                    if self.ballWidth < self.width/2:
                        self.team2TouchCount = 0
                        if ((self.ballWidth <= self.bottomLineL) or
                            (self.ballHeight >= self.courtNetTop) or 
                            (self.ballWidth <= self.courtNetBottom)): #switch this to if ball lands outside the bounds with the height of ball trajectory being 0
                            if self.team1TouchCount == 0:
                                Match.score1 += 1
                                self.servingSide = 0
                                self.rallyReset = True
                            else:
                                Match.score2 += 1
                                self.servingSide = 1
                                self.rallyReset = True
                        elif ((self.courtNetBottom <= self.ballHeight <= self.courtNetTop) and 
                            (self.bottomLineL <=self.ballWidth <= self.width/2)):
                                #Here have the endpoint of curve be within the court
                                Match.score2 += 1
                                self.servingSide = 1
                                self.rallyReset = True
                        elif self.team1TouchCount > 3:
                            Match.score2 += 1
                            self.servingSide = 1
                            self.rallyReset = True
                    elif self.ballWidth > self.width/2:
                        self.team1TouchCount = 0 
                        if self.team2TouchCount == 0:
                            if ((self.ballWidth - self.ballRadius >= self.width) or
                            (self.ballHeight + self.ballRadius >= self.height) or 
                            (self.ballWidth - self.ballRadius <= 0)): #switch this to if ball lands outside the bounds with the height of ball trajectory being 0
                                Match.score2 += 1
                                self.servingSide = 1
                                self.rallyReset = True
                        elif ((self.courtNetBottom <= self.ballHeight <= self.courtNetTop) and 
                            (self.width/2 <=self.ballWidth <= self.bottomLineR)):
                                #Here have the endpoint of curve be within the court
                                if self.team2TouchCount == 0:
                                    Match.score2 += 1
                                    self.servingSide = 1
                                    self.rallyReset = True
                                else:
                                    Match.score1 += 1
                                    self.servingSide = 0
                                    self.rallyReset = True
                        elif self.team2TouchCount > 3:
                            Match.score1 += 1
                            self.servingSide = 0
                            self.rallyReset = True
                    self.rallyStarts = False      
            

    def mousePressed(self, event):
        if self.paused == True:
            if event.x >= self.width/2 - 90 and event.x <= self.width/2 + 90:
                if event.y >= self.height/2 - 160 and event.y <= self.height/2 - 100:
                    Match.resetApp(self)
                    Match.score1 = 0
                    Match.score2 = 0
                if event.y >= self.height/2 - 60 and event.y <= self.height/2:
                    MatchOptions(width=1920, height=1080)
                if event.y >= self.height/2 + 40 and event.y <= self.height/2 + 100:
                    HomeScreen(width=1920, height=1080)
        '''if (self.ballTime > 3):
                    self.rallyStarts = False
                    if self.ballWidth < self.width/2:
                        self.team2TouchCount = 0
                        if ((self.ballWidth <= self.bottomLineL) or
                            (self.ballHeight >= self.courtNetTop) or 
                            (self.ballWidth <= self.courtNetBottom)): #switch this to if ball lands outside the bounds with the height of ball trajectory being 0
                            if self.team1TouchCount == 0:
                                Match.score1 += 1
                                self.servingSide = 0
                                self.rallyReset = True
                            else:
                                Match.score2 += 1
                                self.servingSide = 1
                                self.rallyReset = True
                        elif ((self.courtNetBottom <= self.ballHeight <= self.courtNetTop) and 
                            (self.bottomLineL <=self.ballWidth <= self.width/2)):
                                #Here have the endpoint of curve be within the court
                                Match.score2 += 1
                                self.servingSide = 1
                                self.rallyReset = True
                        elif self.team1TouchCount > 3:
                            Match.score2 += 1
                            self.servingSide = 1
                            self.rallyReset = True

                    elif self.ballWidth > self.width/2:
                        self.team1TouchCount = 0 
                        if self.team2TouchCount == 0:
                            if ((self.ballWidth - self.ballRadius >= self.width) or
                            (self.ballHeight + self.ballRadius >= self.height) or 
                            (self.ballWidth - self.ballRadius <= 0)): #switch this to if ball lands outside the bounds with the height of ball trajectory being 0
                                Match.score2 += 1
                                self.servingSide = 1
                                self.rallyReset = True
                        elif ((self.courtNetBottom <= self.ballHeight <= self.courtNetTop) and 
                            (self.width/2 <=self.ballWidth <= self.bottomLineR)):
                                #Here have the endpoint of curve be within the court
                                if self.team2TouchCount == 0:
                                    Match.score2 += 1
                                    self.servingSide = 1
                                    self.rallyReset = True
                                else:
                                    Match.score1 += 1
                                    self.servingSide = 0
                                    self.rallyReset = True
                        elif self.team2TouchCount > 3:
                            Match.score1 += 1
                            self.servingSide = 0
                            self.rallyReset = True
                    self.rallyStarts = False   '''

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
            and self.player1HeightTM-40 < self.ballHeight < self.player1HeightTM) or 
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
            and self.player2HeightTM-40 < self.ballHeight < self.player2HeightTM) or 
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
                    self.ballVx *= .5
                    self.ballVy *= .5
            elif (self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/12 < self.gageDotHeight 
                    < self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/6) or (self.gageY0_1 + 
                    5*(self.gageY1_1-self.gageY0_1)/6 < self.gageDotHeight < 
                    self.gageY0_1 + 11*(self.gageY1_1-self.gageY0_1)/12): #dark orange
                self.ballVx *= .6
                self.ballVy *= .6

            elif (self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/6 < self.gageDotHeight 
                    < self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/4) or (self.gageY0_1 + 
                    3*(self.gageY1_1-self.gageY0_1)/4 < self.gageDotHeight < self.gageY0_1 + 
                    5*(self.gageY1_1-self.gageY0_1)/6): #light orange
                self.ballVx *= .7
                self.ballVy *= .7

            elif (self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/4 < self.gageDotHeight
                    < self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/3) or (self.gageY0_1 + 
                    2*(self.gageY1_1-self.gageY0_1)/3 < self.gageDotHeight 
                    < self.gageY0_1 + 2*(self.gageY1_1-self.gageY0_1)/3): #Light yellow
                self.ballVx *= .8
                self.ballVy *= .8

            elif (self.gageY0_1 + (self.gageY1_1-self.gageY0_1)/3 < self.gageDotHeight 
                    < self.gageY0_1 + 5*(self.gageY1_1-self.gageY0_1)/12) or (self.gageY0_1 + 
                    7*(self.gageY1_1-self.gageY0_1)/12 < self.gageDotHeight
                    < self.gageY0_1 + 2*(self.gageY1_1-self.gageY0_1)/3): #Dark Yellow
                self.ballVx *= .9
                self.ballVy *= .9

            elif (self.gageY0_1 + 5*(self.gageY1_1-self.gageY0_1)/12 < self.gageDotHeight
                     < self.gageY0_1 + 7*(self.gageY1_1-self.gageY0_1)/12): #Green
                self.ballVx *= 1.1
                self.ballVy *= 1.1

    def jump(self):
        if self.jumpIsPressed == True:
            self.ballHeight += 15
            self.gageActivates = not self.gageActivates
            self.notServed = not self.notServed
            self.gagePressCount += 1
            if self.gagePressCount % 2==0 and self.gagePressCount > 0:
                Match.resetGage(self)
            self.ballHeight -= 15

    def movePlayer1AI(self):
        if Sides.playersInTeam1 == []:
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
                if Match.distance(self.dot1WidthFront, self.dot1HeightFront, self.dot1WidthBack, self.dot1HeightBack) < 10:
                    self.servingSide = 1
                    Match.resetPlayer1(self)
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
                if ((Match.distance(self.player1WidthTL, self.player1HeightTL, self.player1WidthTM, self.player1HeightTM) < 10) or 
                    Match.distance(self.player1WidthTL, self.player1HeightTL, self.player1WidthTR, self.player1HeightTR) < 10 or
                    Match.distance(self.player1WidthTL, self.player1HeightTL, self.player1WidthBR, self.player1HeightBR) < 10 or 
                    Match.distance(self.player1WidthTL, self.player1HeightTL, self.player1WidthBL, self.player1HeightBL) < 10 or
                    Match.distance(self.player1WidthTL, self.player1HeightTL, self.player1WidthBM, self.player1HeightBM) < 10 or
                    Match.distance(self.player1WidthTM, self.player1HeightTM, self.player1WidthBR, self.player1HeightBR) < 10 or
                    Match.distance(self.player1WidthTM, self.player1HeightTM, self.player1WidthBL, self.player1HeightBL) < 10 or
                    Match.distance(self.player1WidthTM, self.player1HeightTM, self.player1WidthBM, self.player1HeightBM) < 10 or 
                    Match.distance(self.player1WidthTM, self.player1HeightTM, self.player1WidthTR, self.player1HeightTR) < 10 or
                    Match.distance(self.player1WidthTR, self.player1HeightTR, self.player1WidthBL, self.player1HeightBL) < 10 or
                    Match.distance(self.player1WidthTR, self.player1HeightTR, self.player1WidthBM, self.player1HeightBM) < 10 or
                    Match.distance(self.player1WidthTR, self.player1HeightTR, self.player1WidthBR, self.player1HeightBR) < 10 or
                    Match.distance(self.player1WidthBR, self.player1HeightBR, self.player1WidthBM, self.player1HeightBM) < 10 or
                    Match.distance(self.player1WidthBR, self.player1HeightBR, self.player1WidthBL, self.player1HeightBL) < 10 or
                    Match.distance(self.player1WidthBM, self.player1HeightBM, self.player1WidthBL, self.player1HeightBL) < 10):
                        self.servingSide = 1
                        Match.resetPlayer1(self)
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
        if Sides.playersInTeam2 == []:
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
                if Match.distance(self.dot2WidthFront, self.dot2HeightFront, self.dot2WidthBack, self.dot2HeightBack) < 10:
                    self.servingSide = 0
                    Match.resetPlayer2(self)
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
                    if ((Match.distance(self.player2WidthTL, self.player2HeightTL, self.player2WidthTM, self.player2HeightTM) < 10) or 
                    Match.distance(self.player2WidthTL, self.player2HeightTL, self.player2WidthTR, self.player2HeightTR) < 10 or
                    Match.distance(self.player2WidthTL, self.player2HeightTL, self.player2WidthBR, self.player2HeightBR) < 10 or 
                    Match.distance(self.player2WidthTL, self.player2HeightTL, self.player2WidthBL, self.player2HeightBL) < 10 or
                    Match.distance(self.player2WidthTL, self.player2HeightTL, self.player2WidthBM, self.player2HeightBM) < 10 or
                    Match.distance(self.player2WidthTM, self.player2HeightTM, self.player2WidthBR, self.player2HeightBR) < 10 or
                    Match.distance(self.player2WidthTM, self.player2HeightTM, self.player2WidthBL, self.player2HeightBL) < 10 or
                    Match.distance(self.player2WidthTM, self.player2HeightTM, self.player2WidthBM, self.player2HeightBM) < 10 or 
                    Match.distance(self.player2WidthTM, self.player2HeightTM, self.player2WidthTR, self.player2HeightTR) < 10 or
                    Match.distance(self.player2WidthTR, self.player2HeightTR, self.player2WidthBL, self.player2HeightBL) < 10 or
                    Match.distance(self.player2WidthTR, self.player2HeightTR, self.player2WidthBM, self.player2HeightBM) < 10 or
                    Match.distance(self.player2WidthTR, self.player2HeightTR, self.player2WidthBR, self.player2HeightBR) < 10 or
                    Match.distance(self.player2WidthBR, self.player2HeightBR, self.player2WidthBM, self.player2HeightBM) < 10 or
                    Match.distance(self.player2WidthBR, self.player2HeightBR, self.player2WidthBL, self.player2HeightBL) < 10 or
                    Match.distance(self.player2WidthBM, self.player2HeightBM, self.player2WidthBL, self.player2HeightBL) < 10):
                        self.servingSide = 0
                        Match.resetPlayer2(self)
                    
                    if self.width/2 <self.ballWidth < self.player2WidthTL: #If the ball is on the left side of the player on screen
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

    def topSpinServe(self, event):
        self.rallyStarts = True
        self.gageActivates = not self.gageActivates
        self.notServed = not self.notServed
        self.gagePressCount += 1
        if self.gagePressCount % 2==0 and self.gagePressCount > 0:
            if self.servingSide == 0:
                self.ballVx = self.ballVx
                if self.serveOption == 1:
                    self.ballAngle = 50
                    self.ballVy = .85 * self.ballVy
                if self.serveOption == 2:
                    self.ballAngle = 40
                    self.ballVy = 1.15 * self.ballVy
            if self.servingSide == 1:
                self.ballVx = -self.ballVx
                if self.serveOption == 1:
                    self.ballAngle = 50
                    self.ballVy = .85 * self.ballVy
                if self.serveOption == 2:
                    self.ballAngle = 40
                    self.ballVy = 1.15 * self.ballVy
        Match.resetGage(self)
                
        #if player 1 is serving
        

    def floaterServe(self, event):
        self.rallyStarts = True
        self.dotDx = -self.dotDx
        self.dotDy = random.randint(-3, -1)

    def toss(self):
        self.touchCount += 1
        #if setter top or bottom index:
                #ballHeight = middleplayerHeight
                #ballHeight = middleplayerWidth
        #elif setter is middle:
            #randomly select one of the widths for bottom or top
            #randomly select one of the heights for bottom or top
        tossList = []
        distanceBallBack1 = Match.distance(self.dot1WidthBack, self.dot1HeightBack, self.ballWidth, self.ballHeight)
        distanceBallFront1 = Match.distance(self.dot1WidthFront, self.dot1HeightFront, self.ballWidth, self.ballHeight)
        distanceBallBack2 = Match.distance(self.dot2WidthBack, self.dot2HeightBack, self.ballWidth, self.ballHeight)
        distanceBallFront2 = Match.distance(self.dot2WidthFront, self.dot2HeightFront, self.ballWidth, self.ballHeight)
        if MatchOptions.PlayerCount == 2:
            '''if self.ballWidth > self.width/2:
                if distanceBallFront2 < distanceBallBack2:
                    if not (self.dot2WidthBack < self.ballWidth < self.dot2WidthBack + 40  
                    and self.dot2HeightBack-40 < self.ballHeight < self.dot2HeightBack):
                        self.ballAngle = 80
                elif distanceBallFront2 > distanceBallBack2:
                    if not (self.dot2WidthFront < self.ballWidth < self.dot2WidthFront + 40  
                    and self.dot2HeightFront-40 < self.ballHeight < self.dot2HeightFront):
                        self.ballSpeed = .25 * self.ballSpeed
                        self.ballVx = -self.ballVx
                        self.ballAngle = 80
            elif self.ballWidth < self.width/2:
                if distanceBallFront1 < distanceBallBack1:
                    if not (self.dot1WidthBack < self.ballWidth < self.dot1WidthBack + 40  
                    and self.dot1HeightBack-40 < self.ballHeight < self.dot1HeightBack):
                        self.ballAngle = 80
                elif distanceBallFront1 > distanceBallBack1:
                    if not (self.dot1WidthFront < self.ballWidth < self.dot1WidthFront + 40  
                    and self.dot1HeightFront-40 < self.ballHeight < self.dot1HeightFront):
                        self.ballVx = -self.ballVx
                        self.ballAngle = 80'''
                
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
            self.ballSpeed = self.ballSpeed * .9
        elif MatchOptions.PlayerCount == 6:
            distanceTL = int(Match.distance(self.player2WidthTL, self.player2HeightTL,
                                            self.ballWidth, self.ballHeight))
            distanceTR = int(Match.distance(self.player2WidthTR, self.player2HeightTR,
                                self.ballWidth, self.ballHeight))
            distanceTM = int(Match.distance(self.player2WidthTM, self.player2HeightTM,
                                self.ballWidth, self.ballHeight))
            distanceBL = int(Match.distance(self.ballWidth, self.ballHeight,
                                            self.player2WidthBL, self.player2HeightBL))
            distanceBR = int(Match.distance(self.ballWidth, self.ballHeight,
                                self.player2WidthBR, self.player2HeightBR))
            distanceBM = int(Match.distance(self.ballWidth, self.ballHeight,
                                self.player2WidthBM, self.player2HeightBM))
            if (self.player2WidthTL < self.ballWidth < self.player2WidthTL + 40  
            and self.player2HeightTL-40 < self.ballHeight < self.player2HeightTL):                    
                if distanceTL < distanceBL:
                    self.ballWidth = self.player2WidthBL
                    self.ballHeight = self.player2HeightBL
                elif distanceTL < distanceTM:
                    self.ballWidth = self.player2WidthTM
                    self.ballHeight = self.player2HeightTM
            elif (self.player2WidthBL < self.ballWidth < self.player2WidthBL + 40  
            and self.player2HeightBL-40 < self.ballHeight < self.player2HeightBL):
                if distanceBL < distanceTL:
                    self.ballWidth = self.player2WidthTL
                    self.ballHeight = self.player2HeightTL
                elif distanceBL < distanceBM:
                    self.ballWidth = self.player2WidthBM
                    self.ballHeight = self.player2HeightBM
            elif (self.player2WidthTM < self.ballWidth < self.player1WidthTM + 40  
            and self.player2HeightTM-40 < self.ballHeight < self.player2HeightTM):
                x = random.choice(0,1)
                if x == 1:
                    if distanceTM < distanceTR:
                        self.ballWidth = self.player2WidthTR
                        self.ballHeight = self.player2HeightTR
                elif x == 0:
                    if distanceTM < distanceTL:
                        self.ballWidth = self.player2WidthTL
                        self.ballHeight = self.player2HeightTL
                elif distanceTM < distanceBM:
                    self.ballWidth = self.player2WidthBM
                    self.ballHeight = self.player2HeightBM
            elif (self.player2WidthBM < self.ballWidth < self.player2WidthBM + 40  
            and self.player2HeightBM-40 < self.ballHeight < self.player2HeightBM):
                x = random.choice(0,1)
                if x == 1:
                    if distanceBM < distanceTR:
                        self.ballWidth = self.player2WidthTR
                        self.ballHeight = self.player2HeightTR
                elif x == 0:
                    if distanceBM < distanceTL:
                        self.ballWidth = self.player2WidthTL
                        self.ballHeight = self.player2HeightTL
                elif distanceBM < distanceTM:
                    self.ballWidth = self.player2WidthTM
                    self.ballHeight = self.player2HeightTM    
            elif (self.player2WidthTR < self.ballWidth < self.player2WidthTR + 40  
            and self.player2HeightTR-40 < self.ballHeight < self.player2HeightTR):                    
                if distanceTR < distanceBR:
                    self.ballWidth = self.player2WidthBR
                    self.ballHeight = self.player2HeightBR
                elif distanceTR < distanceTM:
                    self.ballWidth = self.player2WidthTM
                    self.ballHeight = self.player2HeightTM
            elif (self.player2WidthBR < self.ballWidth < self.player2WidthBR + 40  
            and self.player2HeightBR-40 < self.ballHeight < self.player2HeightBR):                    
                if distanceBR < distanceTR:
                    self.ballWidth = self.player2WidthTR
                    self.ballHeight = self.player2HeightTR
                elif distanceTR < distanceBM:
                    self.ballWidth = self.player2WidthBM
                    self.ballHeight = self.player2HeightBM

            distanceTL1 = int(Match.distance(self.player1WidthTL, self.player1HeightTL,
                                            self.ballWidth, self.ballHeight))
            distanceTR1 = int(Match.distance(self.player1WidthTR, self.player1HeightTR,
                                self.ballWidth, self.ballHeight))
            distanceTM1 = int(Match.distance(self.player1WidthTM, self.player1HeightTM,
                                self.ballWidth, self.ballHeight))
            distanceBL1 = int(Match.distance(self.ballWidth, self.ballHeight,
                                            self.player1WidthBL, self.player1HeightBL))
            distanceBR1 = int(Match.distance(self.ballWidth, self.ballHeight,
                                self.player1WidthBR, self.player1HeightBR))
            distanceBM1 = int(Match.distance(self.ballWidth, self.ballHeight,
                                self.player1WidthBM, self.player1HeightBM))
            if (self.player1WidthTL < self.ballWidth < self.player1WidthTL + 40  
            and self.player1HeightTL-40 < self.ballHeight < self.player1HeightTL):                    
                if distanceTL1 < distanceBL1:
                    self.ballWidth = self.player1WidthBL
                    self.ballHeight = self.player1HeightBL
                elif distanceTL1 < distanceTM1:
                    self.ballWidth = self.player1WidthTM
                    self.ballHeight = self.player1HeightTM
            elif (self.player1WidthBL < self.ballWidth < self.player1WidthBL + 40  
            and self.player1HeightBL-40 < self.ballHeight < self.player1HeightBL):
                if distanceBL1 < distanceTL1:
                    self.ballWidth = self.player1WidthTL
                    self.ballHeight = self.player1HeightTL
                elif distanceBL1 < distanceBM1:
                    self.ballWidth = self.player1WidthBM
                    self.ballHeight = self.player1HeightBM
            elif (self.player1WidthTM < self.ballWidth < self.player1WidthTM + 40  
            and self.player1HeightTM-40 < self.ballHeight < self.player1HeightTM):
                x = random.choice(0,1)
                if x == 1:
                    if distanceTM1 < distanceTR1:
                        self.ballWidth = self.player1WidthTR
                        self.ballHeight = self.player1HeightTR
                elif x == 0:
                    if distanceTM1 < distanceTL1:
                        self.ballWidth = self.player1WidthTL
                        self.ballHeight = self.player1HeightTL
                elif distanceTM1 < distanceBM1:
                    self.ballWidth = self.player1WidthBM
                    self.ballHeight = self.player1HeightBM
            elif (self.player1WidthBM < self.ballWidth < self.player1WidthBM + 40  
            and self.player1HeightBM-40 < self.ballHeight < self.player1HeightBM):
                x = random.choice(0,1)
                if x == 1:
                    if distanceBM1 < distanceTR1:
                        self.ballWidth = self.player1WidthTR
                        self.ballHeight = self.playerHeightTR
                elif x == 0:
                    if distanceBM1 < distanceTL1:
                        self.ballWidth = self.player1WidthTL
                        self.ballHeight = self.player1HeightTL
                elif distanceBM1 < distanceTM1:
                    self.ballWidth = self.player1WidthTM
                    self.ballHeight = self.player1HeightTM    
            elif  (self.player1WidthTR < self.ballWidth < self.player1WidthTR + 40  
            and self.player1HeightTR-40 < self.ballHeight < self.player1HeightTR):                    
                if distanceTR1 < distanceBR1:
                    self.ballWidth = self.player1WidthBR
                    self.ballHeight = self.player1HeightBR
                elif distanceTR1 < distanceTM1:
                    self.ballWidth = self.player1WidthTM
                    self.ballHeight = self.player1HeightTM
            elif (self.player1WidthBR < self.ballWidth < self.player1WidthBR + 40  
            and self.player1HeightBR-40 < self.ballHeight < self.player1HeightBR):                    
                if distanceBR1 < distanceTR1:
                    self.ballWidth = self.player1WidthTR
                    self.ballHeight = self.player1HeightTR
                elif distanceTR1 < distanceBM1:
                    self.ballWidth = self.player1WidthBM
                    self.ballHeight = self.player1HeightBM
    def ctoss(self):
        if MatchOptions.PlayerCount == 6:
            distanceTL = int(Match.distance(self.player2WidthTL, self.player2HeightTL,
                                            self.ballWidth, self.ballHeight))
            distanceTR = int(Match.distance(self.player2WidthTR, self.player2HeightTR,
                                self.ballWidth, self.ballHeight))
            distanceBL = int(Match.distance(self.ballWidth, self.ballHeight,
                                            self.player2WidthBL, self.player2HeightBL))
            distanceBR = int(Match.distance(self.ballWidth, self.ballHeight,
                                self.player2WidthBR, self.player2HeightBR))

            if (self.player2WidthTL < self.ballWidth < self.player2WidthTL + 40  
            and self.player2HeightTL-40 < self.ballHeight < self.player2HeightTL):                    
                if distanceTL < distanceTR:
                    self.ballWidth = self.player2WidthTR
                    self.ballHeight = self.player2HeightTR
            elif (self.player2WidthBL < self.ballWidth < self.player2WidthBL + 40  
            and self.player2HeightBL-40 < self.ballHeight < self.player2HeightBL):
                if distanceBL < distanceBR:
                    self.ballWidth = self.player2WidthBR
                    self.ballHeight = self.player2HeightBR
            elif (self.player2WidthTR < self.ballWidth < self.player2WidthTR + 40  
            and self.player2HeightTR-40 < self.ballHeight < self.player2HeightTR):                    
                if distanceTR < distanceTL:
                    self.ballWidth = self.player2WidthTL
                    self.ballHeight = self.player2HeightTL
            elif (self.player2WidthBR < self.ballWidth < self.player2WidthBR + 40  
            and self.player2HeightBR-40 < self.ballHeight < self.player2HeightBR):                    
                if distanceBR < distanceBL:
                    self.ballWidth = self.player2WidthBL
                    self.ballHeight = self.player2HeightBL

            distanceTL1 = int(Match.distance(self.player1WidthTL, self.player1HeightTL,
                                            self.ballWidth, self.ballHeight))
            distanceTR1 = int(Match.distance(self.player1WidthTR, self.player1HeightTR,
                                self.ballWidth, self.ballHeight))
            distanceBL1 = int(Match.distance(self.ballWidth, self.ballHeight,
                                            self.player1WidthBL, self.player1HeightBL))
            distanceBR1 = int(Match.distance(self.ballWidth, self.ballHeight,
                                self.player1WidthBR, self.player1HeightBR))


            if (self.player1WidthTL < self.ballWidth < self.player1WidthTL + 40  
            and self.player1HeightTL-40 < self.ballHeight < self.player1HeightTL):                    
                if distanceTL1 < distanceTR1:
                    self.ballWidth = self.player1WidthTR
                    self.ballHeight = self.player1HeightTR
            elif (self.player1WidthBL < self.ballWidth < self.player1WidthBL + 40  
            and self.player1HeightBL-40 < self.ballHeight < self.player1HeightBL):
                if distanceBL1 < distanceBR1:
                    self.ballWidth = self.player1WidthBR
                    self.ballHeight = self.player1HeightBR
            elif  (self.player1WidthTR < self.ballWidth < self.player1WidthTR + 40  
            and self.player1HeightTR-40 < self.ballHeight < self.player1HeightTR):                    
                if distanceTR1 < distanceTL1:
                    self.ballWidth = self.player1WidthTL
                    self.ballHeight = self.player1HeightTL
            elif (self.player1WidthBR < self.ballWidth < self.player1WidthBR + 40  
            and self.player1HeightBR-40 < self.ballHeight < self.player1HeightBR):                    
                if distanceBR1 < distanceBL1:
                    self.ballWidth = self.player1WidthBL
                    self.ballHeight = self.player1HeightBL

        
    def spike(self):
        self.touchCount += 1
        if self.balltime < 2:          
            if MatchOptions.PlayerCount == 2:
                    if self.ballWidth < self.width/2:
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
            if MatchOptions.PlayerCount == 6:
                if self.ballWidth < self.width/2:
                    distance1 = int(Match.distance(self.player1WidthTL, self.player1HeightTL,
                                            self.player1WidthBL, self.player1HeightBL))
                    distance2 = int(Match.distance(self.player1WidthTR, self.player1HeightTR,
                                self.player1WidthBR, self.player1HeightBR))
                    distance3 = int(Match.distance(self.player1WidthTM, self.player1HeightTM,
                                self.player1WidthBM, self.player1HeightBM))
                    self.gapsTeam2.append(((self.player1WidthTL + self.player1WidthBL)/2, self.player1HeightTL))
                    self.gapsTeam2.append(((self.player1WidthTL + self.player1WidthBL)/2, (self.player1HeightTL + self.player1HeightBL)/2))
                    self.gapsTeam2.append(((self.player1WidthTL - distance1/2, self.player1HeightTL)))
                    self.gapsTeam2.append(((self.player1WidthTL + distance1/2, self.player1HeightTL)))
                    self.gapsTeam2.append(((self.player1WidthTL, self.player1HeightTL + distance1/2)))
                    self.gapsTeam2.append(((self.player1WidthTL, self.player1HeightTL - distance1/2)))
                    self.gapsTeam2.append(((self.player1WidthTL, (self.player1HeightTL + self.player1HeightBL)/2)))

                    self.gapsTeam2.append(((self.player1WidthTR + self.player1WidthBR)/2, self.player1HeightTR))
                    self.gapsTeam2.append(((self.player1WidthTR + self.player1WidthBR)/2, (self.player1HeightTR + self.player1HeightBR)/2))
                    self.gapsTeam2.append(((self.player1WidthTR - distance2/2, self.player1HeightTR)))
                    self.gapsTeam2.append(((self.player1WidthTR + distance2/2, self.player1HeightTR)))
                    self.gapsTeam2.append(((self.player1WidthTR, self.player1HeightTR + distance2/2)))
                    self.gapsTeam2.append(((self.player1WidthTR, self.player1HeightTR - distance2/2)))
                    self.gapsTeam2.append(((self.player1WidthTR, (self.player1HeightTR + self.player1HeightBR)/2)))

                    self.gapsTeam2.append(((self.player1WidthTM + self.player1WidthBM)/2, self.player1HeightTM))
                    self.gapsTeam2.append(((self.player1WidthTM + self.player1WidthBM)/2, (self.player1HeightTM + self.player1HeightBM)/2))
                    self.gapsTeam2.append(((self.player1WidthTM - distance3/2, self.player1HeightTM)))
                    self.gapsTeam2.append(((self.player1WidthTM + distance3/2, self.player1HeightTM)))
                    self.gapsTeam2.append(((self.player1WidthTM, self.player1HeightTM + distance3/2)))
                    self.gapsTeam2.append(((self.player1WidthTM, self.player1HeightTM - distance3/2)))
                    self.gapsTeam2.append(((self.player1WidthTM, (self.player1HeightTM + self.player1HeightBM)/2)))
                    if Match.ballIntersectsTeam2(self):
                        if MatchOptions.difficulty == "Easy" or MatchOptions.difficulty == "Medium":
                            self.ballWidth , self.ballHeight = random.choice(self.gapsTeam2)
                        elif MatchOptions.difficulty == "Hard":
                            self.ballWidth , self.ballHeight = max(self.gapsTeam2)
                else:
                    distance1 = int(Match.distance(self.player2WidthTL, self.player2HeightTL,
                                            self.player2WidthBL, self.player2HeightBL))
                    distance2 = int(Match.distance(self.player2WidthTR, self.player2HeightTR,
                                self.player2WidthBR, self.player2HeightBR))
                    distance3 = int(Match.distance(self.player2WidthTM, self.player2HeightTM,
                                self.player2WidthBM, self.player2HeightBM))
                    self.gapsTeam2.append(((self.player2WidthTL + self.player2WidthBL)/2, self.player2HeightTL))
                    self.gapsTeam2.append(((self.player2WidthTL + self.player2WidthBL)/2, (self.player2HeightTL + self.player2HeightBL)/2))
                    self.gapsTeam2.append(((self.player2WidthTL - distance1/2, self.player2HeightTL)))
                    self.gapsTeam2.append(((self.player2WidthTL + distance1/2, self.player2HeightTL)))
                    self.gapsTeam2.append(((self.player2WidthTL, self.player2HeightTL + distance1/2)))
                    self.gapsTeam2.append(((self.player2WidthTL, self.player2HeightTL - distance1/2)))
                    self.gapsTeam2.append(((self.player2WidthTL, (self.player2HeightTL + self.player2HeightBL)/2)))

                    self.gapsTeam2.append(((self.player2WidthTR + self.player2WidthBR)/2, self.player2HeightTR))
                    self.gapsTeam2.append(((self.player2WidthTR + self.player2WidthBR)/2, (self.player2HeightTR + self.player2HeightBR)/2))
                    self.gapsTeam2.append(((self.player2WidthTR - distance2/2, self.player2HeightTR)))
                    self.gapsTeam2.append(((self.player2WidthTR + distance2/2, self.player2HeightTR)))
                    self.gapsTeam2.append(((self.player2WidthTR, self.player2HeightTR + distance2/2)))
                    self.gapsTeam2.append(((self.player2WidthTR, self.player2HeightTR - distance2/2)))
                    self.gapsTeam2.append(((self.player2WidthTR, (self.player2HeightTR + self.player2HeightBR)/2)))

                    self.gapsTeam2.append(((self.player2WidthTM + self.player2WidthBM)/2, self.player2HeightTM))
                    self.gapsTeam2.append(((self.player2WidthTM + self.player2WidthBM)/2, (self.player2HeightTM + self.player2HeightBM)/2))
                    self.gapsTeam2.append(((self.player2WidthTM - distance3/2, self.player2HeightTM)))
                    self.gapsTeam2.append(((self.player2WidthTM + distance3/2, self.player2HeightTM)))
                    self.gapsTeam2.append(((self.player2WidthTM, self.player2HeightTM + distance3/2)))
                    self.gapsTeam2.append(((self.player2WidthTM, self.player2HeightTM - distance3/2)))
                    self.gapsTeam2.append(((self.player2WidthTM, (self.player2HeightTM + self.player2HeightBM)/2)))
                    if Match.ballIntersectsTeam1(self):
                        if MatchOptions.difficulty == "Easy" or MatchOptions.difficulty == "Medium":
                            self.ballWidth , self.ballHeight = random.choice(self.gapsTeam1)
                        elif MatchOptions.difficulty == "Hard":
                            self.ballWidth , self.ballHeight = max(self.gapsTeam1)

                self.ballVx *= 2
                self.ballVy *= 1.1

    def receive(self):
        if self.ballY >= self.ballHeight:
                if self.ballWidth < self.width/2 and Match.ballIntersectsTeam1(self):
                    self.ballSpeed = .75 * self.ballSpeed
                    self.ballVx = self.ballVx
                if self.ballWidth > self.width/2 and Match.ballIntersectsTeam2(self):
                    self.ballSpeed = .75 * self.ballSpeed
                    self.ballVx = -self.ballVx
                

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
            canvas.create_oval(self.dot1Width, self.dot1Height, self.dot1Width + 40, self.dot1Height - 40, fill = f"{self.fillTeam1}")
        elif MatchOptions.PlayerCount == 2:
            canvas.create_oval(self.dot1WidthFront, self.dot1HeightFront, self.dot1WidthFront + 40, self.dot1HeightFront - 40, fill = f"{self.fillTeam1}", outline = self.fillTeam1Front, width = 3)
            canvas.create_oval(self.dot1WidthBack, self.dot1HeightBack, self.dot1WidthBack + 40, self.dot1HeightBack - 40, fill = f"{self.fillTeam1}", outline = self.fillTeam1Back, width = 3)
        elif MatchOptions.PlayerCount == 6:
            canvas.create_oval(self.player1WidthTM, self.player1HeightTM, self.player1WidthTM + 40, self.player1HeightTM - 40, fill = f"{self.fillTeam1}", outline = self.fillTeam1TM, width = 3) #Top Middle
            canvas.create_oval(self.player1WidthBM, self.player1HeightBM, self.player1WidthBM + 40, self.player1HeightBM - 40, fill = f"{self.fillTeam1}", outline = self.fillTeam1BM, width = 3) #Back Middle
            canvas.create_oval(self.player1WidthBL, self.player1HeightBL, self.player1WidthBL + 40, self.player1HeightBL - 40, fill = f"{self.fillTeam1}", outline = self.fillTeam1BL, width = 3) #Back left in court
            canvas.create_oval(self.player1WidthTL, self.player1HeightTL, self.player1WidthTL + 40, self.player1HeightTL - 40, fill = f"{self.fillTeam1}", outline = self.fillTeam1TL, width = 3) #Top Left
            canvas.create_oval(self.player1WidthTR, self.player1HeightTR, self.player1WidthTR + 40, self.player1HeightTR - 40, fill = f"{self.fillTeam1}", outline = self.fillTeam1TR, width = 3) #Top Right
            canvas.create_oval(self.player1WidthBR, self.player1HeightBR, self.player1WidthBR + 40, self.player1HeightBR - 40, fill = f"{self.fillTeam1}", outline = self.fillTeam1BR, width = 3) #Bottom Right

    def drawTeam2(self, canvas):
        if MatchOptions.PlayerCount == 1:
            canvas.create_oval(self.dot2Width, self.dot2Height, self.dot2Width + 40, self.dot2Height - 40, fill = f"{self.fillTeam2}")
        elif MatchOptions.PlayerCount == 2:
            canvas.create_oval(self.dot2WidthFront, self.dot2HeightFront, self.dot2WidthFront + 40, self.dot2HeightFront - 40, fill = f"{self.fillTeam2}", outline = self.fillTeam2Front, width = 3)
            canvas.create_oval(self.dot2WidthBack, self.dot2HeightBack, self.dot2WidthBack + 40, self.dot2HeightBack - 40, fill = f"{self.fillTeam2}", outline = self.fillTeam2Back, width = 3)
        elif MatchOptions.PlayerCount == 6:
            canvas.create_oval(self.player2WidthTM, self.player2HeightTM, self.player2WidthTM + 40, self.player2HeightTM - 40, fill = f"{self.fillTeam2}", outline = self.fillTeam2TM, width = 3) #Top Middle
            canvas.create_oval(self.player2WidthBM, self.player2HeightBM, self.player2WidthBM + 40, self.player2HeightBM - 40, fill = f"{self.fillTeam2}", outline = self.fillTeam2BM, width = 3) #Back Middle
            canvas.create_oval(self.player2WidthBL, self.player2HeightBL, self.player2WidthBL + 40, self.player2HeightBL - 40, fill = f"{self.fillTeam2}", outline = self.fillTeam2BL, width = 3) #Back left in court
            canvas.create_oval(self.player2WidthTL, self.player2HeightTL, self.player2WidthTL + 40, self.player2HeightTL - 40, fill = f"{self.fillTeam2}", outline = self.fillTeam2TL, width = 3) #Top Left
            canvas.create_oval(self.player2WidthTR, self.player2HeightTR, self.player2WidthTR + 40, self.player2HeightTR + 40, fill = f"{self.fillTeam2}", outline = self.fillTeam2TR, width = 3) #Top Right
            canvas.create_oval(self.player2WidthBR, self.player2HeightBR, self.player2WidthBR + 40, self.player2HeightBR + 40, fill = f"{self.fillTeam2}", outline = self.fillTeam2BR, width = 3) #Bottom Right

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


######## Calculators ########
    #This physics-based calculation that I based my code off of is from a website explaining projectile motion
    #https://www.assignmentexpert.com/blog/modeling-projectile-motion-using-python/
    #This is being used for the ball trajectory which I write up all myself in moveBall1
    def VxCalculator(self, dt):
        self.ballVx = self.ballVx + self.ballAx*self.ballDt 
        return self.ballVx
    def VyCalculator(self, dt):
        self.ballVy = self.ballVy + self.ballAy*self.ballDt 
        return self.ballVy
    def ballXCalculator(self, dt):
        self.ballX = self.ballX + 0.5*(self.ballVx + self.VxCalculator(self.ballDt))*self.ballDt 
        return self.ballVx
    def ballYCalculator(self, dt):
        self.ballY = self.ballY + 0.5*(self.ballVy + self.VyCalculator(self.ballDt))*self.ballDt
        return self.ballVy
    def step(self):
        self.ballTime = self.ballTime + self.ballDt    


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
        canvas.create_text(self.width/2 - 450, 80, text = f"{self.team1TouchCount}", font = "Arial 18 bold")
        #Do the same with Team 2 on the right
        canvas.create_text(self.width/2 + 450, 55, text = f"{self.Team2}", font = "Arial 24 bold")
        canvas.create_text(self.width/2 + 450, 80, text = f"{self.team2TouchCount}", font = "Arial 18 bold")
        Match.drawVolleyBall(self, canvas)
        Match.drawTeam1(self, canvas)
        Match.drawTeam2(self, canvas)
        if self.paused == True:
            Match.drawPaused(self, canvas)
        if self.notServed == False:
            Match.drawHitGage(self, canvas)
        if self.rallyStarts == False:
            canvas.create_text(self.width/2, self.height/2, text = "Press any key to start next rally", font = "Arial 18 bold")

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
        self.background = self.loadImage("SunnyBackground.jpg")
        #Background of a sunny volleyball court
        #taken from free wallpaper website
        #t.ly/nlkR

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

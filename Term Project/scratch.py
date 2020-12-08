    def moveBall1(self):
        #Edge calculation similar to pong    
        #self.ballWidth += self.dotDx
        #self.ballHeight += self.dotDy 
        self.ballWidth = ballXCalculator(self, self.ballDt):
        self.ballHeight = ballYCalculator(self, self.ballDt):
        if Match.ballIntersectsTeam1(self):
            self.time = 0
            if MatchOptions.PlayerCount == 1:
                self.ballVx = -self.Vx

            elif MatchOptions.PlayerCount == 2:
                if (self.dot1WidthFront < self.ballWidth < self.dot1WidthFront + 40  
                        and self.dot1HeightFront-40 < self.ballHeight < self.dot1HeightFront):
                    self.team1TouchCount += 1
                    self.touchCount += 1
                    if self.team1TouchCount == 2:
                        Match.set(self)
                        self.ballVx = self.Vx/2
                        self.ballVy = 0
                    elif self.team1TouchCount == 3:
                        Match.spike(self)
                        self.ballVx *= 3
                        self.ballVy = self.ballSpeed*sin(radians(self.ballAngle*1.1))
                elif (self.dot1WidthBack < self.ballWidth < self.dot1WidthBack + 40  
                        and self.dot1HeightBack-40 < self.ballHeight < self.dot1HeightBack):
                    self.team1TouchCount += 1
                    self.touchCount += 1
                    if self.team1TouchCount == 2:
                        Match.set(self)
                        self.ballVx = self.Vx/2
                        self.ballVy = 2
                    elif self.team1TouchCount == 3:
                        Match.spike(self)
                        self.ballVx *= 1.5
                        self.ballVy = self.ballSpeed*sin(radians(self.ballAngle*.8))
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
                    and self.player1HeightTR-40 < self.ballHeight < self.player1HeightTR)): #If received in back
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
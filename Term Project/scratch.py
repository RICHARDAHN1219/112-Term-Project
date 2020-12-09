if self.touchCount > 0:
                if (self.ballY < self.ballHeight):
                    self.rallyStarts = False
                    if self.ballWidth < (self.width/2):
                        self.team2TouchCount = 0
                        if ((self.ballWidth <= self.bottomLineL) or 
                            ((self.ballHeight >= self.courtNetTop) or 
                            (self.ballHeight <= self.courtNetBottom))): #switch this to if ball lands outside the bounds with the height of ball trajectory being 0
                            if self.team1TouchCount == 0:
                                Match.score1 += 1
                                self.gameReset = True
                                self.servingSide = 0
                            else:
                                Match.score2 += 1
                                self.gameReset = True
                                self.servingSide = 1
                        elif ((self.courtNetBottom <= self.ballHeight <= self.courtNetTop) and 
                            (self.bottomLineL <=self.ballWidth <= self.width/2)):
                                #Here have the endpoint of curve be within the court
                                Match.score2 += 1
                                self.gameReset = True
                                self.servingSide = 1
                        elif self.team1TouchCount > 3:
                            Match.score2 += 1
                            self.gameReset = True
                            self.servingSide = 1
                    elif self.ballWidth > (self.width/2):
                        self.team1TouchCount = 0 
                        if ((self.ballWidth >= self.bottomLineR) or 
                            ((self.ballHeight >= self.courtNetTop) or 
                            (self.ballHeight <= self.courtNetBottom))): #switch this to if ball lands outside the bounds with the height of ball trajectory being 0
                                if self.team2TouchCount == 0:
                                    Match.score2 += 1
                                    self.gameReset = True
                                    self.servingSide = 1
                                else:
                                    Match.score1 += 1
                                    self.gameReset = True
                                    self.servingSide = 0
                        elif ((self.courtNetBottom <= self.ballHeight <= self.courtNetTop) and 
                            (self.width/2 <=self.ballWidth <= self.bottomLineR)):
                                #Here have the endpoint of curve be within the court
                                Match.score1 += 1
                                self.gameReset = True
                                self.servingSide = 0
                        elif self.team2TouchCount > 3:
                            Match.score1 += 1
                            self.gameReset = True
                            self.servingSide = 0








if MatchOptions.PlayerCount == 1:
                    self.ballWidth = self.dot2Width - self.ballRadius
                    self.ballVx = -self.ballVx
                elif MatchOptions.PlayerCount == 2:
                    if (self.dot2WidthFront < self.ballWidth < self.dot2WidthFront + 40  
                            and self.dot2HeightFront-40 < self.ballHeight < self.dot2HeightFront):
                        self.ballWidth = self.dot2WidthFront - self.ballRadius
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
                        self.ballWidth = self.dot2WidthBack - self.ballRadius
                        self.team2TouchCount += 1
                        self.touchCount += 1
                        if self.team2TouchCount == 1:
                            Match.receive(self)
                        if self.team2TouchCount == 2:
                            Match.toss(self)
                        elif self.team2TouchCount == 3:
                            Match.spike(self)

                            
elif MatchOptions.PlayerCount == 2:
                    if (self.dot1WidthFront < self.ballWidth < self.dot1WidthFront + 40  
                            and self.dot1HeightFront-40 < self.ballHeight < self.dot1HeightFront):
                        self.ballWidth = self.dot1WidthFront + 40 + self.ballRadius
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
                        self.ballWidth = self.dot1WidthBack + 40 + self.ballRadius
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
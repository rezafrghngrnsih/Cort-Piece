class Scores:
    def __init__(self):
        self.TeamAScores = []
        self.TeamBScores = []
        self.TeamARoundWins = 0
        self.TeamBRoundWins = 0
        self.TeamASetWins = 0
        self.TeamBSetWins = 0
        self.SetWinner = ''
        self.GameWinner = ''
        self.TrumpCallerName = ''
        self.TeamA = []
        self.TeamB = []

    def SetWinnerDeterminator(self):
        _TeamARoundScore = 0
        _TeamBRoundScore = 0
        TeamAScoresSum = sum(self.TeamAScores)
        TeamBScoresSum = sum(self.TeamBScores)
        TeamAIsTrumpCaller = False
        TeamBIsTrumpCaller = False
        for item in self.TeamA:
            if item.TrumpCaller == True:
                TeamAIsTrumpCaller == True
        for item in self.TeamB:
            if item.TrumpCaller == True:
                TeamBIsTrumpCaller == True

        if TeamAScoresSum > TeamBScoresSum:
            self.SetWinner = 'A'
            c = 0
            for i, score in enumerate(self.TeamAScores):
                _TeamARoundScore += score
                if i == 6 and _TeamARoundScore == 7 and TeamAIsTrumpCaller == True:
                    self.TeamASetWins += 2
                    c += 1
                elif i == 6 and _TeamARoundScore == 7 and TeamAIsTrumpCaller == False:
                    self.TeamASetWins += 3
                    c += 1

                elif c == 0:
                    self.TeamASetWins += 1

        else:
            self.SetWinner = 'B'
            d = 0
            for i, score in enumerate(self.TeamBScores):
                _TeamBRoundScore += score
                if i == 6 and _TeamBRoundScore == 7 and TeamBIsTrumpCaller == True:
                    self.TeamBSetWins += 2
                    d += 1
                elif i == 6 and _TeamBRoundScore == 7 and TeamBIsTrumpCaller == False:
                    self.TeamBSetWins += 3
                    d += 1
                elif d == 0:
                    self.TeamBSetWins += 1
        return self.SetWinner

    def GameWinnerDeterminator(self):
        if self.TeamASetWins >= 7:
            self.GameWinner = self.TeamA
            return self.GameWinner
        elif self.TeamBSetWins >= 7:
            self.GameWinner = self.TeamB
            return self.GameWinner

    def SetKotDetector(self):
        pass

    def GameKotDetector(self):
        pass

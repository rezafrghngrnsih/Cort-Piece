class Scores:
    def __init__(self):
        self.TeamAScores = []
        self.TeamBScores = []
        self.TeamARoundWins = 0
        self.TeamBRoundWins = 0
        self.TeamASetWins = 0
        self.TeamBSetWins = 0
        self.GameWinner = {}
        self.TrumpCallerName = ''
        self.TeamA = []
        self.TeamB = []

    def SetWinnerDeterminator(self):
        _TeamARoundScore = 0
        _TeamBRoundScore = 0
        TeamAScoresSum = sum(self.TeamAScores)
        TeamBScoresSum = sum(self.TeamBScores)

        if TeamAScoresSum > TeamBScoresSum:
            c = 0
            for i, score in enumerate(self.TeamAScores):
                _TeamARoundScore += score
                if i == 6 and _TeamARoundScore == 7 and self.TrumpCallerName in self.TeamA:
                    self.TeamASetWins += 2
                    c += 1
                    return self.TeamASetWins
                elif i == 6 and _TeamARoundScore == 7 and self.TrumpCallerName not in self.TeamA:
                    self.TeamASetWins += 3
                    c += 1
                    return self.TeamASetWins

                elif c == 0:
                    self.TeamASetWins += 1
                    return self.TeamASetWins
        else:
            d = 0
            for i, score in enumerate(self.TeamBScores):
                _TeamBRoundScore += score
                if i == 6 and _TeamBRoundScore == 7 and self.TrumpCallerName in self.TeamB:
                    self.TeamBSetWins += 2
                    d += 1
                    return self.TeamBSetWins
                elif i == 6 and _TeamBRoundScore == 7 and self.TrumpCallerName not in self.TeamB:
                    self.TeamBSetWins += 3
                    d += 1
                    return self.TeamBSetWins
                elif d == 0:
                    self.TeamBSetWins += 1
                    return self.TeamBSetWins

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

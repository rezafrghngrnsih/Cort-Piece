from Data import CLSGamer
from Data import CLSCards
#from Data import CLSScores
import os

INSCards = CLSCards.Cards()
#INSScores = CLSScores.Scores()

Gamer01 = CLSGamer.Gamer()
Gamer02 = CLSGamer.Gamer()
Gamer03 = CLSGamer.Gamer()
Gamer04 = CLSGamer.Gamer()
GamersInstances = [Gamer01, Gamer02, Gamer03, Gamer04]


class GameManager:
    def __init__(self):
        self.GamersNameAndOrder = {}
        self.SetGamersOrder = {}
        self.PlayGroundCards = {}
        self.TrumpCallerName = ''
        self.Trump = ''
        self.RoundNumber = 0
        self.SetNumber = 0

    def GamersNameAndOrderReciever(self):
        for i in range(1, 5):
            GamerName = input(f'Please enter Gamer 0{i} name :')
            self.GamersNameAndOrder[GamerName] = i

        os.system('cls')
        print(f'Gamers with their order are :\n\n{self.GamersNameAndOrder}')

    def GamerCaller(self):
        pass

    def TrumpCallerDeterminator(self):
        Status = True
        while Status:
            INSCards.PrimitiveDistributer()
            for k, v in INSCards.PlayGroundCards.items():
                if v == 14:
                    PlGrCrdsVals = list(INSCards.PlayGroundCards.values())
                    x = PlGrCrdsVals.index(14)
                    self.TrumpCallerName = list(
                        self.GamersNameAndOrder.keys())[x]
                    Status = False
                    print(f'Trump Caller is : {self.TrumpCallerName}')
                    TrumpCallerIndex = self.GamersNameAndOrder[self.TrumpCallerName]
                    GamersInstances[TrumpCallerIndex-1].TrumpCaller = True
                    INSCards.DeckKeysList = list(INSCards.DeckOfCards.keys())
                    break
            INSCards.PlayGroundCards = {}

        return self.TrumpCallerName

    def SetGamersOrderDeterminator(self):
        pass

    def PartnerDeterminator(self):
        pass

    def TurnCounter(self):
        pass

    def SetCounter(self):
        pass

    def RoundWinnerDeterminator(self):

        PlayGroundKeys = list(self.PlayGroundCards.keys())
        if PlayGroundKeys[0][0:-2] == self.Trump:
            PlayGroundTrumps = {}
            for k, v in self.PlayGroundCards.items():
                if k[0:-2] == self.Trump:
                    PlayGroundTrumps.update({k: v})
            BigTrump = max(PlayGroundTrumps, key=PlayGroundTrumps.get)
            RoundWinnerIndex = PlayGroundKeys.index(BigTrump)
            return RoundWinnerIndex

        elif PlayGroundKeys[0][0:-2] != self.Trump:
            PlayGroundTrumps = {}
            PlayGroundSuits = {}
            if self.Trump in PlayGroundKeys:
                for k, v in self.PlayGroundCards:
                    if k[0:-2] == self.Trump:
                        PlayGroundTrumps.update({k, v})
                BigTrump = max(PlayGroundTrumps, key=PlayGroundTrumps.get)
                RoundWinnerIndex = PlayGroundKeys.index(BigTrump)
                return RoundWinnerIndex
            else:
                for k, v in self.PlayGroundCards.items():
                    if k[0:-2] == PlayGroundKeys[0]:
                        PlayGroundSuits.update({k, v})
                BigSuit = max(PlayGroundSuits, key=PlayGroundSuits.get)
                RoundWinnerIndex = PlayGroundKeys.index(BigSuit)
                return RoundWinnerIndex

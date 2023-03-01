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
        self.PlayGroundCards = {}
        self.TrumpCallerName = ''
        self.Trump = {}
        self.TurnNumber = 0
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

        match self.SetGamersOrder[0].Index:
            case 1:
                for item in GamersInstances:
                    if item.Index == 2:
                        self.SetGamersOrder.append(item)
                for item in GamersInstances:
                    if item.Index == 3:
                        self.SetGamersOrder.append(item)
                for item in GamersInstances:
                    if item.Index == 4:
                        self.SetGamersOrder.append(item)
            case 2:
                for item in GamersInstances:
                    if item.Index == 3:
                        self.SetGamersOrder.append(item)
                for item in GamersInstances:
                    if item.Index == 4:
                        self.SetGamersOrder.append(item)
                for item in GamersInstances:
                    if item.Index == 1:
                        self.SetGamersOrder.append(item)
            case 3:
                for item in GamersInstances:
                    if item.Index == 4:
                        self.SetGamersOrder.append(item)
                for item in GamersInstances:
                    if item.Index == 1:
                        self.SetGamersOrder.append(item)
                for item in GamersInstances:
                    if item.Index == 2:
                        self.SetGamersOrder.append(item)
            case 4:
                for item in GamersInstances:
                    if item.Index == 1:
                        self.SetGamersOrder.append(item)
                for item in GamersInstances:
                    if item.Index == 2:
                        self.SetGamersOrder.append(item)
                for item in GamersInstances:
                    if item.Index == 3:
                        self.SetGamersOrder.append(item)

    def PartnerDeterminator(self):
        pass

    def TurnCounter(self):
        pass

    def SetCounter(self):
        pass

    def TurnWinnerDeterminator(self):
        pass

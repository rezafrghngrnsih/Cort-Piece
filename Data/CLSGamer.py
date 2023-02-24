# from Data import CLSGameManager
from Data import CLSCards
# from Data import CLSScores

#INSGameManager = CLSGameManager.GameManager()
INSCards = CLSCards.Cards()
#INSScores = CLSScores.Scores()


class Gamer:
    def __init__(self):
        self.Name = None
        self.Index = None
        self.Partnet = ''
        self.Hand = {}
        self.TrumpCaller = False
        self.RoundNumber = []

    def FirstCardReciever(self):
        for i in range(5):
            self.Hand.update(INSCards.SetDistributer())
        print(INSCards.Length())

    def SecondCardReciever(self):
        for i in range(4):
            self.Hand.update(INSCards.SetDistributer())
        print(INSCards.Length())

    def CardSender(self):
        pass

    def TrumpDeterminator(self):
        pass

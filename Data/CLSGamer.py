# from Data import CLSGameManager
# from Data import CLSCards
# from Data import CLSScores

#INSGameManager = CLSGameManager.GameManager()
#INSCards = CLSCards.Cards()
#INSScores = CLSScores.Scores()


class Gamer:
    def __init__(self):
        self.Name = None
        self.Index = None
        self.Partnet = ''
        self.Hand = {}
        self.TrumpCaller = False
        self.RoundNumber = []

    def CardReciever(self):
        pass

    def CardSender(self):
        pass

    def TrumpDeterminator(self):
        pass

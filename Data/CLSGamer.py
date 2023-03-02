# from Data import CLSGameManager
from Data import CLSCards
from Data import CLSGamer
# from Data import CLSScores

#INSGameManager = CLSGameManager.GameManager()
INSCards = CLSCards.Cards()
#INSScores = CLSScores.Scores()


class Gamer:
    def __init__(self):
        self.Name = None
        self.Index = None
        self.Partner = ''
        self.Trump = ''
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

        HandTrumpCards = {}
        LowHand = {}

        for k, v in self.Hand.items():
            if (self.Trump not in k) and v != 14:
                LowHand[k] = v

        for k, v in self.Hand.items():
            if k[0:-2] == self.Trump:
                HandTrumpCards.update({k: v})
        print(f'\n{HandTrumpCards}')

        if (len(HandTrumpCards) >= 5) and (self.Trump+'14' in HandTrumpCards) and (self.Trump+'13' in HandTrumpCards):
            BigTrump = max(HandTrumpCards, key=HandTrumpCards.get)
            return {BigTrump: HandTrumpCards[BigTrump]}

        elif len(HandTrumpCards) >= 4:
            SmallTrump = min(HandTrumpCards, key=HandTrumpCards.get)
            return {SmallTrump: HandTrumpCards[SmallTrump]}

        elif len(HandTrumpCards) < 4:
            for k, v in self.Hand.items():
                if (self.Trump not in k) and v == 14:
                    return {k: v}
        else:
            SmallSuit = min(LowHand, key=LowHand.get)
            return {SmallSuit: LowHand[SmallSuit]}

    def TrumpDeterminator(self):
        HandCardsName = []
        HandCardsValues = []
        SpadeCards = []
        ClubCards = []
        DiamondCards = []
        HeartCards = []

        HandCardsName = list(self.Hand.keys())
        HandCardsValues = list(self.Hand.values())
        for card in HandCardsName:
            CardGroup = card[0:-2]
            print(CardGroup)
            match CardGroup:
                case 'Spade':
                    SpadeCards.append(self.Hand[card])
                case 'Club':
                    ClubCards.append(self.Hand[card])
                case 'Diamond':
                    DiamondCards.append(self.Hand[card])
                case 'Heart':
                    HeartCards.append(self.Hand[card])
        print(f'Spade cards vals : {SpadeCards}')
        print(f'Club cards vals : {ClubCards}')
        print(f'Diamond cards vals : {DiamondCards}')
        print(f'Heart cards vals : {HeartCards}')

        SpadeAve = (sum(SpadeCards))  # /len(SpadeCards)
        ClubAve = (sum(ClubCards))  # /len(ClubCards)
        DiamondAve = (sum(DiamondCards))  # /len(DiamondCards)
        HeartAve = (sum(HeartCards))  # /len(HeartCards)

        SuitsAveList = [SpadeAve, ClubAve, DiamondAve, HeartAve]

        MaxAve = max(SuitsAveList)
        MaxAveIndex = SuitsAveList.index(MaxAve)

        match MaxAveIndex:
            case 0:
                return 'Spade'
            case 1:
                return 'Club'
            case 2:
                return 'Diamond'
            case 3:
                return 'Heart'

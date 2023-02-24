from Data import CLSGameManager
from Data import CLSGamer
#from Data import CLSScores
import random


#INSScores = CLSScores.Scores()

Gamer01 = CLSGamer.Gamer()
Gamer02 = CLSGamer.Gamer()
Gamer03 = CLSGamer.Gamer()
Gamer04 = CLSGamer.Gamer()
GamersInstances = [Gamer01, Gamer02, Gamer03, Gamer04]


class Cards:
    def __init__(self):
        self.Spade = {'Spade02': 2, 'Spade03': 3, 'Spade04': 4, 'Spade05': 5, 'Spade06': 6, 'Spade07': 7,
                      'Spade08': 8, 'Spade09': 9, 'Spade10': 10, 'Spade11': 11, 'Spade12': 12, 'Spade13': 13, 'Spade14': 14}
        self.Club = {'Club02': 2, 'Club03': 3, 'Club04': 4, 'Club05': 5, 'Club06': 6, 'Club07': 7,
                     'Club08': 8, 'Club09': 9, 'Club10': 10, 'Club11': 11, 'Club12': 12, 'Club13': 13, 'Club14': 14}
        self.Diamond = {'Diamond02': 2, 'Diamond03': 3, 'Diamond04': 4, 'Diamond05': 5, 'Diamond06': 6, 'Diamond07': 7,
                        'Diamond08': 8, 'Diamond09': 9, 'Diamond10': 10, 'Diamond11': 11, 'Diamond12': 12, 'Diamond13': 13, 'Diamond14': 14}
        self.Heart = {'Heart02': 2, 'Heart03': 3, 'Heart04': 4, 'Heart05': 5, 'Heart06': 6, 'Heart07': 7,
                      'Heart08': 8, 'Heart09': 9, 'Heart10': 10, 'Heart11': 11, 'Heart12': 12, 'Heart13': 13, 'Heart14': 14}
        self.DeckOfCards = {'Spade02': 2, 'Spade03': 3, 'Spade04': 4, 'Spade05': 5, 'Spade06': 6, 'Spade07': 7,
                            'Spade08': 8, 'Spade09': 9, 'Spade10': 10, 'Spade11': 11, 'Spade12': 12, 'Spade13': 13, 'Spade14': 14, 'Club02': 2, 'Club03': 3, 'Club04': 4, 'Club05': 5, 'Club06': 6, 'Club07': 7,
                            'Club08': 8, 'Club09': 9, 'Club10': 10, 'Club11': 11, 'Club12': 12, 'Club13': 13, 'Club14': 14,
                            'Diamond02': 2, 'Diamond03': 3, 'Diamond04': 4, 'Diamond05': 5, 'Diamond06': 6, 'Diamond07': 7,
                            'Diamond08': 8, 'Diamond09': 9, 'Diamond10': 10, 'Diamond11': 11, 'Diamond12': 12, 'Diamond13': 13, 'Diamond14': 14,
                            'Heart02': 2, 'Heart03': 3, 'Heart04': 4, 'Heart05': 5, 'Heart06': 6, 'Heart07': 7,
                            'Heart08': 8, 'Heart09': 9, 'Heart10': 10, 'Heart11': 11, 'Heart12': 12, 'Heart13': 13, 'Heart14': 14}
        self.DeckKeysList = list(self.DeckOfCards.keys())
        self.PlayGroundCards = {}
        self.SetGamersOrder = []

    def PrimitiveDistributer(self):
        for i in range(1, 5):
            RandedCard = random.choices(self.DeckKeysList)[0]
            self.DeckKeysList.remove(RandedCard)
            self.PlayGroundCards[RandedCard] = self.DeckOfCards[RandedCard]
        print(self.PlayGroundCards)

    def SetGamersOrderDeterminator(self):
        INSGameManager = CLSGameManager.GameManager()
        GamersNameAndOrder = INSGameManager.GamersNameAndOrderReciever()
        Gamer01.Name = list(GamersNameAndOrder.keys())[0]
        Gamer01.Index = list(GamersNameAndOrder.values())[0]
        Gamer02.Name = list(GamersNameAndOrder.keys())[1]
        Gamer02.Index = list(GamersNameAndOrder.values())[1]
        Gamer03.Name = list(GamersNameAndOrder.keys())[2]
        Gamer03.Index = list(GamersNameAndOrder.values())[2]
        Gamer04.Name = list(GamersNameAndOrder.keys())[3]
        Gamer04.Index = list(GamersNameAndOrder.values())[3]

        print(f'{Gamer01.Name}    {Gamer01.Index}')
        print(f'{Gamer02.Name}    {Gamer02.Index}')
        print(f'{Gamer03.Name}    {Gamer03.Index}')
        print(f'{Gamer04.Name}    {Gamer04.Index}')

        for item in GamersInstances:
            if item.TrumpCaller == True:
                self.SetGamersOrder.append(item)
        print(f'andise hakem is : {self.SetGamersOrder[0].Index}')

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

    def FirstSetDistributer(self):
        for item in self.SetGamersOrder:
            for i in range(5):
                RandedCard = random.choices(self.DeckKeysList)[0]
                self.DeckKeysList.remove(RandedCard)
                item.Hand[RandedCard] = self.DeckOfCards[RandedCard]

    def SecondSetDistributer(self):
        for item in self.SetGamersOrder:
            for i in range(4):
                RandedCard = random.choices(self.DeckKeysList)[0]
                self.DeckKeysList.remove(RandedCard)
                item.Hand[RandedCard] = self.DeckOfCards[RandedCard]

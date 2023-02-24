from Data import CLSGameManager
from Data import CLSGamer
from Data import CLSCards
from Data import CLSScores

INSGameManager = CLSGameManager.GameManager()
INSCards = CLSCards.Cards()
INSScores = CLSScores.Scores()
SetGamersOrder = []
Gamer01 = CLSGamer.Gamer()
Gamer02 = CLSGamer.Gamer()
Gamer03 = CLSGamer.Gamer()
Gamer04 = CLSGamer.Gamer()
GamersInstances = [Gamer01, Gamer02, Gamer03, Gamer04]

INSGameManager.GamersNameAndOrderReciever()
INSGameManager.TrumpCallerDeterminator()

Gamer01.Name = list(INSGameManager.GamersNameAndOrder.keys())[0]
Gamer01.Index = list(INSGameManager.GamersNameAndOrder.values())[0]
Gamer02.Name = list(INSGameManager.GamersNameAndOrder.keys())[1]
Gamer02.Index = list(INSGameManager.GamersNameAndOrder.values())[1]
Gamer03.Name = list(INSGameManager.GamersNameAndOrder.keys())[2]
Gamer03.Index = list(INSGameManager.GamersNameAndOrder.values())[2]
Gamer04.Name = list(INSGameManager.GamersNameAndOrder.keys())[3]
Gamer04.Index = list(INSGameManager.GamersNameAndOrder.values())[3]

print(f'{Gamer01.Name}    {Gamer01.Index}')
print(f'{Gamer02.Name}    {Gamer02.Index}')
print(f'{Gamer03.Name}    {Gamer03.Index}')
print(f'{Gamer04.Name}    {Gamer04.Index}')

for item in GamersInstances:
    if item.TrumpCaller == True:
        SetGamersOrder.append(item)
        print(f'andise hakem is : {item.Index}')


INSCards.FirstSetDistributer()
Gamer01.FirstCardReciever()
Gamer02.FirstCardReciever()
Gamer03.FirstCardReciever()
Gamer04.FirstCardReciever()
Gamer01.SecondCardReciever()
Gamer02.SecondCardReciever()
Gamer03.SecondCardReciever()
Gamer04.SecondCardReciever()

print(Gamer01.Hand)
print(Gamer02.Hand)
print(Gamer03.Hand)
print(Gamer04.Hand)

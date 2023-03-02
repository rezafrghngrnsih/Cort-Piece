from Data import CLSGameManager
from Data import CLSGamer
from Data import CLSCards
from Data import CLSScores

INSGameManager = CLSGameManager.GameManager()
INSCards = CLSCards.Cards()
INSScores = CLSScores.Scores()
SetGamersOrder = []
INSGamer01 = CLSGamer.Gamer()
INSGamer02 = CLSGamer.Gamer()
INSGamer03 = CLSGamer.Gamer()
INSGamer04 = CLSGamer.Gamer()
GamersInstances = [INSGamer01, INSGamer02, INSGamer03, INSGamer04]


INSGameManager.GamersNameAndOrderReciever()

for item in GamersInstances:
    item.Name = list(INSGameManager.GamersNameAndOrder.keys())[
        GamersInstances.index(item)]
    item.Index = list(INSGameManager.GamersNameAndOrder.values())[
        GamersInstances.index(item)]

TrumpCallerName = INSGameManager.TrumpCallerDeterminator()
INSScores.TrumpCallerName = TrumpCallerName

for item in GamersInstances:
    if item.Name == TrumpCallerName:
        item.TrumpCaller = True

print(f'{INSGamer01.Name}    {INSGamer01.Index}')
print(f'{INSGamer02.Name}    {INSGamer02.Index}')
print(f'{INSGamer03.Name}    {INSGamer03.Index}')
print(f'{INSGamer04.Name}    {INSGamer04.Index}')

for item in GamersInstances:
    if item.TrumpCaller == True:
        SetGamersOrder.append(item)
        print(f'Trump Caller index is : {item.Index}')


INSCards.SetDistributer()

for item in GamersInstances:
    item.FirstCardReciever()

print(f'{INSGamer01.Name} hand : {INSGamer01.Hand}')
print(f'{INSGamer02.Name} hand : {INSGamer02.Hand}')
print(f'{INSGamer03.Name} hand : {INSGamer03.Hand}')
print(f'{INSGamer04.Name} hand : {INSGamer04.Hand}')


for item in GamersInstances:
    if item.TrumpCaller == True:
        INSGameManager.Trump = item.TrumpDeterminator()
    item.Trump = INSGameManager.Trump

print(f'Trump is : {INSGameManager.Trump}')

for i in range(2):
    INSGamer01.SecondCardReciever()
    INSGamer02.SecondCardReciever()
    INSGamer03.SecondCardReciever()
    INSGamer04.SecondCardReciever()

print(f'{INSGamer01.Name} hand : {INSGamer01.Hand}')
print(f'{INSGamer02.Name} hand : {INSGamer02.Hand}')
print(f'{INSGamer03.Name} hand : {INSGamer03.Hand}')
print(f'{INSGamer04.Name} hand : {INSGamer04.Hand}')

for item in GamersInstances:
    if item.TrumpCaller == True:
        print(item.CardSender())

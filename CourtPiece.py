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


def SetGamersOrderDeterminatopr(FirstPlayer):
    match FirstPlayer:
        case 1:
            for item in GamersInstances:
                if item.Index == 2:
                    SetGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 3:
                    SetGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 4:
                    SetGamersOrder.append(item)
        case 2:
            for item in GamersInstances:
                if item.Index == 3:
                    SetGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 4:
                    SetGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 1:
                    SetGamersOrder.append(item)
        case 3:
            for item in GamersInstances:
                if item.Index == 4:
                    SetGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 1:
                    SetGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 2:
                    SetGamersOrder.append(item)
        case 4:
            for item in GamersInstances:
                if item.Index == 1:
                    SetGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 2:
                    SetGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 3:
                    SetGamersOrder.append(item)


INSGameManager.GamersNameAndOrderReciever()

for item in GamersInstances:
    item.Name = list(INSGameManager.GamersNameAndOrder.keys())[
        GamersInstances.index(item)]
    item.Index = list(INSGameManager.GamersNameAndOrder.values())[
        GamersInstances.index(item)]

TeamA = [INSGamer01, INSGamer03]
TeamB = [INSGamer02, INSGamer04]
INSScores.TeamA = TeamA
INSScores.TeamB = TeamB
INSGamer01.Team = INSGamer03.Team = 'A'
INSGamer02.Team = INSGamer04.Team = 'B'
INSGamer01.Partner = INSGamer03.Name
INSGamer02.Partner = INSGamer04.Name
INSGamer03.Partner = INSGamer01.Name
INSGamer04.Partner = INSGamer02.Name


TrumpCallerName = INSGameManager.TrumpCallerDeterminator()
INSScores.TrumpCallerName = TrumpCallerName

for item in GamersInstances:
    if item.Name == TrumpCallerName:
        item.TrumpCaller = True

print(f'{INSGamer01.Name}    {INSGamer01.Index}')
print(f'{INSGamer02.Name}    {INSGamer02.Index}')
print(f'{INSGamer03.Name}    {INSGamer03.Index}')
print(f'{INSGamer04.Name}    {INSGamer04.Index}')

TrumpCallerIndex = 0
for item in GamersInstances:
    if item.TrumpCaller == True:
        SetGamersOrder.append(item)
        print(f'Trump Caller index is : {item.Index}')
        TrumpCallerIndex = item.Index

SetGamersOrderDeterminatopr(TrumpCallerIndex)


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


for i in range(13):
    for item in SetGamersOrder:
        PlayedCard = item.CardSender()
        print(f'Played Card is : {PlayedCard}')
        for ins in GamersInstances:
            ins.PlayGroundCards.update(PlayedCard)
        INSGameManager.PlayGroundCards.update(PlayedCard)
        INSCards.PlayGroundCards.update(PlayedCard)
        print(f'Play Ground Cards : {INSCards.PlayGroundCards}')

    SetGamersOrder = []

    RoundWinnerIndex = INSGameManager.RoundWinnerDeterminator()
    RoundWinner = SetGamersOrder[RoundWinnerIndex]
    print(f'Round Winner is : {RoundWinner.Name}')

    SetGamersOrderDeterminatopr(RoundWinner.Index)
    print(f'Set Gamers Order : {SetGamersOrder}')

    match RoundWinner.Team:
        case 'A':
            INSScores.TeamARoundWins += 1
            INSScores.TeamAScores.append(1)
            INSScores.TeamBScores.append(0)
        case 'B':
            INSScores.TeamBRoundWins += 1
            INSScores.TeamAScores.append(0)
            INSScores.TeamBScores.append(1)
    if (INSScores.TeamARoundWins == 7) or (INSScores.TeamBRoundWins == 7):
        break

from Data import CLSGameManager
from Data import CLSGamer
from Data import CLSCards
from Data import CLSScores

INSGameManager = CLSGameManager.GameManager()
INSCards = CLSCards.Cards()
INSScores = CLSScores.Scores()
RoundGamersOrder = []
INSGamer01 = CLSGamer.Gamer()
INSGamer02 = CLSGamer.Gamer()
INSGamer03 = CLSGamer.Gamer()
INSGamer04 = CLSGamer.Gamer()
GamersInstances = [INSGamer01, INSGamer02, INSGamer03, INSGamer04]


def RoundGamersOrderDeterminator(FirstGamerIndex):
    for item in GamersInstances:
        if item.Index == FirstGamerIndex:
            RoundGamersOrder.append(item)
    match FirstGamerIndex:
        case 1:
            for item in GamersInstances:
                if item.Index == 2:
                    RoundGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 3:
                    RoundGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 4:
                    RoundGamersOrder.append(item)
        case 2:
            for item in GamersInstances:
                if item.Index == 3:
                    RoundGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 4:
                    RoundGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 1:
                    RoundGamersOrder.append(item)
        case 3:
            for item in GamersInstances:
                if item.Index == 4:
                    RoundGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 1:
                    RoundGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 2:
                    RoundGamersOrder.append(item)
        case 4:
            for item in GamersInstances:
                if item.Index == 1:
                    RoundGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 2:
                    RoundGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 3:
                    RoundGamersOrder.append(item)


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
INSGamer01.Partner = INSGamer03
INSGamer02.Partner = INSGamer04
INSGamer03.Partner = INSGamer01
INSGamer04.Partner = INSGamer02


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
        print(f'Trump Caller index is : {item.Index}')
        TrumpCallerIndex = item.Index

RoundGamersOrderDeterminator(TrumpCallerIndex)


INSCards.SetDistributer()

for item in GamersInstances:
    item.FirstCardReciever()

for item in GamersInstances:
    item.Hand = dict(sorted(item.Hand.items(), key=lambda x: x[0]))

print(
    f'\n\n{GamersInstances[0].Name}            {GamersInstances[1].Name}            {GamersInstances[2].Name}            {GamersInstances[3].Name}')
for k in range(5):
    print(f'{list(GamersInstances[0].Hand.keys())[k]}    {list(GamersInstances[1].Hand.keys())[k]}    {list(GamersInstances[2].Hand.keys())[k]}    {list(GamersInstances[3].Hand.keys())[k]}')

Trump = ''
for item in GamersInstances:
    if item.TrumpCaller == True:
        Trump = item.TrumpDeterminator()
for item in GamersInstances:
    item.Trump = Trump
INSGameManager.Trump = Trump

print(f'\n\nTrump is : {INSGameManager.Trump}')

for k in range(2):
    INSGamer01.SecondCardReciever()
    INSGamer02.SecondCardReciever()
    INSGamer03.SecondCardReciever()
    INSGamer04.SecondCardReciever()


print(
    f'\n\n{GamersInstances[0].Name}            {GamersInstances[1].Name}            {GamersInstances[2].Name}            {GamersInstances[3].Name}')
for k in range(13):
    print(f'{list(GamersInstances[0].Hand.keys())[k]}    {list(GamersInstances[1].Hand.keys())[k]}    {list(GamersInstances[2].Hand.keys())[k]}    {list(GamersInstances[3].Hand.keys())[k]}')


for item in GamersInstances:
    item.Hand = dict(sorted(item.Hand.items(), key=lambda x: x[0]))


print('\n\nRound gamers order :')
for item in RoundGamersOrder:
    print(f'{item.Name}')


for j in range(13):
    print('.................................................\n.................................................')
    print(f'\nSet number is : {j+1}\n')
    for i in range(13):
        print(f'\nSet number is : {j+1}\n')
        print(f'\nRound number is : {i+1}\n')
        print(
            f'\n\n{GamersInstances[0].Name}            {GamersInstances[1].Name}            {GamersInstances[2].Name}            {GamersInstances[3].Name}')
        for k in range(len(GamersInstances[0].Hand)):
            print(
                f'{list(GamersInstances[0].Hand.keys())[k]}    {list(GamersInstances[1].Hand.keys())[k]}    {list(GamersInstances[2].Hand.keys())[k]}    {list(GamersInstances[3].Hand.keys())[k]}')

        for item in RoundGamersOrder:
            PlayedCard = item.CardSender()
            print(f'\n{item.Name} played : {PlayedCard}\n')
            for ins in GamersInstances:
                ins.PlayGroundCards.update(PlayedCard)
            INSGameManager.PlayGroundCards.update(PlayedCard)
            INSCards.PlayGroundCards.update(PlayedCard)
            print(f'Play Ground Cards : {INSCards.PlayGroundCards}')

        print(
            f'\nTrump is : {INSGameManager.Trump}\nGround Suit is : {list(INSGameManager.PlayGroundCards.keys())[0]} : {list(INSGameManager.PlayGroundCards.values())[0]}\n')
        RoundWinnerIndex = INSGameManager.RoundWinnerDeterminator()
        RoundWinner = RoundGamersOrder[RoundWinnerIndex]
        print(f'\nRound Winner is : {RoundWinner.Name}\n')

        for item in GamersInstances:
            item.PlayGroundCards = {}

        INSCards.PlayGroundCards = INSGameManager.PlayGroundCards = {}
        RoundGamersOrder = []

        RoundGamersOrderDeterminator(RoundWinner.Index)
        print('Round gamers order :')
        for item in RoundGamersOrder:
            print(f'{item.Name}')

        match RoundWinner.Team:
            case 'A':
                INSScores.TeamARoundWins += 1
                INSScores.TeamAScores.append(1)
                INSScores.TeamBScores.append(0)
                print(f'\nTeam A round scores : {INSScores.TeamAScores}\n')
                print(f'\nTeam B round scores : {INSScores.TeamBScores}\n')

            case 'B':
                INSScores.TeamBRoundWins += 1
                INSScores.TeamAScores.append(0)
                INSScores.TeamBScores.append(1)
                print(f'\nTeam B round scores : {INSScores.TeamBScores}\n')
                print(f'\nTeam A round scores : {INSScores.TeamAScores}\n')

        print('.................................................')
        if (INSScores.TeamARoundWins == 7) or (INSScores.TeamBRoundWins == 7):
            break
    SetWinner = INSScores.SetWinnerDeterminator()
    print(f'Set {j+1} winner is : Team {INSScores.SetWinner}')
    print(f'\nTeam A set wins : {INSScores.TeamASetWins}')
    print(f'\nTeam B set wins : {INSScores.TeamBSetWins}')
    print('.................................................\n.................................................')

    RoundGamersOrder = []

    match SetWinner:
        case 'A':
            x = 0
            for item in TeamA:
                if item.TrumpCaller == True:
                    x += 1
            if x > 0:
                for item in TeamA:
                    if item.TrumpCaller == False:
                        RoundGamersOrderDeterminator(item.Index)
            else:
                for item in GamersInstances:
                    if item.TrumpCaller == True:
                        match item.Index:
                            case 1:
                                for item in GamersInstances:
                                    if item.Index == 2:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 3:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 4:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 1:
                                        RoundGamersOrder.append(item)

                            case 2:
                                for item in GamersInstances:
                                    if item.Index == 3:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 4:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 1:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 2:
                                        RoundGamersOrder.append(item)
                            case 3:
                                for item in GamersInstances:
                                    if item.Index == 4:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 1:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 2:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 3:
                                        RoundGamersOrder.append(item)
                            case 4:
                                for item in GamersInstances:
                                    if item.Index == 1:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 2:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 3:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 4:
                                        RoundGamersOrder.append(item)
        case 'B':
            y = 0
            for item in TeamB:
                if item.TrumpCaller == True:
                    y += 1
            if y > 0:
                for item in TeamB:
                    if item.TrumpCaller == False:
                        RoundGamersOrderDeterminator(item.Index)
            else:
                for item in GamersInstances:
                    if item.TrumpCaller == True:
                        match item.Index:
                            case 1:
                                for item in GamersInstances:
                                    if item.Index == 2:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 3:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 4:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 1:
                                        RoundGamersOrder.append(item)

                            case 2:
                                for item in GamersInstances:
                                    if item.Index == 3:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 4:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 1:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 2:
                                        RoundGamersOrder.append(item)
                            case 3:
                                for item in GamersInstances:
                                    if item.Index == 4:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 1:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 2:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 3:
                                        RoundGamersOrder.append(item)
                            case 4:
                                for item in GamersInstances:
                                    if item.Index == 1:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 2:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 3:
                                        RoundGamersOrder.append(item)
                                for item in GamersInstances:
                                    if item.Index == 4:
                                        RoundGamersOrder.append(item)

    for item in GamersInstances:
        item.Hand = {}
    RoundGamersOrder[0].TrumpCaller = True

    INSCards.SetDistributer()

    for item in GamersInstances:
        item.FirstCardReciever()

    for item in GamersInstances:
        item.Hand = dict(sorted(item.Hand.items(), key=lambda x: x[0]))
    print(
        f'\n\n{GamersInstances[0].Name}            {GamersInstances[1].Name}            {GamersInstances[2].Name}            {GamersInstances[3].Name}')
    for k in range(5):
        print(f'{list(GamersInstances[0].Hand.keys())[k]}    {list(GamersInstances[1].Hand.keys())[k]}    {list(GamersInstances[2].Hand.keys())[k]}    {list(GamersInstances[3].Hand.keys())[k]}')

    TrumpSuit = ''
    for item in GamersInstances:
        if item.TrumpCaller == True:
            TrumpSuit = item.TrumpDeterminator()
    for item in GamersInstances:
        item.Trump = TrumpSuit
    INSGameManager.Trump = TrumpSuit

    print(f'\n\nTrump is : {INSGameManager.Trump}')

    for k in range(2):
        INSGamer01.SecondCardReciever()
        INSGamer02.SecondCardReciever()
        INSGamer03.SecondCardReciever()
        INSGamer04.SecondCardReciever()

    print(
        f'\n\n{GamersInstances[0].Name}            {GamersInstances[1].Name}            {GamersInstances[2].Name}            {GamersInstances[3].Name}')
    for k in range(13):
        print(f'{list(GamersInstances[0].Hand.keys())[k]}    {list(GamersInstances[1].Hand.keys())[k]}    {list(GamersInstances[2].Hand.keys())[k]}    {list(GamersInstances[3].Hand.keys())[k]}')
    for item in GamersInstances:
        item.Hand = dict(sorted(item.Hand.items(), key=lambda x: x[0]))

    print('\n\nRound gamers order :')
    for item in RoundGamersOrder:
        print(f'{item.Name}')

INSScores.GameWinnerDeterminator()

print(f'\nGame Winner Team is : {INSScores.GameWinner}')

from Data import CLSGameManager
from Data import CLSGamer
from Data import CLSCards
from Data import CLSScores

INSGameManager = CLSGameManager.GameManager()
INSCards = CLSCards.Cards()
INSScores = CLSScores.Scores()

Gamer01 = CLSGamer.Gamer()
Gamer02 = CLSGamer.Gamer()
Gamer03 = CLSGamer.Gamer()
Gamer04 = CLSGamer.Gamer()
GamersInstances = [Gamer01, Gamer02, Gamer03, Gamer04]

INSGameManager.GamersNameAndOrderReciever()
INSGameManager.TrumpCallerDeterminator()
INSCards.SetGamersOrderDeterminator()
INSCards.FirstSetDistributer()
print(Gamer01.Hand)
print(Gamer02.Hand)
print(Gamer03.Hand)
print(Gamer04.Hand)

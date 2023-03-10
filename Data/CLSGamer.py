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
        self.Team = ''
        self.Partner = ''
        self.Trump = ''
        self.Hand = {}
        self.TrumpCaller = False
        self.RoundNumber = []
        self.PlayGroundCards = {}

    def FirstCardReciever(self):
        for i in range(5):
            self.Hand.update(INSCards.SetDistributer())
        print(INSCards.Length())

    def SecondCardReciever(self):
        for i in range(4):
            self.Hand.update(INSCards.SetDistributer())
        print(INSCards.Length())

    def CardSender(self):
        __temp_list = {}
        __temp_list_Trumps = {}
        HandTrumpCards = {}
        LowHand = {}

        match len(self.PlayGroundCards):
            case 0:

                for k, v in self.Hand.items():
                    if (self.Trump not in k) and v != 14:
                        LowHand[k] = v

                for k, v in self.Hand.items():
                    if k[0:-2] == self.Trump:
                        HandTrumpCards.update({k: v})
                print(f'\n{HandTrumpCards}')

                if (len(HandTrumpCards) >= 5) and (self.Trump+'14' in HandTrumpCards) and (self.Trump+'13' in HandTrumpCards):
                    BigTrump = max(HandTrumpCards, key=HandTrumpCards.get)
                    self.Hand.pop(BigTrump)
                    return {BigTrump: HandTrumpCards[BigTrump]}

                elif len(HandTrumpCards) >= 4:
                    SmallTrump = min(HandTrumpCards, key=HandTrumpCards.get)
                    self.Hand.pop(SmallTrump)
                    return {SmallTrump: HandTrumpCards[SmallTrump]}

                else:
                    for k, v in self.Hand.items():
                        if (self.Trump not in k) and v == 14:
                            self.Hand.pop(k)
                            return {k: v}
                        else:
                            SmallSuit = min(LowHand, key=LowHand.get)
                            self.Hand.pop(SmallSuit)
                            return {SmallSuit: LowHand[SmallSuit]}
            case 1:
                for inst_card in self.PlayGroundCards:
                    suit = inst_card[0:-2]
                    if suit == self.Trump:
                        for card in self.Hand:
                            if self.Trump in card:
                                __temp_list_Trumps.update(
                                    {card: self.Hand[card]})
                        if len(__temp_list_Trumps) > 0:
                            for card in __temp_list_Trumps:
                                if __temp_list_Trumps[card] > self.PlayGroundCards[inst_card]:
                                    card_to_send = {card: self.Hand[card]}
                                    self.Hand.pop(card)
                                    return card_to_send
                            card = min(__temp_list_Trumps,
                                       key=__temp_list_Trumps.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                    else:
                        for card in self.Hand:
                            if suit in card:
                                if self.Hand[card] == 14:
                                    card_to_send = {card: self.Hand[card]}
                                    self.Hand.pop(card)
                                    return card_to_send
                                else:
                                    __temp_list.update({card: self.Hand[card]})
                        if len(__temp_list) > 0:
                            for card in __temp_list:
                                if __temp_list[card] > self.PlayGroundCards[inst_card]:
                                    card_to_send = {card: self.Hand[card]}
                                    self.Hand.pop(card)
                                    return card_to_send
                            card = min(__temp_list, key=__temp_list.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        else:
                            __suit_other1 = 0
                            __suit_other1_value = 0
                            __temp_list_other1 = {}
                            __suit_other2 = 0
                            __suit_other2_value = 0
                            __temp_list_other2 = {}
                            __weight_other1 = 0
                            __weight_other2 = 0
                            __suits_in_Hand = [x for x in [
                                'Spade', 'Club', 'Diamond', 'Heart'] if x not in [suit, self.Trump]]
                            for card in self.Hand:
                                if card[0:-2] == __suits_in_Hand[0]:
                                    __suit_other1 += 1
                                    __suit_other1_value += self.Hand[card]
                                    __weight_other1 = __suit_other1_value/__suit_other1
                                    __temp_list_other1.update(
                                        {card: self.Hand[card]})
                                else:
                                    __suit_other2 += 1
                                    __suit_other2_value += self.Hand[card]
                                    __weight_other2 = __suit_other2_value/__suit_other2
                                    __temp_list_other2.update(
                                        {card: self.Hand[card]})
                            if __weight_other1 >= __weight_other2:
                                card = min(__temp_list_other1,
                                           key=__temp_list_other1.get)
                                card_to_send = {card: self.Hand[card]}
                                self.Hand.pop(card)
                                return card_to_send
                            else:
                                card = min(__temp_list_other2,
                                           key=__temp_list_other2.get)
                                card_to_send = {card: self.Hand[card]}
                                self.Hand.pop(card)
                                return card_to_send
            case 2:
                inst_cards = list(self.PlayGroundCards)
                suit1 = inst_cards[0][0:-2]
                suit2 = inst_cards[1][0:-2]
                if suit1 == self.Trump and suit2 == self.Trump:
                    for card in self.Hand:
                        if self.Trump in card:
                            __temp_list_Trumps.update({card: self.Hand[card]})
                    if len(__temp_list_Trumps) > 0:
                        if self.PlayGroundCards[inst_cards[0]] > self.PlayGroundCards[inst_cards[1]]:
                            card = min(__temp_list_Trumps,
                                       key=__temp_list_Trumps.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        else:
                            for card in __temp_list_Trumps:
                                if __temp_list_Trumps[card] > self.PlayGroundCards[inst_cards[1]]:
                                    card_to_send = {card: self.Hand[card]}
                                    self.Hand.pop(card)
                                    return card_to_send
                            card = min(__temp_list_Trumps,
                                       key=__temp_list_Trumps.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                    else:
                        __suit_other1 = 0
                        __suit_other1_value = 0
                        __temp_list_other1 = {}
                        __suit_other2 = 0
                        __suit_other2_value = 0
                        __temp_list_other2 = {}
                        __suit_other3 = 0
                        __suit_other3_value = 0
                        __temp_list_other3 = {}
                        __suits_in_Hand = [x for x in [
                            'Spade', 'Club', 'Diamond', 'Heart'] if x != self.Trump]
                        for card in self.Hand:
                            if card[0:-2] == __suits_in_Hand[0]:
                                __suit_other1 += 1
                                __suit_other1_value += self.Hand[card]
                                __weight_other1 = __suit_other1_value/__suit_other1
                                __temp_list_other1.update(
                                    {card: self.Hand[card]})
                            elif card[0:-2] == __suits_in_Hand[1]:
                                __suit_other2 += 1
                                __suit_other2_value += self.Hand[card]
                                __weight_other2 = __suit_other2_value/__suit_other2
                                __temp_list_other2.update(
                                    {card: self.Hand[card]})
                            else:
                                __suit_other3 += 1
                                __suit_other3_value += self.Hand[card]
                                __weight_other3 = __suit_other3_value/__suit_other3
                                __temp_list_other3.update(
                                    {card: self.Hand[card]})
                        if __weight_other1 >= __weight_other2:
                            card = min(__temp_list_other1,
                                       key=__temp_list_other1.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        elif __weight_other2 >= __weight_other3:
                            card = min(__temp_list_other2,
                                       key=__temp_list_other2.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        else:
                            card = min(__temp_list_other3,
                                       key=__temp_list_other3.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                elif suit1 == self.Trump and suit2 != self.Trump:
                    for card in self.Hand:
                        if self.Trump in card:
                            __temp_list_Trumps.update({card: self.Hand[card]})
                    if len(__temp_list_Trumps) > 0:
                        card = min(__temp_list_Trumps,
                                   key=__temp_list_Trumps.get)
                        card_to_send = {card: self.Hand[card]}
                        self.Hand.pop(card)
                        return card_to_send
                    else:
                        __suit_other1 = 0
                        __suit_other1_value = 0
                        __temp_list_other1 = {}
                        __suit_other2 = 0
                        __suit_other2_value = 0
                        __temp_list_other2 = {}
                        __suit_other3 = 0
                        __suit_other3_value = 0
                        __temp_list_other3 = {}
                        __suits_in_Hand = [x for x in [
                            'Spade', 'Club', 'Diamond', 'Heart'] if x != self.Trump]
                        for card in self.Hand:
                            if card[0:-2] == __suits_in_Hand[0]:
                                __suit_other1 += 1
                                __suit_other1_value += self.Hand[card]
                                __weight_other1 = __suit_other1_value/__suit_other1
                                __temp_list_other1.update(
                                    {card: self.Hand[card]})
                            elif card[0:-2] == __suits_in_Hand[1]:
                                __suit_other2 += 1
                                __suit_other2_value += self.Hand[card]
                                __weight_other2 = __suit_other2_value/__suit_other2
                                __temp_list_other2.update(
                                    {card: self.Hand[card]})
                            else:
                                __suit_other3 += 1
                                __suit_other3_value += self.Hand[card]
                                __weight_other3 = __suit_other3_value/__suit_other3
                                __temp_list_other3.update(
                                    {card: self.Hand[card]})
                        if __weight_other1 >= __weight_other2:
                            card = min(__temp_list_other1,
                                       key=__temp_list_other1.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        elif __weight_other2 >= __weight_other3:
                            card = min(__temp_list_other2,
                                       key=__temp_list_other2.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        else:
                            card = min(__temp_list_other3,
                                       key=__temp_list_other3.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send

                elif suit1 != self.Trump and suit2 == self.Trump:
                    for card in self.Hand:
                        if suit1 in card:
                            __temp_list.update({card: self.Hand[card]})
                    if len(__temp_list) > 0:
                        card = min(__temp_list, key=__temp_list.get)
                        card_to_send = {card: self.Hand[card]}
                        self.Hand.pop(card)
                        return card_to_send
                    else:
                        for card in self.Hand:
                            if self.Trump in card:
                                __temp_list_Trumps.update(
                                    {card: self.Hand[card]})
                        if len(__temp_list_Trumps) > 0:
                            for card in __temp_list_Trumps:
                                if __temp_list_Trumps[card] > self.PlayGroundCards[inst_cards[1]]:
                                    card_to_send = {card: self.Hand[card]}
                                    self.Hand.pop(card)
                                    return card_to_send
                    __suit_other1 = 0
                    __suit_other1_value = 0
                    __temp_list_other1 = {}
                    __suit_other2 = 0
                    __suit_other2_value = 0
                    __temp_list_other2 = {}
                    __suits_in_Hand = [x for x in [
                        'Spade', 'Club', 'Diamond', 'Heart'] if x not in [suit1, self.Trump]]
                    for card in self.Hand:
                        if card[0:-2] == __suits_in_Hand[0]:
                            __suit_other1 += 1
                            __suit_other1_value += self.Hand[card]
                            __weight_other1 = __suit_other1_value/__suit_other1
                            __temp_list_other1.update({card: self.Hand[card]})
                        else:
                            __suit_other2 += 1
                            __suit_other2_value += self.Hand[card]
                            __weight_other2 = __suit_other2_value/__suit_other2
                            __temp_list_other2.update({card: self.Hand[card]})
                    if __weight_other1 >= __weight_other2:
                        card = min(__temp_list_other1,
                                   key=__temp_list_other1.get)
                        card_to_send = {card: self.Hand[card]}
                        self.Hand.pop(card)
                        return card_to_send
                    else:
                        card = min(__temp_list_other2,
                                   key=__temp_list_other2.get)
                        card_to_send = {card: self.Hand[card]}
                        self.Hand.pop(card)
                        return card_to_send
                elif suit1 == suit2:
                    for card in self.Hand:
                        if suit1 in card:
                            __temp_list.update({card: self.Hand[card]})
                    if len(__temp_list) > 0:
                        if self.PlayGroundCards[inst_cards[0]] > self.PlayGroundCards[inst_cards[1]]:
                            card = min(__temp_list, key=__temp_list.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        else:
                            for card in __temp_list:
                                if __temp_list[card] > self.PlayGroundCards[inst_cards[1]]:
                                    card_to_send = {card: self.Hand[card]}
                                    self.Hand.pop(card)
                                    return card_to_send
                            card = min(__temp_list, key=__temp_list.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                    else:
                        __suit_other1 = 0
                        __suit_other1_value = 0
                        __temp_list_other1 = {}
                        __suit_other2 = 0
                        __suit_other2_value = 0
                        __temp_list_other2 = {}
                        __suits_in_Hand = [x for x in [
                            'Spade', 'Club', 'Diamond', 'Heart'] if x not in [suit1, self.Trump]]
                        for card in self.Hand:
                            if card[0:-2] == __suits_in_Hand[0]:
                                __suit_other1 += 1
                                __suit_other1_value += self.Hand[card]
                                __weight_other1 = __suit_other1_value/__suit_other1
                                __temp_list_other1.update(
                                    {card: self.Hand[card]})
                            else:
                                __suit_other2 += 1
                                __suit_other2_value += self.Hand[card]
                                __weight_other2 = __suit_other2_value/__suit_other2
                                __temp_list_other2.update(
                                    {card: self.Hand[card]})
                        if __weight_other1 >= __weight_other2:
                            card = min(__temp_list_other1,
                                       key=__temp_list_other1.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        else:
                            card = min(__temp_list_other2,
                                       key=__temp_list_other2.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                else:
                    for card in self.Hand:
                        if suit1 in card:
                            __temp_list.update({card: self.Hand[card]})
                    if len(__temp_list) > 0:
                        card = max(__temp_list, key=__temp_list.get)
                        if self.PlayGroundCards[inst_cards[0]] > __temp_list[card]:
                            card = min(__temp_list, key=__temp_list.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        else:
                            card = max(__temp_list, key=__temp_list.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                    for card in self.Hand:
                        if self.Trump in card:
                            __temp_list_Trumps.update({card: self.Hand[card]})
                    if len(__temp_list_Trumps) > 0:
                        card = min(__temp_list_Trumps,
                                   key=__temp_list_Trumps.get)
                        card_to_send = {card: self.Hand[card]}
                        self.Hand.pop(card)
                        return card_to_send
                    else:
                        __suit_other1 = 0
                        __suit_other1_value = 0
                        __temp_list_other1 = {}
                        __suit_other2 = 0
                        __suit_other2_value = 0
                        __temp_list_other2 = {}
                        __suits_in_Hand = [x for x in [
                            'Spade', 'Club', 'Diamond', 'Heart'] if x not in [suit1, self.Trump]]
                        for card in self.Hand:
                            if card[0:-2] == __suits_in_Hand[0]:
                                __suit_other1 += 1
                                __suit_other1_value += self.Hand[card]
                                __weight_other1 = __suit_other1_value/__suit_other1
                                __temp_list_other1.update(
                                    {card: self.Hand[card]})
                            else:
                                __suit_other2 += 1
                                __suit_other2_value += self.Hand[card]
                                __weight_other2 = __suit_other2_value/__suit_other2
                                __temp_list_other2.update(
                                    {card: self.Hand[card]})
                        if __weight_other1 >= __weight_other2:
                            card = min(__temp_list_other1,
                                       key=__temp_list_other1.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        else:
                            card = min(__temp_list_other2,
                                       key=__temp_list_other2.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
            case 3:
                inst_cards = list(self.PlayGroundCards)
                suit1 = inst_cards[0][0:-2]
                suit2 = inst_cards[1][0:-2]
                suit3 = inst_cards[2][0:-2]
                if suit1 == suit2 == suit3 == self.Trump:
                    for card in self.Hand:
                        if self.Trump in card:
                            __temp_list_Trumps.update({card: self.Hand[card]})
                    if len(__temp_list_Trumps) > 0:
                        if self.PlayGroundCards[inst_cards[1]] > max(
                                self.PlayGroundCards[inst_cards[0]], self.PlayGroundCards[inst_cards[2]]):
                            card = min(__temp_list_Trumps,
                                       key=__temp_list_Trumps.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        else:
                            for card in __temp_list_Trumps:
                                if __temp_list_Trumps[card] > max(
                                        self.PlayGroundCards[inst_cards[0]], self.PlayGroundCards[inst_cards[2]]):
                                    card_to_send = {card: self.Hand[card]}
                                    self.Hand.pop(card)
                                    return card_to_send
                            else:
                                card = min(__temp_list_Trumps,
                                           key=__temp_list_Trumps.get)
                                card_to_send = {card: self.Hand[card]}
                                self.Hand.pop(card)
                                return card_to_send
                    else:
                        __suit_other1 = 0
                        __suit_other1_value = 0
                        __temp_list_other1 = {}
                        __suit_other2 = 0
                        __suit_other2_value = 0
                        __temp_list_other2 = {}
                        __suit_other3 = 0
                        __suit_other3_value = 0
                        __temp_list_other3 = {}
                        __suits_in_Hand = [x for x in [
                            'Spade', 'Club', 'Diamond', 'Heart'] if x != self.Trump]
                        for card in self.Hand:
                            if card[0:-2] == __suits_in_Hand[0]:
                                __suit_other1 += 1
                                __suit_other1_value += self.Hand[card]
                                __weight_other1 = __suit_other1_value/__suit_other1
                                __temp_list_other1.update(
                                    {card: self.Hand[card]})
                            elif card[0:-2] == __suits_in_Hand[1]:
                                __suit_other2 += 1
                                __suit_other2_value += self.Hand[card]
                                __weight_other2 = __suit_other2_value/__suit_other2
                                __temp_list_other2.update(
                                    {card: self.Hand[card]})
                            else:
                                __suit_other3 += 1
                                __suit_other3_value += self.Hand[card]
                                __weight_other3 = __suit_other3_value/__suit_other3
                                __temp_list_other3.update(
                                    {card: self.Hand[card]})
                        if __weight_other1 >= __weight_other2:
                            card = min(__temp_list_other1,
                                       key=__temp_list_other1.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        elif __weight_other2 >= __weight_other3:
                            card = min(__temp_list_other2,
                                       key=__temp_list_other2.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        else:
                            card = min(__temp_list_other3,
                                       key=__temp_list_other3.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                elif suit1 == suit2 == self.Trump and suit3 != self.Trump:
                    for card in self.Hand:
                        if self.Trump in card:
                            __temp_list_Trumps.update({card: self.Hand[card]})
                    if len(__temp_list_Trumps) > 0:
                        if self.PlayGroundCards[inst_cards[1]] > self.PlayGroundCards[inst_cards[0]]:
                            card = min(__temp_list_Trumps,
                                       key=__temp_list_Trumps.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        else:
                            for card in __temp_list_Trumps:
                                if __temp_list_Trumps[card] > self.PlayGroundCards[inst_cards[0]]:
                                    card_to_send = {card: self.Hand[card]}
                                    self.Hand.pop(card)
                                    return card_to_send
                            else:
                                card = min(__temp_list_Trumps,
                                           key=__temp_list_Trumps.get)
                                card_to_send = {card: self.Hand[card]}
                                self.Hand.pop(card)
                                return card_to_send
                    else:
                        __suit_other1 = 0
                        __suit_other1_value = 0
                        __temp_list_other1 = {}
                        __suit_other2 = 0
                        __suit_other2_value = 0
                        __temp_list_other2 = {}
                        __suit_other3 = 0
                        __suit_other3_value = 0
                        __temp_list_other3 = {}
                        __suits_in_Hand = [x for x in [
                            'Spade', 'Club', 'Diamond', 'Heart'] if x != self.Trump]
                        for card in self.Hand:
                            if card[0:-2] == __suits_in_Hand[0]:
                                __suit_other1 += 1
                                __suit_other1_value += self.Hand[card]
                                __weight_other1 = __suit_other1_value/__suit_other1
                                __temp_list_other1.update(
                                    {card: self.Hand[card]})
                            elif card[0:-2] == __suits_in_Hand[1]:
                                __suit_other2 += 1
                                __suit_other2_value += self.Hand[card]
                                __weight_other2 = __suit_other2_value/__suit_other2
                                __temp_list_other2.update(
                                    {card: self.Hand[card]})
                            else:
                                __suit_other3 += 1
                                __suit_other3_value += self.Hand[card]
                                __weight_other3 = __suit_other3_value/__suit_other3
                                __temp_list_other3.update(
                                    {card: self.Hand[card]})
                        if __weight_other1 >= __weight_other2:
                            card = min(__temp_list_other1,
                                       key=__temp_list_other1.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        elif __weight_other2 >= __weight_other3:
                            card = min(__temp_list_other2,
                                       key=__temp_list_other2.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        else:
                            card = min(__temp_list_other3,
                                       key=__temp_list_other3.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                elif suit1 == suit3 == self.Trump and suit2 != self.Trump:
                    for card in self.Hand:
                        if self.Trump in card:
                            __temp_list_Trumps.update({card: self.Hand[card]})
                    if len(__temp_list_Trumps) > 0:
                        for card in __temp_list_Trumps:
                            if __temp_list_Trumps[card] > max(self.PlayGroundCards[inst_cards[0]], self.PlayGroundCards[inst_cards[2]]):
                                card_to_send = {card: self.Hand[card]}
                                self.Hand.pop(card)
                                return card_to_send
                        card = min(__temp_list_Trumps,
                                   key=__temp_list_Trumps.get)
                        card_to_send = {card: self.Hand[card]}
                        self.Hand.pop(card)
                        return card_to_send
                    else:
                        __suit_other1 = 0
                        __suit_other1_value = 0
                        __temp_list_other1 = {}
                        __suit_other2 = 0
                        __suit_other2_value = 0
                        __temp_list_other2 = {}
                        __suit_other3 = 0
                        __suit_other3_value = 0
                        __temp_list_other3 = {}
                        __suits_in_Hand = [x for x in [
                            'Spade', 'Club', 'Diamond', 'Heart'] if x != self.Trump]
                        for card in self.Hand:
                            if card[0:-2] == __suits_in_Hand[0]:
                                __suit_other1 += 1
                                __suit_other1_value += self.Hand[card]
                                __weight_other1 = __suit_other1_value/__suit_other1
                                __temp_list_other1.update(
                                    {card: self.Hand[card]})
                            elif card[0:-2] == __suits_in_Hand[1]:
                                __suit_other2 += 1
                                __suit_other2_value += self.Hand[card]
                                __weight_other2 = __suit_other2_value/__suit_other2
                                __temp_list_other2.update(
                                    {card: self.Hand[card]})
                            else:
                                __suit_other3 += 1
                                __suit_other3_value += self.Hand[card]
                                __weight_other3 = __suit_other3_value/__suit_other3
                                __temp_list_other3.update(
                                    {card: self.Hand[card]})
                        if __weight_other1 >= __weight_other2:
                            card = min(__temp_list_other1,
                                       key=__temp_list_other1.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        elif __weight_other2 >= __weight_other3:
                            card = min(__temp_list_other2,
                                       key=__temp_list_other2.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        else:
                            card = min(__temp_list_other3,
                                       key=__temp_list_other3.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                elif suit1 == self.Trump and suit2 != self.Trump and suit3 != self.Trump:
                    for card in self.Hand:
                        if self.Trump in card:
                            __temp_list_Trumps.update({card: self.Hand[card]})
                    if len(__temp_list_Trumps) > 0:
                        for card in __temp_list_Trumps:
                            if __temp_list_Trumps[card] > self.PlayGroundCards[inst_cards[0]]:
                                card_to_send = {card: self.Hand[card]}
                                self.Hand.pop(card)
                                return card_to_send
                        card = min(__temp_list_Trumps,
                                   key=__temp_list_Trumps.get)
                        card_to_send = {card: self.Hand[card]}
                        self.Hand.pop(card)
                        return card_to_send
                    else:
                        __suit_other1 = 0
                        __suit_other1_value = 0
                        __temp_list_other1 = {}
                        __suit_other2 = 0
                        __suit_other2_value = 0
                        __temp_list_other2 = {}
                        __suit_other3 = 0
                        __suit_other3_value = 0
                        __temp_list_other3 = {}
                        __suits_in_Hand = [x for x in [
                            'Spade', 'Club', 'Diamond', 'Heart'] if x != self.Trump]
                        for card in self.Hand:
                            if card[0:-2] == __suits_in_Hand[0]:
                                __suit_other1 += 1
                                __suit_other1_value += self.Hand[card]
                                __weight_other1 = __suit_other1_value/__suit_other1
                                __temp_list_other1.update(
                                    {card: self.Hand[card]})
                            elif card[0:-2] == __suits_in_Hand[1]:
                                __suit_other2 += 1
                                __suit_other2_value += self.Hand[card]
                                __weight_other2 = __suit_other2_value/__suit_other2
                                __temp_list_other2.update(
                                    {card: self.Hand[card]})
                            else:
                                __suit_other3 += 1
                                __suit_other3_value += self.Hand[card]
                                __weight_other3 = __suit_other3_value/__suit_other3
                                __temp_list_other3.update(
                                    {card: self.Hand[card]})
                        if __weight_other1 >= __weight_other2:
                            card = min(__temp_list_other1,
                                       key=__temp_list_other1.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        elif __weight_other2 >= __weight_other3:
                            card = min(__temp_list_other2,
                                       key=__temp_list_other2.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        else:
                            card = min(__temp_list_other3,
                                       key=__temp_list_other3.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                elif suit1 != self.Trump and suit2 == suit3 == self.Trump:
                    for card in self.Hand:
                        if suit1 in card:
                            __temp_list.update({card: self.Hand[card]})
                    if len(__temp_list) > 0:
                        card = min(__temp_list, key=__temp_list.get)
                        card_to_send = {card: self.Hand[card]}
                        self.Hand.pop(card)
                        return card_to_send
                    else:
                        for card in self.Hand:
                            if self.Trump in card:
                                __temp_list_Trumps.update(
                                    {card: self.Hand[card]})
                        if len(__temp_list_Trumps) > 0:
                            if self.PlayGroundCards[inst_cards[2]] > self.PlayGroundCards[inst_cards[1]]:
                                for card in __temp_list_Trumps:
                                    if __temp_list_Trumps[card] > self.PlayGroundCards[inst_cards[2]]:
                                        card_to_send = {card: self.Hand[card]}
                                        self.Hand.pop(card)
                                        return card_to_send
                    __suit_other1 = 0
                    __suit_other1_value = 0
                    __temp_list_other1 = {}
                    __suit_other2 = 0
                    __suit_other2_value = 0
                    __temp_list_other2 = {}
                    __suits_in_Hand = [x for x in [
                        'Spade', 'Club', 'Diamond', 'Heart'] if x not in [suit1, self.Trump]]
                    for card in self.Hand:
                        if card[0:-2] == __suits_in_Hand[0]:
                            __suit_other1 += 1
                            __suit_other1_value += self.Hand[card]
                            __weight_other1 = __suit_other1_value/__suit_other1
                            __temp_list_other1.update({card: self.Hand[card]})
                        else:
                            __suit_other2 += 1
                            __suit_other2_value += self.Hand[card]
                            __weight_other2 = __suit_other2_value/__suit_other2
                            __temp_list_other2.update({card: self.Hand[card]})
                    if __weight_other1 >= __weight_other2:
                        card = min(__temp_list_other1,
                                   key=__temp_list_other1.get)
                        card_to_send = {card: self.Hand[card]}
                        self.Hand.pop(card)
                        return card_to_send
                    else:
                        card = min(__temp_list_other2,
                                   key=__temp_list_other2.get)
                        card_to_send = {card: self.Hand[card]}
                        self.Hand.pop(card)
                        return card_to_send
                elif suit1 != self.Trump and suit2 == self.Trump and suit3 != self.Trump:
                    for card in self.Hand:
                        if suit1 in card:
                            __temp_list.update({card: self.Hand[card]})
                    if len(__temp_list) > 0:
                        card = min(__temp_list, key=__temp_list.get)
                        card_to_send = {card: self.Hand[card]}
                        self.Hand.pop(card)
                        return card_to_send
                    else:
                        __suit_other1 = 0
                        __suit_other1_value = 0
                        __temp_list_other1 = {}
                        __suit_other2 = 0
                        __suit_other2_value = 0
                        __temp_list_other2 = {}
                        __suits_in_Hand = [x for x in [
                            'Spade', 'Club', 'Diamond', 'Heart'] if x not in [suit1, self.Trump]]
                        for card in self.Hand:
                            if card[0:-2] == __suits_in_Hand[0]:
                                __suit_other1 += 1
                                __suit_other1_value += self.Hand[card]
                                __weight_other1 = __suit_other1_value/__suit_other1
                                __temp_list_other1.update(
                                    {card: self.Hand[card]})
                            else:
                                __suit_other2 += 1
                                __suit_other2_value += self.Hand[card]
                                __weight_other2 = __suit_other2_value/__suit_other2
                                __temp_list_other2.update(
                                    {card: self.Hand[card]})
                        if __weight_other1 >= __weight_other2:
                            card = min(__temp_list_other1,
                                       key=__temp_list_other1.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                        else:
                            card = min(__temp_list_other2,
                                       key=__temp_list_other2.get)
                            card_to_send = {card: self.Hand[card]}
                            self.Hand.pop(card)
                            return card_to_send
                elif suit1 != self.Trump and suit2 != self.Trump and suit3 == self.Trump:
                    for card in self.Hand:
                        if suit1 in card:
                            __temp_list.update({card: self.Hand[card]})
                    if len(__temp_list) > 0:
                        card = min(__temp_list, key=__temp_list.get)
                        card_to_send = {card: self.Hand[card]}
                        self.Hand.pop(card)
                        return card_to_send
                    else:
                        for card in self.Hand:
                            if self.Trump in card:
                                __temp_list_Trumps.update(
                                    {card: self.Hand[card]})
                        if len(__temp_list_Trumps) > 0:
                            for card in __temp_list_Trumps:
                                if __temp_list_Trumps[card] > self.PlayGroundCards[inst_cards[2]]:
                                    card_to_send = {card: self.Hand[card]}
                                    self.Hand.pop(card)
                                    return card_to_send
                        else:
                            __suit_other1 = 0
                            __suit_other1_value = 0
                            __temp_list_other1 = {}
                            __suit_other2 = 0
                            __suit_other2_value = 0
                            __temp_list_other2 = {}
                            __suits_in_Hand = [x for x in [
                                'Spade', 'Club', 'Diamond', 'Heart'] if x not in [suit1, self.Trump]]
                            for card in self.Hand:
                                if card[0:-2] == __suits_in_Hand[0]:
                                    __suit_other1 += 1
                                    __suit_other1_value += self.Hand[card]
                                    __weight_other1 = __suit_other1_value/__suit_other1
                                    __temp_list_other1.update(
                                        {card: self.Hand[card]})
                                else:
                                    __suit_other2 += 1
                                    __suit_other2_value += self.Hand[card]
                                    __weight_other2 = __suit_other2_value/__suit_other2
                                    __temp_list_other2.update(
                                        {card: self.Hand[card]})
                            if __weight_other1 >= __weight_other2:
                                card = min(__temp_list_other1,
                                           key=__temp_list_other1.get)
                                card_to_send = {card: self.Hand[card]}
                                self.Hand.pop(card)
                                return card_to_send
                            else:
                                card = min(__temp_list_other2,
                                           key=__temp_list_other2.get)
                                card_to_send = {card: self.Hand[card]}
                                self.Hand.pop(card)
                                return card_to_send
                else:
                    if suit1 == suit2:
                        for card in self.Hand:
                            if suit1 in card:
                                __temp_list.update({card: self.Hand[card]})
                            if len(__temp_list) > 0:
                                if suit3 == suit1:
                                    if self.PlayGroundCards[inst_cards[1]] > max(self.PlayGroundCards[inst_cards[0]],
                                                                                 self.PlayGroundCards[inst_cards[2]]):
                                        card = min(
                                            __temp_list, key=__temp_list.get)
                                        card_to_send = {card: self.Hand[card]}
                                        self.Hand.pop(card)
                                        return card_to_send
                                    else:
                                        for card in __temp_list:
                                            if __temp_list[card] > max(self.PlayGroundCards[inst_cards[0]], self.PlayGroundCards[inst_cards[2]]):
                                                card_to_send = {
                                                    card: self.Hand[card]}
                                                self.Hand.pop(card)
                                                return card_to_send
                                            else:
                                                card = min(
                                                    __temp_list, key=__temp_list.get)
                                                card_to_send = {
                                                    card: self.Hand[card]}
                                                self.Hand.pop(card)
                                                return card_to_send
                                else:
                                    if self.PlayGroundCards[inst_cards[1]] > self.PlayGroundCards[inst_cards[0]]:
                                        card = min(
                                            __temp_list, key=__temp_list.get)
                                        card_to_send = {card: self.Hand[card]}
                                        self.Hand.pop(card)
                                        return card_to_send
                                    else:
                                        for card in __temp_list:
                                            if __temp_list[card] > self.PlayGroundCards[inst_cards[0]]:
                                                card_to_send = {
                                                    card: self.Hand[card]}
                                                self.Hand.pop(card)
                                                return card_to_send
                                        card = min(
                                            __temp_list, key=__temp_list.get)
                                        card_to_send = {card: self.Hand[card]}
                                        self.Hand.pop(card)
                                        return card_to_send
                            else:
                                for card in self.Hand:
                                    if self.Trump in card:
                                        __temp_list_Trumps.update(
                                            {card: self.Hand[card]})
                                if len(__temp_list_Trumps) > 0:
                                    card = min(
                                        __temp_list_Trumps, key=__temp_list_Trumps.get)
                                    card_to_send = {card: self.Hand[card]}
                                    self.Hand.pop(card)
                                    return card_to_send
                                else:
                                    __suit_other1 = 0
                                    __suit_other1_value = 0
                                    __temp_list_other1 = {}
                                    __suit_other2 = 0
                                    __suit_other2_value = 0
                                    __temp_list_other2 = {}
                                    __suits_in_Hand = [x for x in [
                                        'Spade', 'Club', 'Diamond', 'Heart'] if x not in [suit1, self.Trump]]
                                    for card in self.Hand:
                                        if card[0:-2] == __suits_in_Hand[0]:
                                            __suit_other1 += 1
                                            __suit_other1_value += self.Hand[card]
                                            __weight_other1 = __suit_other1_value/__suit_other1
                                            __temp_list_other1.update(
                                                {card: self.Hand[card]})
                                        else:
                                            __suit_other2 += 1
                                            __suit_other2_value += self.Hand[card]
                                            __weight_other2 = __suit_other2_value/__suit_other2
                                            __temp_list_other2.update(
                                                {card: self.Hand[card]})
                                    if __weight_other1 >= __weight_other2:
                                        card = min(__temp_list_other1,
                                                   key=__temp_list_other1.get)
                                        card_to_send = {card: self.Hand[card]}
                                        self.Hand.pop(card)
                                        return card_to_send
                                    else:
                                        card = min(__temp_list_other2,
                                                   key=__temp_list_other2.get)
                                        card_to_send = {card: self.Hand[card]}
                                        self.Hand.pop(card)
                                        return card_to_send
                    else:
                        for card in self.Hand:
                            if suit1 in card:
                                __temp_list.update({card: self.Hand[card]})
                            if len(__temp_list) > 0:
                                for card in __temp_list:
                                    if suit3 == suit1:
                                        if __temp_list[card] > max(self.PlayGroundCards[inst_cards[0]],
                                                                   self.PlayGroundCards[inst_cards[2]]):
                                            card_to_send = {
                                                card: self.Hand[card]}
                                            self.Hand.pop(card)
                                            return card_to_send
                                        card = min(
                                            __temp_list, key=__temp_list.get)
                                        card_to_send = {card: self.Hand[card]}
                                        self.Hand.pop(card)
                                        return card_to_send
                                    else:
                                        if __temp_list[card] > self.PlayGroundCards[inst_cards[0]]:
                                            card_to_send = {
                                                card: self.Hand[card]}
                                            self.Hand.pop(card)
                                            return card_to_send
                                        card = min(
                                            __temp_list, key=__temp_list.get)
                                        card_to_send = {card: self.Hand[card]}
                                        self.Hand.pop(card)
                                        return card_to_send
                            else:
                                for card in self.Hand:
                                    if self.Trump in card:
                                        __temp_list_Trumps.update(
                                            {card: self.Hand[card]})
                                if len(__temp_list_Trumps) > 0:
                                    card = min(
                                        __temp_list, key=__temp_list.get)
                                    card_to_send = {card: self.Hand[card]}
                                    self.Hand.pop(card)
                                    return card_to_send
                                else:
                                    __suit_other1 = 0
                                    __suit_other1_value = 0
                                    __temp_list_other1 = {}
                                    __suit_other2 = 0
                                    __suit_other2_value = 0
                                    __temp_list_other2 = {}
                                    __suits_in_Hand = [x for x in [
                                        'Spade', 'Club', 'Diamond', 'Heart'] if x not in [suit1, self.Trump]]
                                    for card in self.Hand:
                                        if card[0:-2] == __suits_in_Hand[0]:
                                            __suit_other1 += 1
                                            __suit_other1_value += self.Hand[card]
                                            __weight_other1 = __suit_other1_value/__suit_other1
                                            __temp_list_other1.update(
                                                {card: self.Hand[card]})
                                        else:
                                            __suit_other2 += 1
                                            __suit_other2_value += self.Hand[card]
                                            __weight_other2 = __suit_other2_value/__suit_other2
                                            __temp_list_other2.update(
                                                {card: self.Hand[card]})
                                    if __weight_other1 >= __weight_other2:
                                        card = min(__temp_list_other1,
                                                   key=__temp_list_other1.get)
                                        card_to_send = {card: self.Hand[card]}
                                        self.Hand.pop(card)
                                        return card_to_send
                                    else:
                                        card = min(__temp_list_other2,
                                                   key=__temp_list_other2.get)
                                        card_to_send = {card: self.Hand[card]}
                                        self.Hand.pop(card)
                                        return card_to_send

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

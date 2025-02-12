class Card :
    def __init__(self, value, symbol, number, state):
        self.value = value
        self.symbol = symbol
        self.number = number
        self.state = state

    def show(self):
        print(f"{self.number} of {self.symbol}. Value : {self.value}")


class Deck : 
    def __init__(self):
        self.card_list = []

    def add_a_card_in_deck (self, card):
        self.card_list.append(card)

    def shuffle_deck(self) :
        pass

    def show(self):
        print(f"Number of card in the deck : {len(self.card_list)}")
        for card in self.card_list:
            card.show()

class Human: 
    def __init__(self, money, name):
        self.money = money
        self.name = name
        self.bet = 0
        self.hand = []

    def pick_a_card (self) :
        pass
        
    def throw_a_card (self) : 
        pass 

class Dealer(Human): 
    pass


card_deck = Deck()

symbol = ["spades", "diamonds", "clubs", "hearts"]
number = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

# for o in range (0, 4, 1):
for i in range(0, 4, 1): 
    for j in range(0, 13, 1):
        if j < 10 and j > 0:
            card_value = j + 1
        elif j == 0 :
            card_value = 11
        else:
            card_value = 10
        
        card_deck.add_a_card_in_deck(Card(card_value, symbol[i], number[j], True))


card_deck.show()



my_player = Human(1000, "Mickeal")
dealer = Dealer(10000, "Andrew")



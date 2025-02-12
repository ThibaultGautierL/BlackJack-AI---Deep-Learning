class Dealer: 
    def __init__(self, name):
        self.money = 1000000
        self.name = name
        self.bet = 0
        self.hand = []
        self.total_hand_value = 0

    def pick_a_card (self, card) :
        self.hand.append(card)
        
    def throw_cards (self) : 
        self.hand.clear()

    def show_hand(self):
        print("Dealer's Hand :")
        for index, card in enumerate(self.hand):
            if index == 0:
                card.show()
            else:
                print("[Carte cachée]")





class Human(Dealer): 
    
    def __init__(self, name, money):
        super().__init__(name)
        self.money = money
    
    def show_hand(self):
        self.total_hand_value = 0
        print("Your Hand :")
        for card in self.hand:
            card.show()
            self.total_hand_value += card.value
        print(f"Total Hand Value : {self.total_hand_value}")

    def bet_money(self, value):
        self.bet = value
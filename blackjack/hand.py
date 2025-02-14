class Hand:

    def __init__(self, number,card = None):
        self.value = 0
        self.cards = []
        self.bet = 0
        self.number = number

        if card is not None:
            self.add_a_cart(card)

    
    def add_a_cart(self, card):
        self.cards.append(card)
        self.update_hand_value(card)

    def update_hand_value(self, card):
        #Si j'ai un main supérieure à 10 (soit 11 et +), mon As vaut 1 au lieu de 11
        if self.value > 10 and card.value == 11:
            self.value += 1
        else:
            self.value += card.value


    def split_card(self):
        #On retire la première carte et on retire la valeur à notre main
        card_to_split = self.cards.pop(0)
        self.value -= card_to_split.value
        return card_to_split
    

    def add_a_bet(self, value):
        self.bet = value


    def doble_bet(self):
        self.bet *= 2


    def clear(self):
        self.value = 0 
        self.cards.clear()
        self.bet = 0


    def show(self):
        print(f"Votre Main {self.number}:")
        for card in self.cards:
            card.show()
        print(f"Valeur de votre main : {self.value}")

    

    def show_bank_hand(self, end):
        first_card_value = 0

        print("Main de la banque :")
        for index, card in enumerate(self.cards): 

            #Au premier tour, quand le joueur joue, on ne connait pas la 2eme carte du croupier
            if len(self.cards) <= 2 and not end:
                if index == 0:
                    card.show()
                    first_card_value = card.value
                else:
                    print("[Carte Cachée]")

            else: # Sinon, on affiche toute la main
                card.show()

        ##Quand c'est le premier tour, la valeur affichée de la main du dealer est théorique (car on ne connait pas la 2nd carte)
        if (len(self.cards) <= 2) and not end:
            print(f"Valeur théorique de la main de la banque : {first_card_value}")
        else: # Sinon Afficher la main
            print(f"Valeur de la main de la banque : {self.value}")

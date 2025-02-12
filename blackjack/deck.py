import random

class Deck : 
    def __init__(self):
        self.card_list = []
        self.card_already_picked = []

    def add_a_card_in_deck (self, card):
        self.card_list.append(card)

    def shuffle(self):
        random.shuffle(self.card_list)

    def pick_a_card(self, player):
        self.card_already_picked.append(self.card_list[0])
        player.pick_a_card(self.card_list[0])
        self.card_list.remove(self.card_list[0])

    def show(self):
        print(f"Number of card in the deck : {len(self.card_list)}")
        for card in self.card_list:
            card.show()


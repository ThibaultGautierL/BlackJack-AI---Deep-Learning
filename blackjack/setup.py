from blackjack.deck import Deck
from blackjack.card import Card


def setup_deck():

    card_deck = Deck()
    symbol = ["♠️", "♦️", "♣️", "♥️"]
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

    return card_deck
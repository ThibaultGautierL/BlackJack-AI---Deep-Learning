from blackjack.hand import Hand

class Dealer: #Class Dealer

    def __init__(self, name):
        self.money = 1000000
        self.name = name
        self.hands = [Hand(1)]
        

    #Carte Distribuée
    def pick_a_card (self, card, hand=0) :
        #J'envoie ma carte à ma main qui à le numéro de "hand"
        self.hands[hand].add_a_cart(card)


    #Supprimer la main (quand la partie est finie)
    def empty_hand(self):
        for hand in self.hands:
            hand.clear()
        
        #Si on a plus d'une seule main, je supprime la 2nd, pour la prochaine partie.
        if len(self.hands) > 1:
            del self.hands[1]


    #Show
    def show_hand(self, end = False):
        self.hands[0].show_bank_hand(end)




#Inherits from Dealer
class Human(Dealer): 
    
    #Ajoute la valeur attribut et Pari
    def __init__(self, name, money):
        super().__init__(name)
        self.old_money = 0
        self.money = money


    #Parier de l'argent
    def bet_money(self, bet):
        self.hands[0].add_a_bet(bet)
        self.old_money = self.money
        self.money -= self.hands[0].bet
        print(f"Mise de {self.hands[0].bet}€. Argent restant {self.money}€")


    #Pour le double
    def doble_bet(self, index=0) :
        bet_total = 0
        #On retire de nouveau la valeur du bet à notre argent, et on double la valeur du bet
        self.money -= self.hands[0].bet
        self.hands[index].doble_bet()

        for index, hand in enumerate(self.hands):
            bet_total += hand.bet

        print(f"Nouvelle mise totale :{bet_total}€. Argent restant {self.money}€")


    #Pour le split de carte
    def split(self, deck) :
        bet_total = 0
        #On retire notre première carte de la main, pour l'ajouter à une nouvelle carte. 
        card_to_split = self.hands[0].split_card()
        self.hands.append(Hand(2, card_to_split))
        
        #on retire de nouveau la mise de notre premier bet à notre argent (car au split, on remise le double) et on ajoute ce bet à notre nouvelle main
        self.money -= self.hands[0].bet
        self.hands[1].bet = self.hands[0].bet

        for index, hand in enumerate(self.hands):
            bet_total += hand.bet
            deck.pick_a_card(self, index)
            hand.show()
        
        print(f"Nouvelle mise totale :{bet_total}€. Argent restant {self.money}€")


    #Si le joueur perd
    def loose_game(self, index):
        self.hands[index].clear()
        print(f"Main {index+1} Perdu")


    #Si le joueuru gagne
    def win_game(self, index):
        self.money += (2*self.hands[index].bet)
        self.hands[index].clear()
        print(f"Main {index+1} Gagné")


    #BlackJack
    def blackjack(self, index):
        self.money += (2.5*self.hands[index].bet)
        self.hands[index].clear()
        print(f"Main {index+1} BlackJack")
    

    #Si il y a égalité
    def tie_game(self, index):
        self.money += self.hands[index].bet
        self.hands[index].clear()
        print(f"Main {index+1} Egalité")


    #Show
    def show_hand(self, index = 0):
        self.hands[index].show()
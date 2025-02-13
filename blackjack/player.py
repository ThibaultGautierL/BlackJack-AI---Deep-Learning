class Dealer: #Class Dealer

    def __init__(self, name):
        self.money = 1000000
        self.name = name
        self.hand = []
        self.total_hand_value = 0

    #Carte Distribuée
    def pick_a_card (self, card) :
        self.hand.append(card)
        self.update_total_hand_value(card)


    #Mise a jour de la valeur de main 
    def update_total_hand_value(self, card):
        #Si j'ai un main supérieure à 10 (soit 11 et +), mon As vaut 1 au lieu de 11
        if self.total_hand_value > 10 and card.value == 11:
            self.total_hand_value += 1
        else:
            self.total_hand_value += card.value


    #Supprimer la main (quand la partie est finie)
    def empty_hand(self):
        self.hand.clear()
        self.total_hand_value = 0


    #Show
    def show_hand(self):
        first_card_value = 0

        print("Main de la banque :")
        for index, card in enumerate(self.hand): 

            #Au premier tour, quand le joueur joue, on ne connait pas la 2eme carte du croupier
            if len(self.hand) <= 2:
                if index == 0:
                    card.show()
                    first_card_value = card.value
                else:
                    print("[Carte Cachée]")

            else: # Sinon, on affiche toute la main
                card.show()

        ##Quand c'est le premier tour, la valeur affichée de la main du dealer est théorique (car on ne connait pas la 2nd carte)
        if len(self.hand) <= 2:
            print(f"Valeur théorique de la main de la banque : {first_card_value}")
        else: # Sinon Afficher la main
            print(f"Valeur de la main de la banque : {self.total_hand_value}")




#Inherits from Dealer
class Human(Dealer): 
    
    #Ajoute la valeur attribut et Pari
    def __init__(self, name, money):
        super().__init__(name)
        self.old_money = 0
        self.money = money
        self.bet = 0


    #Parier de l'argent
    def bet_money(self, value):
        self.bet = value
        self.old_money = self.money
        self.money -= self.bet
        print(f"Mise de {self.bet}€. Argent restant {self.money}€")


    def doble_bet(self) :
        self.money -= self.bet
        self.bet *= 2
        print(f"Nouvelle mise :{self.bet}€. Argent restant {self.money}€")


    #Si le joueur perd
    def loose_game(self):
        self.bet = 0
        print(f"Perdu. Argent : {self.old_money}€ -> {self.money}€")


    #Si le joueuru gagne
    def win_game(self):
        self.money += (2*self.bet)
        self.bet = 0
        print(f"Gagné, Argent : {self.old_money}€ -> {self.money}€")


    #BlackJack
    def blackjack(self):
        self.money += (2.5*self.bet)
        self.bet = 0
        print(f"BlackJack ! Argent : {self.old_money}€ -> {self.money}€")
    

    #Si il y a égalité
    def tie_game(self):
        self.money += self.bet
        self.bet = 0
        print(f"Egalité, Argent : {self.old_money}€ -> {self.money}€")


    #Vider la main du joueur, et reset ses stats
    def empty_hand(self):
        self.hand.clear()
        self.total_hand_value = 0
        self.bet = 0


    #Show
    def show_hand(self):
        print("Votre Main :")
        for card in self.hand:
            card.show()
        print(f"Valeur de votre main : {self.total_hand_value}")
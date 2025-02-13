from blackjack.deck import Deck
from blackjack.card import Card



#Creer un deck de 4 fois 52 cartes
def setup_deck():

    card_deck = Deck()
    symbol = ["♠️", "♦️", "♣️", "♥️"]
    number = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Reine", "Roi"]


    for o in range (0, 4, 1): #4 Jeux
        for i in range(0, 4, 1): #4 Symboles
            for j in range(0, 13, 1): # 13 Nombres

                #Au blackJack, 10, Valet, Dame, Roi valent 10, et As soit 1 soit 11
                if j < 10 and j > 0:
                    card_value = j + 1
                elif j == 0 :
                    card_value = 11
                else:
                    card_value = 10
                
                card_deck.add_a_card_in_deck(Card(card_value, symbol[i], number[j], True))

    return card_deck



#Parier le jeu, et distribuer les 2 premières cartes
def draw_first_cards(deck, my_player, dealer):
    print(f"Vous avez {my_player.money}€")
    while True:
        try:
            bet = int(input("Faites vos mises"))
            break
        except ValueError:
            print("Entrer une valeur valide")
    
    #Le pari du joueur
    my_player.bet_money(bet)

    #Distribuer 2 cartes pour chacun
    deck.pick_a_card(my_player)
    deck.pick_a_card(dealer)
    deck.pick_a_card(my_player)
    deck.pick_a_card(dealer)

    #Montrer la main des joueurs
    my_player.show_hand()
    dealer.show_hand()



#Actions possibles du joueur
def player_actions(deck, my_player):

    first_turn = True
    blackjack = False

    if my_player.total_hand_value == 21:
        blackjack = True

    #Tant qu'il ne dépasse pas 21 de main
    while my_player.total_hand_value < 21:

        print("Actions possibles :")
        print("1. Tirer une carte")
        if first_turn:
            print("2. Split")
            print("3. Doubler")
            print("4. Rester")
        else:
            print("2. Rester")

        if first_turn:
            shall_continue_game = input("Que voulez-vous faire ? (1/2/3/4) ").strip()
        else:
            shall_continue_game = input("Que voulez-vous faire ? (1/2) ").strip()



        if shall_continue_game == "1":  # Trier une carte
            deck.pick_a_card(my_player)
            my_player.show_hand()
            first_turn = False

        elif (shall_continue_game == "2") and first_turn:  # Spliter le jeu
            my_player.split(deck)
            break

        elif (shall_continue_game == "3") and first_turn:  # Doubler la mise
            #On double la mise
            my_player.doble_bet()
            #On ne pick qu'une carte
            deck.pick_a_card(my_player)
            my_player.show_hand()
            break

        elif ((shall_continue_game == "4") and first_turn) or ((shall_continue_game == "2") and (not first_turn)):  # Rester
            break  

        else:
            print("Entrée invalide !")
    

    return blackjack



#Jeu du dealer. Juste piocher tant qu'on a en dessous de 17
def dealer_logic(deck, dealer):

    if dealer.total_hand_value >= 17: #Permet d'afficher la valeur de la main du dealer, si il a une valeur suppérieur à 17 avec ses 2 premières cartes seulement
        print(f"Main de la Banque : {dealer.total_hand_value}")


    while dealer.total_hand_value < 17: #Tant que le dealer a une valeur de carte en dessous de 17, il doit piocher
        deck.pick_a_card(dealer)
        dealer.show_hand()



#Conditions de victoire :
def win_condition_check(my_player, dealer):

    #Joueur à une valeur de main supérieur à 21 = PERDU
    if my_player.total_hand_value > 21:
        my_player.loose_game()
    elif len(my_player.hand) == 2 and my_player.total_hand_value == 21:
        my_player.blackjack()
    #Croupier à une valeur de main supérieure à 21, et le joueur inférieure = GAGNE
    elif dealer.total_hand_value > 21:
        my_player.win_game()
    #Meme valeur pour le joueur et le croupier = EGALITE
    elif my_player.total_hand_value == dealer.total_hand_value:
        my_player.tie_game()
    #Le joueur a une meilleure valeur = GAGNE
    elif my_player.total_hand_value > dealer.total_hand_value:
        my_player.win_game()
    #Le joueur a une moins bonne valeur = PERDU
    elif my_player.total_hand_value < dealer.total_hand_value:
        my_player.loose_game()

    
    #Empty Hand
    my_player.empty_hand()
    dealer.empty_hand()



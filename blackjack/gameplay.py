from blackjack.deck import Deck
from blackjack.card import Card

VALID_BETS = {100, 200, 400, 500}

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
    while True:
        try:
            bet = int(input("Faites vos mises : ")) 
            if bet in VALID_BETS and bet <= my_player.money:
                break 
            else:
                print(f"Vous devez choisir parmi (100, 200, 400 ou 500), et ne pas dépasser votre solde ({my_player.money}€).")
        except ValueError:
            print("Entrer une valeur valide (100, 200, 400 ou 500).")

    
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
    
    return bet



#Actions possibles du joueur
def player_actions(deck, my_player, dealer, bet):

    first_turn = True
    blackjack = False

    if my_player.hands[0].value == 21:
        blackjack = True


    #Tant qu'il ne dépasse pas 21 de main
    while my_player.hands[0].value < 21:


        #Si le dealer a un black Jack, on arrête la partie
        if len(dealer.hands[0].cards) == 2 and dealer.hands[0].value == 21:
            break


        print("Actions possibles :")
        print("1. Tirer une carte")
        if first_turn and bet <= my_player.money:
            print("2. Split")
            print("3. Doubler")
            print("0. Rester")
            shall_continue_game = input("Que voulez-vous faire ? (1/2/3/0) ").strip()
        else:
            print("0. Rester")
            shall_continue_game = input("Que voulez-vous faire ? (1/0) ").strip()


        #Cas ou on souhaite piocher == 1
        if shall_continue_game == "1":  # Tirer une carte
            deck.pick_a_card(my_player)
            my_player.show_hand()
            first_turn = False


        #Cas ou on souhaite spliter == 2
        elif (shall_continue_game == "2") and first_turn and bet <= my_player.money:  # Spliter le jeu
            my_player.split(deck)

            for index, hand in enumerate(my_player.hands):
                first_turn_split = True

                while hand.value < 21:

                    #Si on a split une paire d'as, on ne peut pas piocher, ou doubler.
                    if (my_player.hands[0].cards[0].value == 11) and (my_player.hands[1].cards[0].value == 11):
                        break

                    print(f"Actions possibles pour la main {hand.number}:")
                    print("1. Tirer une carte")

                    if first_turn_split and bet <= my_player.money:
                        print("2. Doubler")
                        print("0. Rester")
                        split_action_choice = input("Que voulez-vous faire ? (1/2/0) ").strip()
                    else:
                        print("0. Rester")
                        split_action_choice = input("Que voulez-vous faire ? (1/0) ").strip()

                    
                    if split_action_choice == "1":
                        deck.pick_a_card(my_player, index)
                        my_player.show_hand(index)
                        first_turn_split = False


                    elif (split_action_choice == "2") and first_turn_split and bet <= my_player.money:  # Doubler la mise
                        #On double la mise
                        my_player.doble_bet(index)
                        #On ne pick qu'une carte sur la main en question
                        deck.pick_a_card(my_player, index)
                        my_player.show_hand()
                        break
                    
                    elif split_action_choice == "0":
                        break

                    else:
                        print("Entrée invalide !")

            break
        

        #Cas ou on souhaite doubler == 3
        elif (shall_continue_game == "3") and first_turn and bet <= my_player.money:  # Doubler la mise
            #On double la mise
            my_player.doble_bet()
            #On ne pick qu'une carte
            deck.pick_a_card(my_player)
            my_player.show_hand()
            break


        #Cas ou on souhaite rester == 4
        elif shall_continue_game == "0":  # Rester
            break  

        else:
            print("Entrée invalide !")
    

    return blackjack



#Jeu du dealer. Juste piocher tant qu'on a en dessous de 17
def dealer_logic(deck, dealer, my_player):

    if dealer.hands[0].value == 21:
        print("BlackJack de la banque")
    if dealer.hands[0].value >= 17: #Permet d'afficher la valeur de la main du dealer, si il a une valeur suppérieur à 17 avec ses 2 premières cartes seulement
        dealer.show_hand(True)


    while dealer.hands[0].value < 17: #Tant que le dealer a une valeur de carte en dessous de 17, il doit piocher

        #Si le player s'est cramé sur sa ou ses mains, pas besoin que la banque pioche (vu qu'elle gagne)
        if all(hand.value > 21 for hand in my_player.hands): 
            dealer.show_hand(True)
            break
        deck.pick_a_card(dealer)
        dealer.show_hand()



#Conditions de victoire :
def win_condition_check(my_player, dealer):

    for index, hand in enumerate(my_player.hands):

        #Joueur à une valeur de main supérieur à 21 = PERDU
        if hand.value > 21:
            my_player.loose_game(index)
        #Si le joueur a un blackJack et le Croupier aussi = EGALITE
        elif (len(hand.cards) == 2 and hand.value == 21) and (len(dealer.hands[0].cards) == 2 and dealer.hands[0].value == 21):
            my_player.tie_game(index)
        #Si le joueur a un blackjack = GAGNE *2.5
        elif len(hand.cards) == 2 and hand.value == 21:
            my_player.blackjack(index)
        #Si le croupier a un blackjack = PERDU 
        elif len(dealer.hands[0].cards) == 2 and dealer.hands[0].value == 21:
            my_player.loose_game(index)
        #Croupier à une valeur de main supérieure à 21, et le joueur inférieure = GAGNE
        elif dealer.hands[0].value > 21:
            my_player.win_game(index)
        #Meme valeur pour le joueur et le croupier = EGALITE
        elif hand.value == dealer.hands[0].value:
            my_player.tie_game(index)
        #Le joueur a une meilleure valeur = GAGNE
        elif hand.value > dealer.hands[0].value:
            my_player.win_game(index)
        #Le joueur a une moins bonne valeur = PERDU
        elif hand.value < dealer.hands[0].value:
            my_player.loose_game(index)

    
    #Empty Hand
    my_player.empty_hand()
    dealer.empty_hand()



from blackjack.gameplay import setup_deck, draw_first_cards, win_condition_check, dealer_logic, player_actions
from blackjack.player import Human, Dealer 

#Créé et mélange le deck
deck = setup_deck()
deck.shuffle()
deck.show()

my_player = Human("Mickeal", 1000)
dealer = Dealer("Andrew")


#Tant que le joueur a de l'argent
while my_player.money > 0:

    #Savoir si le joueur veut continuer de faire du BlackJack
    # shall_continue_play = input("Continuer à jouer ? (1 = Yes / 0 = No) ").strip()
    # if shall_continue_play == "0": #No : Stop here
    #     break 


    
    #On distribue les cartes et on parie
    draw_first_cards(deck, my_player, dealer)


    #Jeu du joueur. Renvoie s'il a un blackJack
    blackjack = player_actions(deck,my_player)


    #Jouer le tour du dealer. Seulement si le joueur n'a pas de BalckJack
    if not blackjack:
        dealer_logic(deck, dealer)
    
    #Check conditions de victoire
    win_condition_check(my_player, dealer)






from blackjack.player import Human, Dealer 
from blackjack.setup import setup_deck



def draw_first_cards(deck, my_player, dealer):
    while True:
        try:
            bet = int(input("How many do you want to bet ? "))
            break
        except ValueError:
            print("Please enter a valid number")
    
    my_player.bet_money(bet)


    deck.pick_a_card(my_player)
    deck.pick_a_card(dealer)

    deck.pick_a_card(my_player)
    deck.pick_a_card(dealer)

    my_player.show_hand()
    dealer.show_hand()




deck = setup_deck()
deck.shuffle()
# deck.show()


my_player = Human("Mickeal", 1000)
dealer = Dealer("Andrew")


while my_player.money > 0:


    shall_continue = True
    draw_first_cards(deck, my_player, dealer)

    while my_player.total_hand_value < 21:

        
        shall_continue = input("Continue ? (1 = Yes / 0 = No) ").strip()

        if shall_continue == "1":
            deck.pick_a_card(my_player)
            my_player.show_hand()
        elif shall_continue == "0":
            break 
            


    break


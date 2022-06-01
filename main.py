from class_black import Deck, Hand, Chips

playing = True


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input(f"How many chips would you like to bet (chips amount: {player_chips.total})? "))

        except ValueError:
            print("Sorry, a bet must be an integer")

        else:
            if chips.bet > chips.total:
                print(f"Sorry, you do not have enough chips! You have {chips.total}")
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):

    global playing

    while True:
        x = input("Hit or Stand? Enter h or s ").lower()

        if x == "h":
            hit(deck,hand)

        elif x == "s":
            print("PLayer stands. Dealer's turn")
            playing = False

        else:
            print("Sorry, please neter h or s only!")
            continue

        break


def show_some(player, dealer):

    print("DEALERS HAND: ")
    print("'one card hidden'")
    print(dealer.cards[1])
    print("")
    print("PLAYERS HAND: ")
    for card in player.cards:
        print(card)
    print(f"Player Hand value: {player_hand.value}\n")

def show_all(player, dealer):

    print("DEALERS HAND: ")
    for card in dealer.cards:
        print(card)
    print(f"Dealer Hand value: {dealer_hand.value}")
    print("")
    print("PLAYERS HAND: ")
    for card in player.cards:
        print(card)
    print(f"Player Hand value: {player_hand.value}\n")

def player_busts(chips):
    print("BUST PLAYER!")
    chips.lose_bet()


def player_win(chips):
    print("PLAYER WINS!")
    chips.win_bet()


def dealer_busts(chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()


def dealer_win(chips):
    print("DEALER WINS!")
    chips.lose_bet()


def push():
    print("Dealer and player tie! PUSH")


while True:

    print("WELCOME TO BLACKJACK!")
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_win(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_win(player_chips)
        else:
            push()

        print(f"Player total chips are at {player_chips.total}")

        new_game = input("Would you like to play another game? (y/n): ").lower()

        if new_game == "y":
            playing = True
            continue
        else:
            print("Thank you for playing!")
            break

# Blackjack game

import p1_random as p1  # Importing the random module

rng = p1.P1Random()  # P1 random variable

game_num = 0
player_win = 0
dealer_win = 0
game_ties = 0
in_progress = True

while in_progress:
    # New game loop
    game_num += 1
    print(f"START GAME #{game_num}")
    card = rng.next_int(13) + 1  # Generates [0,12] + 1

    if card == 1:
        print("\nYour card is a ACE!")
    elif 2 <= card <= 10:
        print(f"\nYour card is a {card}!")
    elif card == 11:
        print("\nYour card is a JACK!")
    elif card == 12:
        print("\nYour card is a QUEEN!")
    elif card == 13:
        print("\nYour card is a KING!")

    if card <= 10:
        hand = card
    else:
        hand = 10

    print(f"Your hand is: {hand}")

    while True:
        choice = input("\n1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n\nChoose an option: ")

        if choice == "1":
            card = rng.next_int(13) + 1

            if card == 1:
                hand += 1
                print("\nYour card is a ACE!")
                print(f"Your hand is: {hand}")

            elif 2 <= card <= 10:
                hand += card
                print(f"\nYour card is a {card}!")
                print(f"Your hand is: {hand}")

            elif card == 11:
                hand += 10
                print("\nYour card is a JACK!")
                print(f"Your hand is: {hand}")

            elif card == 12:
                hand += 10
                print("\nYour card is a QUEEN!")
                print(f"Your hand is: {hand}")

            elif card == 13:
                hand += 10
                print("\nYour card is a KING!")
                print(f"Your hand is: {hand}")

            if hand == 21:
                player_win += 1
                print("\nBLACKJACK! You win!\n")
                break

            elif hand > 21:
                dealer_win += 1
                print("\nYou exceeded 21! You lose.\n")
                break


        elif choice == "2":
            # Dealer's draw
            dealer_hand = rng.next_int(11) + 16
            print(f"\nDealer's hand: {dealer_hand}")
            print(f"Your hand is: {hand}")

            if dealer_hand == 21:
                dealer_win += 1
                print("\nDealer wins!\n")
                break

            elif dealer_hand > 21:
                player_win += 1
                print("\nYou win!\n")
                break

            elif hand == dealer_hand:
                print("\nIt's a tie! No one wins!\n")
                game_ties += 1
                break

            elif hand > dealer_hand:
                player_win += 1
                print("\nYou win!\n")
                break

            elif dealer_hand > hand:
                dealer_win += 1
                print("\nDealer wins!\n")
                break

        elif choice == "3":
            print(f"Number of Player wins: {player_win}")
            print(f"Number of Dealer wins: {dealer_win}")
            print(f"Number of tie games: {game_ties}")
            print(f"Total # of games played is: {game_num - 1}")
            percentage = (player_win / (game_num - 1)) * 100
            print(f"Percentage of Player wins: {percentage:.1f}%")


        elif choice == "4":
            in_progress = False
            break

        else:
            print("Invalid input!\n\nPlease enter an integer value between 1 and 4.")

# -*- coding: utf-8 -*-
"""Diamond_CardGame.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AJhPsar6BncSQqauNXWIhvYd7RAwtC3C

Each player gets a suit of cards other than the diamond suit.
The diamond cards are then shuffled and put on auction one by one.
All the players must bid with one of their own cards face down.
The banker gives the diamond card to the highest bid, i.e. the bid with the most points.
2<3<4<5<6<7<8<9<T<J<Q<K<A
The winning player gets the points of the diamond card to their column in the table. If there are multiple players that have the highest bid with the same card, the points from the diamond card are divided equally among them.
The player with the most points wins at the end of the game.The game is played till all the cards from diamond suit are bid.
"""

#random computer bid
import random

def initialize_deck():
    return list(range(2, 15)) * 4  # Each card value is repeated 4 times

def play_game():
    deck = initialize_deck()
    random.shuffle(deck)
    player_score = 0
    computer_score = 0
    rounds = 13  # Number of rounds

    player_used_cards = set()   # To track cards used by the player
    computer_used_cards = set() # To track cards used by the computer

    for round_num in range(rounds):
        # Step 3: Display diamond card
        diamond_card = deck.pop()
        print("Diamond card for bidding:", diamond_card)

        # Step 4: Player bidding
        valid_player_bid = False
        while not valid_player_bid:
            player_bid = int(input("Enter your bid (2-14): "))
            if player_bid in player_used_cards:
                print("You have already used this card. Please bid another card.")
            else:
                valid_player_bid = True
                player_used_cards.add(player_bid)

        # Step 5: Computer bidding (hidden)
        valid_computer_bid = False
        while not valid_computer_bid:
            computer_bid = random.randint(2, 14)
            if computer_bid not in computer_used_cards:
                valid_computer_bid = True
                computer_used_cards.add(computer_bid)

        # Step 6: Determine winner
        if player_bid > computer_bid:
            print("You win this round!")
            player_score += diamond_card
        elif player_bid < computer_bid:
            print("Computer wins this round!")
            computer_score += diamond_card
        else:
            print("It's a tie for this round!")

    # Step 8: End game
    print("\nGame Over!")
    print("Your final score:", player_score)
    print("Computer's final score:", computer_score)
    if player_score > computer_score:
        print("Congratulations! You win!")
    elif player_score < computer_score:
        print("Computer wins!")
    else:
        print("It's a tie!")

# Main function to start the game
if __name__ == "__main__":
    play_game()

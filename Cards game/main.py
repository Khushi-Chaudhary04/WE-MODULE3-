from gameplay import Gameplay, card_value
from strategies import smart_bid  # Import the chosen bidding strategy (smart_bid in this case)
from ui import display_message, display_decks, get_user_bid, display_round_results, display_final_scores

def main():
  game = Gameplay()
  ui = UI()

  ui.display_message("Welcome to the Diamond Card Game!")
  game.initialize_decks()

  for round_number in range(1, 14):
    ui.display_message(f"\nRound {round_number}:")
    diamond_card = random.choice(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'])
    ui.display_message(f"Diamond card for bidding: {diamond_card}")

    user_deck = game.get_user_deck()
    comp_deck = game.get_comp_deck()

    display_decks(user_deck, comp_deck)

    user_bid = get_user_bid(user_deck)
    comp_bid = smart_bid(comp_deck, card_value(diamond_card))

    user_deck.remove(user_bid)
    comp_deck.remove(comp_bid)

    winner = game.play_round(user_bid, comp_bid, diamond_card)
    display_round_results(user_bid, comp_bid, winner)

  user_points = game.get_user_points()
  comp_points = game.get_comp_points()
  display_final_scores(user_points, comp_points)


if __name__ == "__main__":
  main()

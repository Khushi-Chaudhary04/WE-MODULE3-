def display_message(message):
  print(message)

def display_decks(user_deck, comp_deck):
  print("Your deck:", user_deck)
  print("Computer's deck:", comp_deck)

def get_user_bid(user_deck):
  user_bid = input("Enter your bid (choose a card from your deck): ").upper()
  while user_bid not in user_deck:
    user_bid = input("Invalid bid. Enter your bid again: ").upper()
  return user_bid

def display_round_results(user_bid, comp_bid, winner):
  print(f"User bid: {user_bid}, Computer bid: {comp_bid}")
  print(f"Winner of the round: {winner}")

def display_final_scores(user_points, comp_points):
  print("\nFinal Scores:")
  print(f"User points: {user_points}, Computer points: {comp_points}")

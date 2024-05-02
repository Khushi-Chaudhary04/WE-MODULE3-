def random_bid(deck):
  return random.choice(deck)

def smart_bid(deck, diamond_value):
  # Choose a bid based on the value of the diamond card
  if diamond_value < 7:  # If the diamond card is small
    # Bid a smaller card
    valid_bids = [card for card in deck if card_value(card) < 7]
    return random.choice(valid_bids) if valid_bids else random.choice(deck)
  else:
    # Bid a bigger card
    valid_bids = [card for card in deck if card_value(card) > 7]
    return random.choice(valid_bids) if valid_bids else random.choice(deck)

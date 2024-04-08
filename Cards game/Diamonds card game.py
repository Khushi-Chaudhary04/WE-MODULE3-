import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set card dimensions
CARD_WIDTH = 50
CARD_HEIGHT = 80

# Set font
FONT = pygame.font.Font(None, 36)

# Dictionary mapping cards to their values
CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

# Function to generate a unique random diamond card
def generate_diamond_card(remaining_cards, used_diamonds):
    while True:
        card = random.choice(remaining_cards)
        if card not in used_diamonds:
            used_diamonds.append(card)
            return card

# Function to display text on the screen
def display_text(screen, text, position, color):
    text_surface = FONT.render(text, True, color)
    screen.blit(text_surface, position)

# Load card images
def load_card_images():
    cards = {}
    for card in ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']:
        image_path = os.path.join('cards', f'{card}.png')  # Assuming card images are in a folder named 'cards'
        image = pygame.image.load(image_path).convert_alpha()
        # Resize the image to desired dimensions
        image = pygame.transform.scale(image, (int(75), int(150)))
        cards[card] = image
    return cards


# Main function to run the game
def main():
    # Initialize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Diamonds Game")

    # Load card images
    card_images = load_card_images()

    # Initialize game variables
    diamond_cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    player_deck = diamond_cards.copy()
    computer_deck = diamond_cards.copy()
    player_score = 0
    computer_score = 0
    round_number = 1
    used_diamonds = []

    running = True
    # Main game loop
    while diamond_cards:
        if not(diamond_cards):
            break
        current_diamond = generate_diamond_card(diamond_cards, used_diamonds)
        # Clear the screen
        screen.fill(WHITE)

        # Display the diamond card in the center of the screen
        screen.blit(card_images[current_diamond], (SCREEN_WIDTH // 2 - CARD_WIDTH // 2, SCREEN_HEIGHT // 2))

        # Display text asking for player's bid
        display_text(screen, "Choose a card to bid:", (10, SCREEN_HEIGHT - 120), BLACK)

        # Draw the player's deck
        for i, card in enumerate(player_deck):
            screen.blit(card_images[card], (i * CARD_WIDTH, SCREEN_HEIGHT - CARD_HEIGHT))

        # Display player and computer scores
        display_text(screen, f"Player Score: {player_score}", (10, 10), BLACK)
        display_text(screen, f"Computer Score: {computer_score}", (10, 50), BLACK)
        pygame.display.flip()

        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if SCREEN_HEIGHT - CARD_HEIGHT <= mouse_y <= SCREEN_HEIGHT:
                        selected_card_index = (mouse_x // CARD_WIDTH) % len(player_deck)
                        selected_card = player_deck.pop(selected_card_index)

                        # Computer's bid
                        computer_card = generate_diamond_card(computer_deck, used_diamonds)

                        # Determine winner of the round and update scores
                        if CARD_VALUES[computer_card[0]] > CARD_VALUES[selected_card[0]]:
                            computer_score += CARD_VALUES[current_diamond]
                            text = "Computer Won this round"
                        elif CARD_VALUES[computer_card[0]] == CARD_VALUES[selected_card[0]]:
                            computer_score += CARD_VALUES[current_diamond]//2
                            player_score += CARD_VALUES[current_diamond]//2
                            text = "This round is a tie"
                        else:
                            player_score += CARD_VALUES[current_diamond]
                            text = "You won this round"

                        # Display computer's bid and round result
                        display_text(screen, f"Computer's bid: {computer_card}   You bid: {selected_card}", (10, SCREEN_HEIGHT - 200), BLACK)
                        display_text(screen, text, (10, SCREEN_HEIGHT - 250), BLACK)
                        pygame.display.flip()
                        pygame.time.delay(3000)
                break

        # Update round number
        round_number += 1

    # Display final scores and winner
    screen.fill(WHITE)
    display_text(screen, f"Player Score: {player_score}", (10, 10), BLACK)
    display_text(screen, f"Computer Score: {computer_score}", (10, 50), BLACK)

    if player_score > computer_score:
        text = "You won!"
    elif player_score == computer_score:
        text = "It's a tie!"
    else:
        text = "Computer won!"
    
    display_text(screen, text, (300, 300), BLACK)

    pygame.display.flip()
    # Quit Pygame

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:    
            pygame.quit()
            break

if __name__ == "__main__":
    main()

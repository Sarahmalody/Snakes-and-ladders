import pygame
import random

# Game constants
WIDTH = 600
HEIGHT = 600
NUM_ROWS = 10
NUM_COLS = 10
SQUARE_SIZE = 60
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Snakes and ladders positions
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Load player images
player1_image = pygame.image.load("player1.png")
player2_image = pygame.image.load("player2.png")

# Resize player images
player1_image = pygame.transform.scale(player1_image, (SQUARE_SIZE, SQUARE_SIZE))
player2_image = pygame.transform.scale(player2_image, (SQUARE_SIZE, SQUARE_SIZE))

# Function to draw the game board
def draw_board():
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)

# Function to draw the player tokens
def draw_players(player1_position, player2_position):
    player1_row, player1_col = divmod(player1_position - 1, NUM_COLS)
    player2_row, player2_col = divmod(player2_position - 1, NUM_COLS)
    
    player1_x = player1_col * SQUARE_SIZE
    player1_y = player1_row * SQUARE_SIZE
    player2_x = player2_col * SQUARE_SIZE
    player2_y = player2_row * SQUARE_SIZE
    
    screen.blit(player1_image, (player1_x, player1_y))
    screen.blit(player2_image, (player2_x, player2_y))

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to check for snakes and ladders
def check_snake_or_ladder(position):
    if position in snakes:
        print("Oops! You got bitten by a snake. Go back to position", snakes[position])
        return snakes[position]
    elif position in ladders:
        print("Hooray! You found a ladder. Climb up to position", ladders[position])
        return ladders[position]
    
    return position

# Function to play the game
def play_game():
    player1_position = 1
    player2_position = 1
    current_player = 1
    
    running = True
    while running:
        clock.tick
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Roll the dice
        dice = roll_dice()
        print("Player", current_player, "rolled a", dice)
        
        if current_player == 1:
            player1_position += dice
            player1_position = check_snake_or_ladder(player1_position)
            
            if player1_position > 100:
                player1_position = 100
            
            if player1_position == 100:
                print("Player 1 wins!")
                running = False
            
            current_player = 2
        else:
            player2_position += dice
            player2_position = check_snake_or_ladder(player2_position)
            
            if player2_position > 100:
                player2_position = 100
            
            if player2_position == 100:
                print("Player 2 wins!")
                running = False
            
            current_player = 1
        
        # Update the display
        screen.fill(WHITE)
        draw_board()
        draw_players(player1_position, player2_position)
        pygame.display.flip()

# Start the game
print("Welcome to Snakes and Ladders!")
play_game()

# Quit the game
pygame.quit()

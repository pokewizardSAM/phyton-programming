import pygame
import random

# Initialize the game engine
pygame.init()

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set the screen dimensions
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Pygame Game")

# Set the font for displaying score
font = pygame.font.Font(None, 30)

# Define the Player object extending pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

# Define the Enemy object extending pygame.sprite.Sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(SCREEN_HEIGHT - self.rect.height)

    def update(self):
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(SCREEN_HEIGHT - self.rect.height)

# Create the sprite groups
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# Create the Player object and add it to the player group
player = Player()
player_group.add(player)

# Create 20 Enemy objects and add them to the enemy group
for i in range(20):
    enemy = Enemy()
    enemy_group.add(enemy)

# Set the game clock
clock = pygame.time.Clock()

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update the player and enemy groups
    player_group.update()
    enemy_group.update()

    # Check for collisions between the player and enemy groups
    hit_list = pygame.sprite.spritecollide(player, enemy_group, True)

    # Add to

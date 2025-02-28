import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
BIRD_X, BIRD_Y = 50, HEIGHT // 2
BIRD_SIZE = 30
GRAVITY = 1
JUMP = -12
PIPE_WIDTH = 60
PIPE_GAP = 150
PIPE_SPEED = 5
FPS = 30
SPAWN_INTERVAL = 1200  # Milliseconds between new pipe pairs

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

# Bird properties
bird = pygame.Rect(BIRD_X, BIRD_Y, BIRD_SIZE, BIRD_SIZE)
velocity = 0

# Pipe properties
pipes = []
def create_pipe():
    height = random.randint(100, 400)
    pipes.append(pygame.Rect(WIDTH, 0, PIPE_WIDTH, height))
    pipes.append(pygame.Rect(WIDTH, height + PIPE_GAP, PIPE_WIDTH, HEIGHT - height - PIPE_GAP))

# Initial pipe creation
create_pipe()
last_spawn_time = pygame.time.get_ticks()

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            velocity = JUMP
    
    # Bird physics
    velocity += GRAVITY
    bird.y += velocity
    
    # Check for collisions with ground or ceiling
    if bird.y + BIRD_SIZE > HEIGHT or bird.y < 0:
        running = False
    
    # Move pipes
    for pipe in pipes:
        pipe.x -= PIPE_SPEED
    
    # Check for pipe collisions
    for pipe in pipes:
        if bird.colliderect(pipe):
            running = False
    
    # Remove off-screen pipes
    if pipes and pipes[0].x + PIPE_WIDTH < 0:
        pipes.pop(0)
        pipes.pop(0)
    
    # Spawn new pipes at intervals
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time > SPAWN_INTERVAL:
        create_pipe()
        last_spawn_time = current_time
    
    # Draw all elements
    pygame.draw.rect(screen, BLUE, bird)
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
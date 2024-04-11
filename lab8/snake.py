import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == pygame.K_UP:
            new_head = (head_x, head_y - 1)
        elif self.direction == pygame.K_DOWN:
            new_head = (head_x, head_y + 1)
        elif self.direction == pygame.K_LEFT:
            new_head = (head_x - 1, head_y)
        elif self.direction == pygame.K_RIGHT:
            new_head = (head_x + 1, head_y)

        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def grow_snake(self):
        self.grow = True

    def check_collision(self):
        head = self.body[0]
        if head in self.body[1:] or head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
            return True
        return False

    def change_direction(self, new_direction):
        if new_direction == pygame.K_UP and self.direction != pygame.K_DOWN:
            self.direction = new_direction
        elif new_direction == pygame.K_DOWN and self.direction != pygame.K_UP:
            self.direction = new_direction
        elif new_direction == pygame.K_LEFT and self.direction != pygame.K_RIGHT:
            self.direction = new_direction
        elif new_direction == pygame.K_RIGHT and self.direction != pygame.K_LEFT:
            self.direction = new_direction

# Food class
class Food:
    def __init__(self):
        self.position = self.generate_food_position()

    def generate_food_position(self):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake.body:
                return (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Initialize game variables
snake = Snake()
food = Food()
score = 0
level = 1
speed = FPS

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                snake.change_direction(event.key)

    # Move snake
    snake.move()

    # Check for collisions
    if snake.check_collision():
        running = False

    # Check if snake eats food
    if snake.body[0] == food.position:
        snake.grow_snake()
        score += 1
        if score % 3 == 0:  # Increase level every 3 foods eaten
            level += 1
            speed += 2  # Increase speed on level up
            pygame.display.set_caption(f"Snake Game - Level {level}")

        food.position = food.generate_food_position()

    # Draw everything
    screen.fill(BLACK)
    for segment in snake.body:
        pygame.draw.rect(screen, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    food.draw(screen)

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()

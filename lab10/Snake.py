import pygame
import time
import random
import psycopg2

# Connect to the database
conn = psycopg2.connect(host="localhost", dbname="snake", user="postgres", password="qazqaz", port=5432)
cur = conn.cursor()

# Create table if not exists
cur.execute("""CREATE TABLE IF NOT EXISTS snakegame (
    username VARCHAR(255),
    score INT,
    level INT 
);
""")
conn.commit()

# Initialize pygame
pygame.init()

# Window size
window_x = 400
window_y = 280

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Initialize game window
pygame.display.set_caption('SnakeGame')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS controller
fps = pygame.time.Clock()

# Default snake position and direction
snake_position = [100, 50]
direction = 'RIGHT'

# Default snake body
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Default fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]

# Game settings
snake_speed = 10
level = 1
score = 0
score_current = 0
fruit_spawn = True

# Function to display score
def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

# Function to display level
def show_level(color, font, size):
    level_font = pygame.font.SysFont(font, size)
    level_surface = level_font.render(str(level), True, color)
    level_rect = level_surface.get_rect()
    game_window.blit(level_surface, (100, 0))

# Game over function
def game_over():
    my_font = pygame.font.SysFont('Verdana', 50)
    game_over_surface = my_font.render('Score: ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)

    # Insert username, score, and level into the database
    cur.execute("INSERT INTO snakegame (username, score, level) VALUES (%s, %s, %s)", (username, score, level))
    conn.commit()

    pygame.quit()
    quit()

# Function to handle user input and update game state
def handle_input_and_update():
    global direction, snake_position, snake_body, score, level, snake_speed, fruit_spawn, fruit_position, score_current

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Move the snake
    if direction == 'UP':
        snake_position[1] -= 10
    elif direction == 'DOWN':
        snake_position[1] += 10
    elif direction == 'LEFT':
        snake_position[0] -= 10
    elif direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    # Condition for levels
    if score == score_current + 30 and snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        snake_speed += 5
        score_current = score
        level += 1

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]

    fruit_spawn = True

# Get username and show last score and level if exists
def get_username():
    username = input("Enter your username: ")
    cur.execute("SELECT * FROM snakegame WHERE username = %s", (username,))
    user_data = cur.fetchone()
    if user_data:
        print("Welcome back, {}!".format(username))
        print("Your last score was: {}".format(user_data[1]))
        print("Your last level was: {}".format(user_data[2]))
    else:
        print("New user detected. Let's start a new game!")
    return username

# Main Function
username = get_username()

# Main game loop
while True:
    handle_input_and_update()

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Display game elements
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    show_score(white, 'Verdana', 20)
    show_level('Magenta', 'Verdana', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second / Refresh Rate
    fps.tick(snake_speed)

# Close the cursor and connection outside the loop
cur.close()
conn.close()

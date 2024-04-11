import pygame
import threading
import random
import time
 
snake_speed = 10
 
# Window size
window_x = 400
window_y = 280

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
 
# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('SnakeGame')
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()
 
# defining snake default position
snake_position = [100, 50]
 
# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]

fruit_position1 = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]

fruit_position2 = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True
fruit_spawn1 = True
fruit_spawn2 = True
# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction
# initial level
level = 1
# initial score
score = 0
# current score
score_current = 0
# displaying Score function
def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)
# displaying Level function
def show_level(color, font, size):
    level_font = pygame.font.SysFont(font, size)
    level_surface = level_font.render(str(level), True, color)
    level_rect = level_surface.get_rect()
    game_window.blit(level_surface, (100, 0))
# game over function
def game_over():
    my_font = pygame.font.SysFont('Verdana', 50)
    game_over_surface = my_font.render('Score: ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()
#Timer for fruit:
fruit_timer = time.time()
fruit_disappear_delay = 3
# Main Function
while True:
     
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    # If two keys pressed simultaneously
    # we don't want snake to move into two 
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    if snake_position[0] == fruit_position1[0] and snake_position[1] == fruit_position1[1]:
        score += 30
        fruit_spawn1 = False
    elif fruit_position[0] == fruit_position1[0] and fruit_position[1] == fruit_position1[1]:
        fruit_spawn1 = False
    if snake_position[0] == fruit_position2[0] and snake_position[1] == fruit_position2[1]:
        score += 50
        fruit_spawn2 = False
    elif fruit_position[0] == fruit_position2[0] and fruit_position[1] == fruit_position2[1]:
        fruit_spawn2 = False   
    elif fruit_position1[0] == fruit_position2[0] and fruit_position1[1] == fruit_position2[1]:
        fruit_spawn2 = False
    else:
        snake_body.pop()
    # Condition for levels
    if score - score_current == 100 and snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        snake_speed += 3
        score_current = score
        level += 1
    if score - score_current >= 100 and snake_position[0] == fruit_position1[0] and snake_position[1] == fruit_position1[1]:
        snake_speed += 3
        score_current = score
        level += 1
    if score - score_current >= 100 and snake_position[0] == fruit_position2[0] and snake_position[1] == fruit_position2[1]:
        snake_speed += 3
        score_current = score
        level += 1
    # Condition for disappearing fruit:
    current_time = time.time()
    if current_time - fruit_timer >= fruit_disappear_delay:
        # Time for delete fruit:
        fruit_position2 = [-10, -10]  # Move fruit beyond of display
        fruit_spawn2 = False  
        fruit_timer = current_time
    #x = threading.Timer(2, fruit_spawn2, args= False)
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
            random.randrange(1, (window_y//10)) * 10]
    if not fruit_spawn1:    
        fruit_position1 = [random.randrange(1, (window_x//10)) * 10, 
            random.randrange(1, (window_y//10)) * 10]
    if not fruit_spawn2:    
        fruit_position2 = [random.randrange(1, (window_x//10)) * 10, 
            random.randrange(1, (window_y//10)) * 10]
        fruit_spawn2 = False
    
    fruit_spawn = True
    fruit_spawn1 = True
    fruit_spawn2 = True
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
    pygame.draw.rect(game_window, 'red', pygame.Rect(
        fruit_position1[0], fruit_position1[1], 10, 10))
    pygame.draw.rect(game_window, 'orange', pygame.Rect(
        fruit_position2[0], fruit_position2[1], 10, 10))
        
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    # displaying score continuously
    show_score(white, 'Verdana', 20)
    show_level('Magenta', 'Verdana', 20)
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
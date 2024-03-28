import pygame
import datetime

pygame.init()

window_width, window_height = 1000, 800
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mickey Mouse Clock")

mickey_image = pygame.image.load('img/mainclock.png')
right_hand_image = pygame.image.load('img/leftarm.png')
left_hand_image = pygame.image.load('img/rightarm.png')

current_time = datetime.datetime.now()

clock_radius = 200
clock_center = (window_width // 2, window_height // 2)

def calculate_rotation_angle(current_time, hand_length, is_minutes_hand):
    if is_minutes_hand:
        time_value = current_time.minute
        max_value = 60
    else:
        time_value = current_time.second
        max_value = 60
    
    angle = 360 * (time_value / max_value)
    return angle

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = datetime.datetime.now()

    screen.fill((255, 255, 255))

    mickey_rect = mickey_image.get_rect(center=clock_center)
    screen.blit(mickey_image, mickey_rect)

    minutes_angle = calculate_rotation_angle(current_time, clock_radius, is_minutes_hand=True)
    seconds_angle = calculate_rotation_angle(current_time, clock_radius, is_minutes_hand=False)

    rotated_right_hand = pygame.transform.rotate(right_hand_image, -minutes_angle)
    right_hand_rect = rotated_right_hand.get_rect(center=clock_center)
    screen.blit(rotated_right_hand, right_hand_rect)

    rotated_left_hand = pygame.transform.rotate(left_hand_image, -seconds_angle)
    left_hand_rect = rotated_left_hand.get_rect(center=clock_center)
    screen.blit(rotated_left_hand, left_hand_rect)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()

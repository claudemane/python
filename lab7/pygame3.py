import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
done = False
x = 200
y = 200

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 20
    if pressed[pygame.K_DOWN]: y += 20
    if pressed[pygame.K_LEFT]: x -= 20
    if pressed[pygame.K_RIGHT]: x += 20

    if x + 25 > 400:
        x = 400 - 25
    elif x - 25 < 0:
        x = 25
    if y + 25 > 400:
        y = 400 - 25
    elif y - 25 < 0:
        y = 25

    screen.fill((255, 255, 255))
    color = (255, 0, 0)
    pygame.draw.circle(screen, color, (x, y), 25)

    pygame.display.flip()
    clock.tick(60)

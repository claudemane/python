import pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    tool = 'line'
    points = []
    POS = (-1,-1)
    color = (0,0,255)
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                    color = (255,0,0)
                elif event.key == pygame.K_g:
                    mode = 'green'
                    color = (0,255,0)
                elif event.key == pygame.K_b:
                    mode = 'blue'
                    color = (0,0,255)
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key == pygame.K_c:
                    tool = 'circle'
                elif event.key == pygame.K_t:
                    tool = 'rectangle'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tool == 'line':
                    if event.button == 1:
                        radius = min(200, radius + 1)
                    elif event.button == 3:
                        radius = max(1, radius - 1)
                elif tool == 'circle':
                    if event.button == 1:
                        pygame.draw.circle(screen, color, pygame.mouse.get_pos(), 50)
                elif tool == 'rectangle':
                    if event.button == 1:
                        POS = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if tool == 'rectangle':
                    if event.button == 1:
                        pygame.draw.rect(screen, color, (min(pygame.mouse.get_pos()[0],POS[0]),min(POS[1],pygame.mouse.get_pos()[1]),abs(pygame.mouse.get_pos()[0]-POS[0]),abs(pygame.mouse.get_pos()[1]-POS[1])))
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points = points + [position]
                points = points[-256:]
        if tool == 'line':
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
                i += 1
        elif tool == 'eraser':
            if pygame.mouse.get_pressed()[0]:
                    pygame.draw.circle(screen, (0,0,0), pygame.mouse.get_pos(), 50)
        pygame.display.flip()
        clock.tick(60)
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)
main()
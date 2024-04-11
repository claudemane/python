import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    radius = 15
    mode = 'blue'
    tool = 'line'
    points = []
    POS = (-1, -1)
    color = (0, 0, 255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    mode = 'green'
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    mode = 'blue'
                    color = (0, 0, 255)
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key == pygame.K_l:
                    tool = 'line'
                elif event.key == pygame.K_t:
                    tool = 'rectangle'
                elif event.key == pygame.K_s:
                    tool = 'square'
                elif event.key == pygame.K_q:
                    tool = 'triangle'
                elif event.key == pygame.K_i:
                    tool = 'equilateral_triangle'
                elif event.key == pygame.K_d:
                    tool = 'rhombus'
                elif event.key == pygame.K_c: 
                    tool = 'circle'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tool == 'line':
                    if event.button == 1:
                        radius = min(200, radius + 1)
                    elif event.button == 3:
                        radius = max(1, radius - 1)
                elif tool == 'rectangle':
                    if event.button == 1:
                        POS = pygame.mouse.get_pos()
                elif tool == 'square':
                    if event.button == 1:
                        POS = pygame.mouse.get_pos()
                elif tool == 'triangle':
                    if event.button == 1:
                        POS = pygame.mouse.get_pos()
                elif tool == 'equilateral_triangle':
                    if event.button == 1:
                        POS = pygame.mouse.get_pos()
                elif tool == 'rhombus':
                    if event.button == 1:
                        POS = pygame.mouse.get_pos()
                elif tool == 'circle':  # Handle circle tool
                    if event.button == 1:
                        POS = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if tool == 'rectangle':
                    if event.button == 1:
                        pygame.draw.rect(screen, color, (min(pygame.mouse.get_pos()[0], POS[0]),
                                                        min(POS[1], pygame.mouse.get_pos()[1]),
                                                        abs(pygame.mouse.get_pos()[0] - POS[0]),
                                                        abs(pygame.mouse.get_pos()[1] - POS[1])))
                elif tool == 'square':
                    if event.button == 1:
                        side_length = min(abs(POS[0] - pygame.mouse.get_pos()[0]),
                                          abs(POS[1] - pygame.mouse.get_pos()[1]))
                        square_rect = pygame.Rect(POS[0], POS[1], side_length, side_length)
                        pygame.draw.rect(screen, color, square_rect)
                elif tool == 'triangle':
                    if event.button == 1:
                        pos2 = pygame.mouse.get_pos()
                        pygame.draw.polygon(screen, color, [POS, pos2, (POS[0], pos2[1])])
                elif tool == 'equilateral_triangle':
                    if event.button == 1:
                        side_length = math.sqrt(3) / 2 * abs(pygame.mouse.get_pos()[0] - POS[0])
                        height = side_length * math.sqrt(3) / 2
                        pos2 = (POS[0] + side_length, POS[1])
                        pos3 = ((POS[0] + pos2[0]) / 2, POS[1] - height)
                        pygame.draw.polygon(screen, color, [POS, pos2, pos3])
                elif tool == 'rhombus':
                    if event.button == 1:
                        pos2 = pygame.mouse.get_pos()
                        d = abs(pos2[0] - POS[0])
                        pygame.draw.polygon(screen, color, [(POS[0] - d, POS[1]), (POS[0], POS[1] - d),
                                                             (POS[0] + d, POS[1]), (POS[0], POS[1] + d)])
                elif tool == 'circle':  # Handle circle tool
                    if event.button == 1:
                        pygame.draw.circle(screen, color, POS, max(abs(POS[0] - pygame.mouse.get_pos()[0]),
                                                                   abs(POS[1] - pygame.mouse.get_pos()[1])))
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
                pygame.draw.circle(screen, (0, 0, 0), pygame.mouse.get_pos(), 50)

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
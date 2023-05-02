# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.

import pygame
import math
pygame.init()
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My Simple Picture")
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
pentagon_center = (100, 100)
pentagon_size = 50
pentagon_points = []
for i in range(5):
    angle = math.radians(90 + i * 72)
    x = pentagon_center[0] + pentagon_size * math.cos(angle)
    y = pentagon_center[1] + pentagon_size * math.sin(angle)
    pentagon_points.append((x, y))
pygame.draw.polygon(screen, BLUE, pentagon_points)
octagon_center = (250, 100)
octagon_size = 50
octagon_points = []
for i in range(8):
    angle = math.radians(45 + i * 45)
    x = octagon_center[0] + octagon_size * math.cos(angle)
    y = octagon_center[1] + octagon_size * math.sin(angle)
    octagon_points.append((x, y))
pygame.draw.polygon(screen, GREEN, octagon_points)
rect_x = 350
rect_y = 50
rect_width = 100
rect_height = 75
pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))
circle_center = (100, 250)
circle_radius = 50
pygame.draw.circle(screen, YELLOW, circle_center, circle_radius)
square_x = 250
square_y = 200
square_size = 75
pygame.draw.rect(screen, PURPLE, (square_x, square_y, square_size, square_size))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

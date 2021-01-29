import pygame
import random
import time

pygame.init()

clock = pygame.time.Clock()
isjump = False
jump_count = 10

#Main arena dimensions and program name
arena_x = 1280
arena_y = 680

arena = pygame.display.set_mode((arena_x, arena_y))
pygame.display.set_caption("Agrisimo Snake game (Game#2)")

#Object and arena colors
background_color = (0,0,0)
snake_color = (255, 0, 0)
fruit_color = (57, 255, 20)

#Sizes of objects:
width_snake = 40
height_snake = 40

radius_fruit = 20
width_fruit = 10

#Coordinates of objects:
x_snake = 0
y_snake = arena_y - height_snake

x_fruit = random.randint(radius_fruit * 2, arena_x - radius_fruit * 2)
y_fruit = random.randint(radius_fruit * 2, arena_y - radius_fruit * 2)

#Movement step size of objects:
step_size_snake = 5
step_size_fruit = 4

run_program_status = True

#Main While loop
while run_program_status:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_program_status = False
    keys = pygame.key.get_pressed()


# Snake Controls
    if keys[pygame.K_RIGHT] and x_snake <= (arena_x - step_size_snake - width_snake):
        x_snake = x_snake + step_size_snake
    if keys[pygame.K_LEFT] and x_snake >= step_size_snake:
        x_snake = x_snake - step_size_snake
    if not (isjump):
        if keys[pygame.K_UP] and y_snake >= step_size_snake:
            y_snake = y_snake - step_size_snake
        if keys[pygame.K_DOWN] and y_snake <= (arena_y - step_size_snake - width_snake):
            y_snake = y_snake + step_size_snake
        if keys[pygame.K_SPACE]:
            isjump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y_snake = y_snake - (jump_count ** 2) * 0.5 * neg
            jump_count = jump_count - 1
        else:
            isjump = False
            jump_count = 10

# Fruit Controls
    if keys[pygame.K_a]:
        x_fruit = x_fruit - step_size_fruit
    if keys[pygame.K_d]:
        x_fruit = x_fruit + step_size_fruit
    if keys[pygame.K_w]:
        y_fruit = y_fruit - step_size_fruit
    if keys[pygame.K_s]:
        y_fruit = y_fruit + step_size_fruit

    #Character. Shape, on which surface, color, coordinates, width and height)
    arena.fill((background_color))
    pygame.draw.rect(arena, snake_color, (x_snake, y_snake, width_snake, height_snake))
    pygame.draw.circle(arena, fruit_color, center=(x_fruit, y_fruit), radius=radius_fruit, width=width_fruit)
    pygame.display.update()

#Fruit eating interraction

pygame.quit()
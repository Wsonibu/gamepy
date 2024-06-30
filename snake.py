import pygame
import random

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
map_width, map_height = 600, 400
info_panel_width = 200
width = map_width + info_panel_width  # Tổng chiều rộng của cửa sổ
height = map_height  # Chiều cao của cửa sổ
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Màu sắc
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Kích thước khối
block_size = 20
# Tốc độ mặc định của rắn
snake_speed = 15

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 35)

def message(msg, color):
    mesg = font.render(msg, True, color)
    window.blit(mesg, [map_width / 6, map_height / 3])

def show_score(score):
    value = font.render("Score: " + str(score), True, white)
    window.blit(value, [map_width + 10, 10])

def draw_buttons():
    pygame.draw.rect(window, yellow, [map_width + 10, 60, 70, 30])
    pygame.draw.rect(window, yellow, [map_width + 10, 100, 100, 30])
    pygame.draw.rect(window, yellow, [map_width + 10, 140, 70, 30])

    slow_text = font.render("Slow", True, black)
    medium_text = font.render("Medium", True, black)
    fast_text = font.render("Fast", True, black)

    window.blit(slow_text, [map_width + 15, 65])
    window.blit(medium_text, [map_width + 15, 105])
    window.blit(fast_text, [map_width + 15, 145])

def gameLoop():
    global snake_speed
    game_over = False
    game_close = False

    x1 = map_width / 2
    y1 = map_height / 2

    x1_change = 0
    y1_change = 0

    direction = "STOP"

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, map_width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, map_height - block_size) / 20.0) * 20.0

    wall_startx = map_width // 2 - block_size
    wall_starty = map_height // 2 - 100
    wall_endy = map_height // 2 + 100

    while not game_over:

        while game_close == True:
            window.fill(black)
            message("You Lost!Press Q-Quit or C-Play Again", red, )
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    x1_change = -block_size
                    y1_change = 0
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    x1_change = block_size
                    y1_change = 0
                    direction = "RIGHT"
                elif event.key == pygame.K_UP and direction != "DOWN":
                    y1_change = -block_size
                    x1_change = 0
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    y1_change = block_size
                    x1_change = 0
                    direction = "DOWN"
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if map_width + 10 < mouse_pos[0] < map_width + 80 and 60 < mouse_pos[1] < 90:
                    snake_speed = 10
                if map_width + 10 < mouse_pos[0] < map_width + 80 and 100 < mouse_pos[1] < 130:
                    snake_speed = 15
                if map_width + 10 < mouse_pos[0] < map_width + 80 and 140 < mouse_pos[1] < 170:
                    snake_speed = 20

        if x1 >= map_width:
            x1 = 0
        elif x1 < 0:
            x1 = map_width - block_size
        if y1 >= map_height:
            y1 = 0
        elif y1 < 0:
            y1 = map_height - block_size

        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        pygame.draw.rect(window, red, [foodx, foody, block_size, block_size])

        # Vẽ tường
        for wall_y in range(wall_starty, wall_endy, block_size):
            pygame.draw.rect(window, blue, [wall_startx, wall_y, block_size, block_size])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for segment in snake_List:
            pygame.draw.rect(window, green, [segment[0], segment[1], block_size, block_size])

        show_score(Length_of_snake - 1)
        draw_buttons()
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, map_width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, map_height - block_size) / 20.0) * 20.0
            Length_of_snake += 1

        # Kiểm tra va chạm với tường
        if wall_startx <= x1 < wall_startx + block_size and wall_starty <= y1 < wall_endy:
            game_close = True

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()

import pygame
import random
import time


pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0,0,255)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snakes")
pygame.display.update()

# Game specific variables

snake_size = 30
font = pygame.font.SysFont(None, 40)
fps = 60
clock = pygame.time.Clock()


# defining functions

# for score and messages
def print_score(text, color, x, y):
    screen_text = font.render(text,True, color)
    gameWindow.blit(screen_text, [x,y])

# for printing all rectangle of snake
def print_snake(gameWindow, color, snk_list):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x, y, snake_size, snake_size])


# Game Loop
def game_loop():
    exit_game = False
    game_over = False
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
    score = 0
    init_velocity = 5
    snake_x = 45
    snake_y = 55
    snk_list = []
    snk_len = 1

    while not exit_game:
        if game_over: 
            gameWindow.fill(white)
            print_score("Game Over Press Enter!", red, 100,200)
            for event in pygame.event.get():
                if event.key == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_RETURN:
                        game_loop()

        
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score +=1
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_len += 5

            if snake_x<= 0 or snake_x >=900 or snake_y <=0 or snake_y >=600:
                game_over = True

            head = [snake_x, snake_y]
            snk_list.append(head)

            if len(snk_list) > snk_len:
                del(snk_list[0] )
            
            if head in snk_list[:-1]:
                game_over = True
                
            gameWindow.fill(white)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            print_snake(gameWindow, black, snk_list)
            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            print_score("score : " + str(score*10), blue, 5,5)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
game_loop()




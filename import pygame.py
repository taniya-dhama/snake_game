import pygame
import random
import time

pygame.init()


width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")



x, y = 200, 200
delta_x, delta_y = 0, 0
food_x, food_y = random.randrange(0, width, 10), random.randrange(0, height, 10)
snake_list = [(x, y)]
snake_length = 1  
clock=pygame.time.Clock()
highest_score=0



game_over = False



font = pygame.font.SysFont("bahnschrift", 15)


def snake():
    global x, y, food_x, food_y, game_over, snake_list, snake_length

   
    x = (x + delta_x) % width
    y = (y + delta_y) % height

    
    if (x, y) in snake_list[:-1]:  
        game_over = True
        return

    
    snake_list.append((x, y))

    
    if (food_x == x and food_y == y):
        
        while (food_x, food_y) in snake_list:
            food_x, food_y = random.randrange(0, width, 10), random.randrange(0, height, 10)
        snake_length += 5
    else:
        
        if len(snake_list) > snake_length:
            del snake_list[0]

    
    screen.fill((0, 0, 0))
    score = font.render("SCORE: " + str(snake_length - 1), True, (255, 255, 0))  # Snake score is length - 1
    screen.blit(score, [0, 0])

    
    pygame.draw.rect(screen, (255, 255, 255), [food_x, food_y, 10, 10])

    
    for (i, j) in snake_list:
        pygame.draw.rect(screen, (168, 50, 98), [i, j, 10, 10])

    pygame.display.update()


def game_over_screen():
    global highest_score
    screen.fill((0, 0, 0))
    your_score=(snake_length-1)
    highest_score=max(highest_score,your_score)


    
    msg = font.render(f"GAME OVER YOUR SCORE IS {your_score}.",True, (255, 255, 255))
    screen.blit(msg, [width // 3, height // 3])
    msg = font.render("PRESS Q-QUIT GAME OR C-PLAY AGAIN!",True, (255, 255, 255))
    screen.blit(msg, [width // 3, height // 2])
    msg = font.render(f"HIGHEST SCORE IS {highest_score}",True,(255,255,255))
    screen.blit(msg,[width // 3, height // 4])
    pygame.display.update()
    

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()  
            if event.type == pygame.KEYDOWN:
                if event.unicode.lower() == "q":
                    pygame.quit()
                    quit()
                elif event.unicode.lower() == "c":
                    # reset_game()  # Reset game state
                    waiting_for_input = False
                    reset_game()
                    snake()

def reset_game():
    global game_over,snake_length,food_x,food_y,snake_list,delta_x,delta_y
    game_over=False
    snake_length=1
    delta_x,delta_y=0,0
    food_x, food_y = random.randrange(0, width, 10), random.randrange(0, height, 10)
    snake_list = [(x, y)]



while True:
    # game_over=True
    if game_over:
        game_over_screen()

    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and delta_x == 0:
                delta_x = -10
                delta_y = 0 
            elif event.key == pygame.K_RIGHT and delta_x == 0:
                delta_x = 10
                delta_y = 0
            elif event.key == pygame.K_UP and delta_y == 0:
                delta_y = -10
                delta_x = 0
            elif event.key == pygame.K_DOWN and delta_y == 0:
                delta_y = 10
                delta_x = 0

    
    snake()
   

   
    clock.tick(15)
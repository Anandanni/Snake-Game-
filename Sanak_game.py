import pygame
import random
import  os

#Music for game
pygame.mixer.init()
pygame.mixer.music.load('nagin.mp3')
pygame.mixer.music.play()



pygame.init()
# sw=12000
# sh=600
#creating a display
gamewindow=pygame.display.set_mode((900,600))
pygame.display.set_caption("SanakAnand")
pygame.display.update()
#BackGround image

bgimg=pygame.image.load("img2.jpg")
bgimg=pygame.transform.scale(bgimg,(900,600)).convert_alpha()




#Colors

white=(255,255,255)
red=(255,0,0)

black=(0,0,0)




#Clock

clock=pygame.time.Clock()

#Score on screen
font=pygame.font.SysFont(None,55)
def screen_score(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

#function of head

def plot_snake(gamewindow,color,sanak_list,snake_size):
    for x,y in sanak_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])


#Welcome screen

def welcome():
    exit_game=False
    while not exit_game:
        gamewindow.fill(white)
        screen_score("Welcome to My Game",black,200,300)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game==True




    pygame.display.update()
    clock.tick(60)


#Game Loop
def gameloop():
    # Importan variablie game spicifi
    exit_game = False
    game_over = False

    snake_x = 50
    snake_y = 55
    snake_size = 30
    fps = 60
    volo_x = 0
    volo_y = 0

    food_x = random.randint(10, 900 / 2)
    food_y = random.randint(10, 600 / 2)
    score = 0
    init_volo = 5
    # Lenght of sanak
    sanak_list = []
    sanak_lenght = 1

    #check highscore file not in system
    if (not os.path.exists("high_score.txt")):
        with open("high_score.txt", "w") as f:
            f.write("0")



    # High_score Python file read

    with open("high_score.txt", "r") as f:
        hiscore = f.read()
    while not exit_game:
        if game_over:
            with open("high_score.txt", "w") as f:
                f.write(str(hiscore))
            gamewindow.fill(white)
            screen_score("Game Over !Press Enter  ", red, 600 / 15, 900 / 15)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('nagin.mp3')
                        pygame.mixer.music.play()

                        gameloop()


        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        volo_x = init_volo
                        volo_y = 0
                    if event.key == pygame.K_LEFT:
                        volo_x = -init_volo
                        volo_y = 0
                    if event.key == pygame.K_UP:
                        volo_y = -init_volo
                        volo_x = 0
                    if event.key == pygame.K_DOWN:
                        volo_y = init_volo
                        volo_x = 0
                    # Cheating
                    if event.key==pygame.K_q:
                        score+=100

            snake_x = snake_x + volo_x
            snake_y = snake_y + volo_y

            # Eatiing  food logic

            if abs(snake_x - food_x) < 25 and abs(snake_y - food_y) < 25:
                pygame.mixer.music.load('eat.mp3')
                pygame.mixer.music.play()
                score = score + 10

                food_x = random.randint(10, 900 / 2)
                food_y = random.randint(10, 600 / 2)
                sanak_lenght += 5
                if score>int(hiscore):
                    hiscore=score



            gamewindow.fill(white)
            #Imge blid
            gamewindow.blit(bgimg,(0,0))
            # Screen_Score
            screen_score(" Anand Your score :" + str(score)+" Hiscore"+str(hiscore), red, 5, 5)
            # Food for snake
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])
            # Empyt head
            head = []
            head.append(snake_x)
            head.append(snake_y)
            sanak_list.append(head)

            # Remove haed
            if len(sanak_list) > sanak_lenght:
                del (sanak_list[0])

            # Game over condiction
            if head in sanak_list[:-1]:
                game_over=True
                pygame.mixer.music.load('out.wav')
                pygame.mixer.music.play()
            if snake_x < 0 or snake_x > 900 or snake_y < 0 or snake_y > 600:
                game_over = True
                pygame.mixer.music.load('out.wav')
                pygame.mixer.music.play()

                # print("Game is over bsdk")


            # Head of snake
            # pygame.draw.rect(gamewindow, black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gamewindow, black, sanak_list, snake_size)

        pygame.display.update()

        clock.tick(fps)

    pygame.quit()
    quit()

gameloop()

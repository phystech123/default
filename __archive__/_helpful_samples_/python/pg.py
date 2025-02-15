# import pygame
# import sys
# from pygame.color import THECOLORS
# import random
# from random import randint

# pygame.init()

# n=(int(input()), int(input()))
# yy={}
# width=1200
# height=800

# screen = pygame.display.set_mode((width, height))
# screen.fill(THECOLORS['white'])
# font=pygame.font.SysFont('couriernew', 40, True, True)

# flag=0
# x=width//n[0]
# y=height//n[1]

# for i in range(n[0]+1):
#     pygame.draw.line(screen, (0,0,0), (flag*x, 0), (flag*x, height))
#     flag+=1

# flag=0

# for i in range(y+1):
#     pygame.draw.line(screen, (0,0,0), (0, flag*y), (width, flag*y))
#     flag+=1

# flag=1
# for j in range(n[1]):
#     for i in range(n[0]):
#         text=font.render(str(flag), False, THECOLORS['black'])
#         screen.blit(text, (i*x, j*y + y//2))
#         yy[flag]=(i*x+1, j*y+1)
#         flag+=1

# m=randint(0, flag-1)
# r=pygame.Rect(yy[m], (x-1,y-1))
# pygame.draw.rect(screen, THECOLORS['yellow'], r, 0)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         pygame.display.flip()






import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
rect = pygame.Rect(40, 40, 120, 120)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.move_ip(-40, 0)
            elif event.key == pygame.K_RIGHT:
                rect.move_ip(40, 0)
            elif event.key == pygame.K_UP:
                rect.move_ip(0, -40)
            elif event.key == pygame.K_DOWN:
                rect.move_ip(0, 40)

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), rect, 0)

    pygame.display.flip()
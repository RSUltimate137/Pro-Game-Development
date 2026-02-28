import pygame
import time
pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birthday Greeting Card!")

font=pygame.font.SysFont("Times New Roman",62)
text=font.render("Happy Birthday to you!",True,"yellow")

img=pygame.image.load("./images/img1.png")
img1=pygame.image.load("./images/img2.jpg")

image = pygame.transform.scale(img,(WIDTH,HEIGHT))

running=True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
           
    screen.blit(image,(0,0))
    screen.blit(text,(0,50))
    pygame.display.update()
    time.sleep(2)
    screen.blit(img1,(0,0))
    pygame.display.update()

pygame.quit()
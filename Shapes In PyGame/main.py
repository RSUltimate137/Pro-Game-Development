import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill(("white"))
pygame.display.update()

class Circle():
    def __init__(self,color,radius,position):
        self.color = color
        self.radius = radius
        self.position = position
        self.circle_surface = screen
    def draw(self):
        self.draw_circle = pygame.draw.circle(self.circle_surface,self.color,self.position,self.radius)
    def grow(self,r):
        self.radius+=r
        self.draw_circle = pygame.draw.circle(self.circle_surface,self.color,self.position,self.radius)
circle1 = Circle("yellow",60,(300,300))
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("red")
            circle1.draw()
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill("blue")
            circle1.grow(15)
            pygame.display.update()
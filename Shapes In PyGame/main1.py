import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill(("white"))
pygame.display.update()

class Circle():
    def __init__(self,color,radius,position,width):
        self.color = color
        self.radius = radius
        self.position = position
        self.width = width
        self.circle_surface = screen
    def draw(self):
        self.draw_circle = pygame.draw.circle(self.circle_surface,self.color,self.position,self.radius,self.width)
    def grow(self,r):
        self.radius+=r
        self.draw_circle = pygame.draw.circle(self.circle_surface,self.color,self.position,self.radius,self.width)
circle1 = Circle("yellow",60,(300,300),0)
circle2 = Circle("purple",40,(300,300),0)
circle3 = Circle("black",20,(300,300),0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("red")
            circle1.draw()
            circle2.draw()
            circle3.draw()
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill("blue")
            circle1.grow(15)
            circle2.grow(13)
            circle3.grow(11)
            pygame.display.update()
        if event.type == pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            circle4 = Circle("green",2,(pos),0)
            circle4.draw()
            pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
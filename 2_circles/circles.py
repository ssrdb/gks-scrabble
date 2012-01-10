import pygame

(width, height) = (400,400)
back_color = (255,255,255)

class Particle:
  def __init__(self,(x,y),size):
    self.x=x
    self.y=y
    self.size=size
    self.color = (0,0,255)
    self.thickness = 1

  def display(self):
    pygame.draw.circle(screen,self.color, (self.x,self.y),self.size,self.thickness)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Tutorial 2')
screen.fill(back_color)

my_first_particle = Particle((150,50),15)
my_first_particle.display()
my_second_particle = Particle((250,150),15)
my_second_particle.display()


pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      running=False

import random
import math
import pygame

background_colour = (255,255,255)
(width, height) = (1024, 720)
gravity = (math.pi/2, 0.08)
drag = 0.999
elasticity = 0.95

def addVectors((angle1,length1), (angle2,length2)):
  x = math.cos(angle1)*length1 + math.cos(angle2)*length2
  y = math.sin(angle1)*length1+math.sin(angle2)*length2
  length = math.sqrt(x*x+y*y)
  angle = math.atan2(y,x)
  return (angle, length)

def findParticle(particles, x, y):
  for p in particles:
    if math.sqrt((p.x-x)**2+(p.y-y)**2) <= p.size:
      return p
  return None

class Particle():
    def __init__(self, (x, y), size):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 1
        self.speed = 0.05
        self.angle = 0

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        (self.angle, self.speed) = addVectors((self.angle,self.speed),gravity)
        self.speed*=drag

    def bounce(self):
        if self.x > width - self.size:
          self.x = 2*(width - self.size) - self.x
          self.angle = math.pi - self.angle
          self.speed *= elasticity
        elif self.x < self.size:
          self.x = 2*self.size - self.x
          self.angle = math.pi - self.angle
          self.speed *= elasticity
          
        if self.y + self.size > height: 
          self.y = 2*(height - self.size) - self.y
          self.angle *= -1
          self.speed *= elasticity
        elif self.y < self.size:
          self.y = 2*self.size - self.y
          self.angle *= -1
          self.speed *= elasticity

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bounce')
number_of_particles = 3
my_particles = []
screen.fill(background_colour)
clock = pygame.time.Clock()

for n in range(number_of_particles):
    size = random.randint(10, 40)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)

    particle = Particle((x,y),size)
    particle.speed = random.uniform(1,2)
    particle.angle = random.uniform(0,math.pi*2)
    my_particles.append(particle)

selected_particle = None
running = True
while running:
    screen.fill(background_colour)
    for particle in my_particles:
        particle.move()
        particle.bounce()
        particle.display()

    timeDrFreeman = clock.tick(50)
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        (mouseX, mouseY) = pygame.mouse.get_pos()
        selected_particle = findParticle(my_particles, mouseX, mouseY)
      elif event.type == pygame.MOUSEBUTTONUP:
        if selected_particle:
          selected_particle.colour = (0,0,255)
          selected_particle = None
          
    if selected_particle:
      selected_particle.colour = (255,0,0)
      (mouseX, mouseY) = pygame.mouse.get_pos()
      dx = mouseX - selected_particle.x
      dy = mouseY - selected_particle.y
      selected_particle.angle = math.atan2(dy,dx)
      selected_particle.speed = math.sqrt(dx**2+dy**2)*0.1

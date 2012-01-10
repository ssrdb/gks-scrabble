import random
import math
import pygame

background_colour = (255,255,255)
(width, height) = (1024, 720)

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

    def bounce(self):
        if self.x > width - self.size:
          self.x = 2*(width - self.size) - self.x
          self.angle = math.pi - self.angle
        elif self.x < self.size:
          self.x = 2*self.size - self.x
          self.angle = math.pi - self.angle

        if self.y + self.size > height: 
          self.y = 2*(height - self.size) - self.y
          self.angle *= -1
        elif self.y < self.size:
          self.y = 2*self.size - self.y
          self.angle *= -1

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 5')
number_of_particles = 10
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
    particle.angle = math.pi/4.0
    my_particles.append(particle)


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


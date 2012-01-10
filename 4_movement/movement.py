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
        self.speed = 0.01
        self.angle = 0

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 4')
number_of_particles = 10
my_particles = []
screen.fill(background_colour)

for n in range(number_of_particles):
    size = random.randint(10, 20)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)

    particle = Particle((x,y),size)
    particle.speed = random.random()
    particle.angle = random.uniform(0,math.pi*2)
    my_particles.append(particle)


running = True
while running:
    screen.fill(background_colour)
    for particle in my_particles:
        particle.move()
        particle.display()

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
       super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen,"green",self.position,self.radius,2)
   
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        if self.radius == ASTEROID_MIN_RADIUS:
            self.kill()
            return
        self.kill()
        random_angle = random.uniform(20,50)
        asteroid1 = self.velocity.rotate(random_angle)
        asteroid2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = asteroid1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = asteroid2 * 1.2
        
       
        





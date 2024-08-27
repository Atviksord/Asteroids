from circleshape import CircleShape
import pygame
from constants import *

class Megashot(CircleShape):
    def __init__(self, x, y):
       super().__init__(x, y, SHOT_RADIUS)
    def draw(self, screen):
        pygame.draw.circle(screen,"gold",self.position,self.radius,10)
   
    def update(self, dt):
        self.position += self.velocity * dt

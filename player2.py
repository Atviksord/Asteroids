import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot
from megashot import Megashot

class Player2(CircleShape):
    def __init__(self, x, y, life = 5):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.cooldown = 0
        self.health = life

    def draw(self, screen):
        pygame.draw.polygon(screen, "pink", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
 

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown = self.cooldown - dt

        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_KP_0]:
            self.shoot()
        if keys[pygame.K_KP_1]:
            self.megashoot()
    
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def shoot(self):
        if self.cooldown <= 0:
            self.cooldown = PLAYER_SHOOT_COOLDOWN
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
    def megashoot(self):
        if self.cooldown <= 0:
            self.cooldown = MEGA_SHOT_COOLDOWN
            megashot = Megashot(self.position.x ,self.position.y)
            megashot.velocity = pygame.Vector2(0, 0.5).rotate(self.rotation ) * PLAYER_SHOOT_SPEED

    
            
       


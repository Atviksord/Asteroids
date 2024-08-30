import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot
from megashot import Megashot
from mine import Mine

class Player(CircleShape):
    def __init__(self, x, y, life = 5):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.cooldown = 0
        self.mine_cooldown = 0

        self.health = life
        self.points = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

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

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_t]:
            self.megashoot()
        if keys[pygame.K_e]:
            self.placemine()
    
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
    
    def placemine(self):
        if self.mine_cooldown <=0:
            self.mine_cooldown = MINE_COOLDOWN
            mine = Mine(self.position.x,self.position.y)
            mine.velocity = pygame.Vector2(0,0).rotate(self.rotation) * PLAYER_SHOOT_SPEED
    
    ##def calculatePoints(self):


    
            
       


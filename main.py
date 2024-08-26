import pygame
import sys
from constants import *
from player import Player
from Asteroid import *
from asteroidfield import AsteroidField
from shot import Shot



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updateable
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    Shot.containers = (updateable, drawable, shots)


    player = Player(SCREEN_WIDTH /2,SCREEN_HEIGHT/2)
    asteroidfield1 = AsteroidField()
    
    
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for thing in updateable:
            thing.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collisioncheck(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collisioncheck(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")
        for stuff in drawable:
            stuff.draw(screen)
        

       
        
        
        
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
    
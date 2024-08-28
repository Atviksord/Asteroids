import pygame
import sys
from constants import *
from player import Player
from Asteroid import *
from asteroidfield import AsteroidField
from shot import Shot
from megashot import Megashot
from player2 import Player2



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    megashots = pygame.sprite.Group()



    AsteroidField.containers = updateable
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    Shot.containers = (updateable, drawable, shots)
    Megashot.containers = (updateable,drawable,megashots)
    Player2.containers = (updateable,drawable)


    player = Player(SCREEN_WIDTH /2,SCREEN_HEIGHT/2)
    player2 = Player2(SCREEN_WIDTH / 3, SCREEN_HEIGHT /3)
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
                player.kill()
                player.health -= 1
                player = Player(SCREEN_WIDTH /2,SCREEN_HEIGHT/2,player.health)
                print(player.health)
                if player.health <= 0:
                    player.kill()
                
            if asteroid.collisioncheck(player2):
                player2.kill()
                player2.health -= 1
                player2 = Player2(SCREEN_WIDTH /2,SCREEN_HEIGHT/2,player2.health)
                if player2.health <= 0:
                    player2.kill()
            if player.health and player2.health <= 0:
                print("--------GAME OVER-------")
                sys.quit()
                    

            for megashot in megashots:
                if asteroid.collisioncheck(megashot):
                    asteroid.kill()
                    megashot.kill()

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
    
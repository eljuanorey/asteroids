import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shoots)
    AsteroidField.containers = (updatable)

    player_instance = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(player_instance):
                print("Game over!")
                sys.exit()
                return
        
        for asteroid in asteroids:
            for shot in shoots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()

            
        pygame.display.flip()
        
        dt = clock.tick(FPS) / 1000.0

if __name__ == "__main__":
    main()
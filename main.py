import pygame, constants, player

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player_instance = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))
        player_instance.draw(screen)
        player_instance.update(dt)
        pygame.display.flip()
        
        dt = clock.tick(constants.FPS) / 1000.0

if __name__ == "__main__":
    main()
import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    Player.containers = (updateable, drawable)
    player =  Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)
        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)
        
        pygame.display.flip()
        
        # limit framerate to 60fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
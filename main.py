# this allows us to use code from
# the open-source pygame library
# throughout this file
# import pygame # type: ignore
import constants
import pygame
from player import Player

def main():
  print("Starting Asteroids!")
  print(f"Screen width: {constants.SCREEN_WIDTH}")
  print(f"Screen height: {constants.SCREEN_HEIGHT}")
  pygame.init()
  screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  
  drawable = pygame.sprite.Group()
  updatable = pygame.sprite.Group()
  
  Player.containers = (drawable, updatable)
  player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
  dt = 0
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    updatable.update(dt)
    
    for item in drawable:
      item.draw(screen)
    
    screen.fill("black")
    player.draw(screen)
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    
    

if __name__ == "__main__":
    main()
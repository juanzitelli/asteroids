import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED 
class Player(CircleShape):
    def __init__(self, x, y):
      self.x = x
      self.y = y
      self.rotation = 0
      super().__init__(self.x, self.y ,PLAYER_RADIUS)
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
      return pygame.draw.polygon(screen, "white", self.triangle(), 2)
      
    def rotate(self, dt):
      self.rotation += PLAYER_TURN_SPEED * dt
      
    def update(self, dt):
      keys = pygame.key.get_pressed()
      if keys[pygame.K_a]:
        self.rotate(-dt)
      if keys[pygame.K_d]:
        self.rotate(dt)
      if keys[pygame.K_s]:
        self.move(-dt)
      if keys[pygame.K_w]:
        self.move(dt)
      
    
    def move(self, dt):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      self.position += forward * PLAYER_SPEED * dt
import pygame
import os

img_path = os.path.join ('TailsTheFox.png')

class character(object):
    def __init__(self):
      pygame.sprite.Sprite.__init__(self)

      character.image = pygame.image.load ('TailsTheFox.png')
      #self.image = character.image
      #self.image = pygame.trasform.scale(self.image(50,50))
      self.x = 50
      self.y = 50
      self.hitbox = (self.x, self.y, 50, 50)

    def draw(self, surface):
      surface.blit(self.image,(self.x, self.y))
      self.image = pygame.transform.scale(self.image,(50,50))

class Mypaddle(object):
    def __init__(self):
       """The Constructor of the Sprite """ 
       
     Pygame.Sprite.Sprite.__init__(self):

      paddle.image = pygame. image.load("TailsTheFox.png")

      self.image = pygame.scale(self.image, (20,500))


      self.x = 600
      self.y = 30

class ball(object):
    def __init__(self):
        """ The constructor of the class """
        pygame.sprite.Sprite.__init__(self)

        ball.image = pygame.image.load("TailsTheFox.png")
        
        self.image = pygame.transform.scale(self.image,(50,50))

        self.x = 20
        self.y = 30
        self.x_velocity = 1
        self.y_velocity = 1
        
    def draw(self, surface):
        """ Draw on surface """
        surface.blit(self.image, (self.x, self.y))
        


pygame.init()
screen_width = 500
screen_hight = 500
screen = pygame.display.set_mode((screen_width,screen_hight))


Sprite = character()
clock = pygame.time.Clock() 


running = True
while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False

  screen.fill((255,255,255))
  Sprite.draw(screen)


  pygame.display.update()
 
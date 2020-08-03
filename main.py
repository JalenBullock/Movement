import pygame
import os

img_path = os.path.join ('TailsTheFox.png')

class character(object):
    def __init__(self):
      pygame.sprite.Sprite.__init__(self)

      character.image = pygame.image.load ('TailsTheFox.png')
      #self.image = character.image
      #self.image = pygame.trasform.scale(self.image(50,50))
      self.x = 500
      self.y = 500
      self.hitbox = (self.x, self.y, 500, 500)

    def draw(self, surface):
      surface.blit(self.image,(self.x, self.y))
   



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

screen.fill((500,500,500))
Sprite.display(screen)


pygame.display.update()
 
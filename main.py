import pygame
import os

img_path = os.path.join('Dylan The Fox.png')

class charater(objects):
  def__init__(self):
   pygame.sprite.Sprite.__init__(self)

   character.image = pygame.image.load
   ('Dylan The Fox.png')
   self.image = character.image
   self.image = pygame.trasform.scale(self.image(50,50))

   self.x = 50
   self.y = 50
   self.hitbox = (self.x, self.y, 55, 55)

 def draw(self, surface):
   surface.blit(self.image,(self.x, self.y))
   



pygame.init()
screen_width = 600
screen_hight = 600
screen = pygame.display.set_mode((screen_width,screen_hight))


Sprite = character()
clock = pygame.time.Clock()


running = True
while running

 for event in pygame.event.get()
   if event.type == pygame.QUIT:
     pygame.quit()
     running = False
wd
 
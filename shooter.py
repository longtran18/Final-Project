import sys, pygame, pygame.mixer
from pygame.locals import *

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

background = pygame.image.load("Final Project/resources/batman.png")
ship = pygame.image.load("Final Project/resources/batman.png")
ship = pygame.transform.scale(ship,(64,64))



while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()



  clock.tick(60)

  mx,my = pygame.mouse.get_pos()

  screen.blit(background,(0,0))
  screen.blit(ship,(mx-32,500))
  pygame.display.flip()
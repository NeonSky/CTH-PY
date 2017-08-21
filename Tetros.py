import pygame as pg

from GameManager import GameManager

#Block -> 1x1
#Shape -> Has 4 blocks
#BlockMap -> Has instance of every placed block
#GameManager -> Controls score and general game logic like spawning shapes and removing them. Also rendering
#Tetros -> Screen management

gameManager = GameManager()

background_colour = (0, 0, 0)
(width, height) = (640, 480)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('Tetros')
screen.fill(background_colour)

running = True
while running:
  gameManager.draw()
  pg.display.flip()

  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False
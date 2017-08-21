import pygame as pg

#Block -> 1x1
#Shape -> Has 4 blocks
#BlockMap -> Has instance of every placed block
#GameManager -> Controls score and general game logic like spawning shapes and removing them
#Tetros -> Screen management

background_colour = (0, 0, 0)
(width, height) = (640, 480)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('Tetros')
screen.fill(background_colour)

pg.display.flip()

running = True
while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False
import pygame as pg

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
import pygame as pg

from GameManager import GameManager
from AudioManager import AudioManager

gameManager = GameManager()
audio_manager = AudioManager()
audio_manager.play_music()

background_color = (0, 0, 0)
(width, height) = (640, 640)

target_framerate = 60
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Tetros')
screen.fill(background_color)

clock = pg.time.Clock()

running = True
while running:
  gameManager.update()
  gameManager.draw(screen)
  pg.display.flip()



  #pygame.time.Clock.tick() sets a maximum framerate for the screen to draw
  clock.tick(target_framerate)
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False
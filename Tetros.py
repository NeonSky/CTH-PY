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

pg.init()
myfont = pg.font.SysFont("monospace", 24)
label = myfont.render("Highscore", 1, (255, 255, 255))
screen.blit(label, (430, 50))
for i in range(0, 5):
  label = myfont.render(str(i+1), 1, (255, 255, 255))
  screen.blit(label, (380, 150+i*50))

clock = pg.time.Clock()

running = True
while running:
  gameManager.update()
  gameManager.draw(screen)
  pg.display.flip()

  if gameManager.isGameOver:
    audio_manager.play_game_over()
  elif not audio_manager.music_playing:
    audio_manager.play_music()


  #pygame.time.Clock.tick() sets a maximum framerate for the screen to draw
  clock.tick(target_framerate)
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False
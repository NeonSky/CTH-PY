import pygame as pg

sample_rate = 44100
channels = 2
bitsize = -16 #uint_16 bit size
buffer = 2048
music_filename = "Tetris.mp3"
game_over_filename = "Game_Over.mp3"
class AudioManager:
    def __init__(self):

        pg.mixer.init(frequency=sample_rate, channels=channels, size=bitsize, buffer=buffer)
        pg.mixer.music.load(music_filename)


    def play_music(self):
        pg.mixer.music.play(-1)

    def play_game_over(self):
        pg.mixer.music.stop()
        sound = pg.mixer.Sound(game_over_filename)
        sound.play()


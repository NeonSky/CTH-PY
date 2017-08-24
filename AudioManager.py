import pygame as pg

sample_rate = 44100
channels = 2
bitsize = -16 #uint_16 bit size
buffer = 512
music_filename = "Tetris.mp3"
game_over_filename = "Game_Over.wav"
class AudioManager:
    def __init__(self):
        self.music_playing = False
        pg.mixer.init(frequency=sample_rate, channels=channels, size=bitsize, buffer=buffer)
        pg.mixer.music.load(music_filename)
        self.lost_sound = pg.mixer.Sound(game_over_filename)


    def play_music(self):
        pg.mixer.music.play(-1)
        self.music_playing = True


    def play_game_over(self):
        pg.mixer.music.stop()
        self.music_playing = False
        self.lost_sound.play(loops=0)



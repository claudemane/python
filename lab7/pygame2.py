import pygame
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))

music = ["music/music2.wav","music/rickroll2.wav"]
i = 0
is_playing = False

pygame.mixer.music.load(music[i])

def play_music():
    pygame.mixer.music.play()
    global is_playing
    is_playing = True

def stop_music():
    pygame.mixer.music.stop()
    global is_playing
    is_playing = False

def play_next_track():
    global i
    i = (i + 1) % len(music)
    pygame.mixer.music.load(music[i])
    if is_playing:
        play_music()

def play_previous_track():
    global i
    i = (i - 1) % len(music)
    pygame.mixer.music.load(music[i])
    if is_playing:
        play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_playing:
                    stop_music()
                else:
                    play_music() 
            elif event.key == pygame.K_RIGHT:
                play_next_track()
            elif event.key == pygame.K_LEFT:
                play_previous_track()

pygame.quit()

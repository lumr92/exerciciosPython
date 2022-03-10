'''Faça um programa em python que abre e recomenda o áudio de um arquivo mp3'''

import pygame

pygame.init()
pygame.mixer.music.load('ForfunTeoriaDinamicaGastativaCompleto .mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()
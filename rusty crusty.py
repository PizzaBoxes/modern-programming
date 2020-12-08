#i'm very rusty
from pygame.locals import*
import pygame
import time
pygame.init()

#screen variables
Black = (0, 0, 0)
White = [0, 255, 0]
LineMin = 800
LineMax = 20
windowWide = 800
windowTall = 600

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

words = ['word']
word = words[0]

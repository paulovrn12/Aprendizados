# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# 1. Quais são os dados de entrada necessários?
#   * 

# 2. Que devo fazer com estes dados?
#   *

# 3. Quais são as restrições deste problema?
#   *

# 4. Qual é o resultado esperado?
#   *

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   *

import pygame

pygame.mixer.init()
pygame.init()
input('Tecle ENTER para iniciar... ')
pygame.event.wait()
pygame.mixer.music.load('The_Weeknd-Blinding_Lights.mp3')
pygame.mixer.music.play()
input('Tecle ENTER para finalizar... ')
pygame.event.wait()
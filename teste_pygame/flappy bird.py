import pygame
import os
import random

TELA_LARGURA = 500
ALTURA_TELA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.loaad(os.path.join('imgs','pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.loaad(os.path.join('imgs','base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.loaad(os.path.join('imgs','bg.png')))
IMAGEM_PASSARO = pygame.transform.scale2x(pygame.image.loaad(os.path.join('imgs','bird1.png')))
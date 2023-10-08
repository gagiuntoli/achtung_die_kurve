import pygame

MINIMUM_PLAYERS = 2
MAXIMUM_PLAYERS = 3

BLACK  = (0x00, 0x00, 0x00)
ORANGE = (0xFF, 0x8C, 0x00)
WHITE  = (0xFF, 0xFF, 0xFF)
RED    = (0xFF, 0x00, 0x00)
GREEN  = (0xAA, 0xFF, 0x00)
BLUE   = (0x00, 0x96, 0xFF)

FPS            = 24
HEIGHT         = 900
WIDTH          = 1100
SPEED          = 70.0
ROTATION_SPEED = 2.0
DELTA_TIME     = 1.0 / FPS
CONTACT_RADIUS = 2.0
LINE_WIDTH     = 5

PLAYERS_COLORS = [WHITE, RED, ORANGE, GREEN, BLUE]

ROTATION_KEYS = [
    [pygame.K_z, pygame.K_a],
    [pygame.K_m, pygame.K_k],
    [pygame.K_v, pygame.K_b]
]
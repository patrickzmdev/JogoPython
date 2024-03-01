# C
import pygame

COLOR_RED = (255, 0, 7, 0)
COLOR_WHITE = (255, 255, 255)

# E
ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 0.5,
                'Level1Bg2': 1,
                'Level1Bg3': 1.5,
                'Level1Bg4': 2,
                'Player1': 2,
                'Player2': 2,
                'Enemy1': 1,
                'Enemy2': 1.5
                }

EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w
                 }
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s
                   }
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a
                   }
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d
                    }

# W
WIN_WIDTH = 576
WIN_HEIGHT = 323

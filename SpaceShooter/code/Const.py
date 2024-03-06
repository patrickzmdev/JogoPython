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
                'Player1Shot': 3,
                'Player2': 3,
                'Player2Shot': 2,
                'Enemy1': 1,
                'Enemy1Shot': 3,
                'Enemy2': 1,
                'Enemy2Shot': 3
                }

ENTITY_HEALTH = {'Level1Bg0': 999,
                 'Level1Bg1': 999,
                 'Level1Bg2': 999,
                 'Level1Bg3': 999,
                 'Level1Bg4': 999,
                 'Player1': 300,
                 'Player1Shot': 1,
                 'Player2': 300,
                 'Player2Shot': 1,
                 'Enemy1': 200,
                 'Enemy1Shot': 4,
                 'Enemy2': 200,
                 'Enemy2Shot': 3
                 }

ENTITY_SHOT_DELAY = {'Player1': 20,  # intervalo de criação de tiro
                     'Player2': 15,
                     'Enemy1': 100,
                     'Enemy2': 150

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
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL
                    }

# W
WIN_WIDTH = 576
WIN_HEIGHT = 323

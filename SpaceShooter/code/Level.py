#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from SpaceShooter.code.Const import C_WHITE, MENU_OPTION, EVENT_ENEMY, WIN_HEIGHT, C_GREEN, C_CYAN
from SpaceShooter.code.Enemy import Enemy
from SpaceShooter.code.Entity import Entity
from SpaceShooter.code.EntityFactory import EntityFactory
from SpaceShooter.code.EntityMediator import EntityMediator
from SpaceShooter.code.Player import Player


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # opção do menu
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 4000)
        pygame.time.set_timer(EVENT_TIMEOUT, 20000)  # 20 segundos cada level

    def run(self, ):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)

            # for para desenhar todas as entidades
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)

                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Pontos de Vida {ent.health} | Score: {ent.score}', C_GREEN,
                                    (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Pontos de Vida {ent.health} | Score: {ent.score}', C_CYAN, (10, 45))

            # texto a ser printado na tela
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            # atualizar a tela
            pygame.display.flip()

            # verificar relacionamentos de entidades
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            # conferir eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lacida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

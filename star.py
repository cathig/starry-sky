# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 19:19:08 2020

@author: Cathig
"""
import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star in the sky."""

    def __init__(self, ss_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = ss_game.screen

        # Load the star image and set is rec attribute.
        self.image = pygame.image.load('images/gingerbread_star.png')
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's exact horizontal position.
        self.x = float(self.rect.x)
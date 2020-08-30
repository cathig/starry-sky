# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 15:09:30 2020

@author: Cathig
"""
import sys
import pygame
from random import randint
from settings import Settings
from star import Star

class StarrySky:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # Set the window size and title bar text
        # Windowed
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # Full screen
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Starry Sky")

        self.stars = pygame.sprite.Group()

        self._create_starry_field()

    def _create_starry_field(self):
        """Create the field of stars."""
        # Create a star and find the number of stars in a row if spaced evenly.
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        # Determine the number of rows of stars that fit if spaced evenly.
        available_space_y = (self.settings.screen_height - 3 * star_height)
        number_stars_y = available_space_y // (2 * star_height)

        # Determine the number of stars to create.
        number_stars = number_stars_x * number_stars_y

        # Create the full field of of stars.
        for star_number in range(number_stars):
            self._create_star(star_number)

    def _create_star(self, star_number):
        #Create a star and place it in the row.
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = randint(0, self.settings.screen_width - star_width)
        star.rect.x = star.x
        star.rect.y = randint(0, self.settings.screen_height - star_height)
        self.stars.add(star)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        """Respond to key presses and mouse events."""
        # Gracefully exit when 'X' or alt+F4 close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                             and event.key == pygame.K_q):
                pygame.quit()
                # sys.exit() - in text, but does not close gracefully

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ss = StarrySky()
    ss.run_game()
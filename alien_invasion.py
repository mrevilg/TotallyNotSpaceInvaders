import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Totally Not Space Invaders")

    # Make a ship.
    ship = Ship(screen)
	
    # Set the background color.
    bg_color = (230, 230, 230)

	# Start main loop for the game.
    while True:
        gf.check_events()
        
        # Redraw the screen during each pass of the the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()
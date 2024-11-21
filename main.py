import sys
import pygame
import random
from settings import Settings
from user import User
from obstacle import Obstacle

class TechFighters:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.user = User(self)

        self.obstacles = pygame.sprite.Group()


        pygame.display.set_caption("Tech Fighters")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.obstacles.update()
            self._update_screen()
            self.user.update()
            self.clock.tick(60)
            self._load_obstacle()
            self._delete_obstacle()
            
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                # Move the ship to the right.
                    self.user.moving_right = True
                    self.user.facing_right = True
                elif event.key == pygame.K_LEFT:
                    self.user.moving_left = True
                    self.user.facing_right = False
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.user.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.user.moving_left = False

                
    def _update_screen(self):
        self.screen.fill(self.settings.bg_colour)
        for obstacle in self.obstacles.sprites():
            obstacle.draw_obstacle()
        self.user.blitme()
        pygame.display.flip()

    def _load_obstacle(self):
        if random.randint(0,50) == 3:
            new_obstacle = Obstacle(self)
            self.obstacles.add(new_obstacle)

    def _delete_obstacle(self):
        for obstacle in self.obstacles.copy():
            if obstacle.rect.bottom <= 0:
                self.obstacles.remove(obstacle)
    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = TechFighters()
    game.run_game()





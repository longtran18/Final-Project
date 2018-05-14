"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
From:
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
 
Explanation video: http://youtu.be/BCxWJgN4Nnc
 
Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/
"""
#Week 1: Created Project Proposal
# Week 2: Made jumping circle
# Week 3: Swapped template to one more suitable for project,read and broke and undid different parts, figured out how to use custom graphics 
import pygame
from pygame import *
from time import sleep

 
# Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 52, 52)
BLUE = (52, 52, 255)
 
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        
        # Creates Player image
        width = 40
        height = 60
        #self.image = pygame.Surface([width, height])
        self.image=pygame.image.load("Final Project/Resources/batman.png")
        self.image = pygame.transform.scale(self.image,(20,23))
        #self.image.fill(RED)
 
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
 
        # List of sprites we can bump against
        self.level = None
 
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
                
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
        """ Called when user hits 'jump' button. """
 
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
 
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
 
 
class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
 
 
class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
         
        # Background image
        self.background = pygame.image.load("Final Project/Resources/800x600.png")
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        #screen.fill(BLUE)
        self.size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        self.screen = pygame.display.set_mode(self.size)
        self.screen.blit(self.background, (0, 0))
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
 
 
# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        # Array with width, height, x, and y of platform,put platforms in here
        level = [#[800, 70, 0, 0],
                 [10, 90, 330, 520],
                 [10, 30, 370, 480],
                 [10, 30, 370, 540],
                 [50, 10, 370, 540],
                 [100, 10, 370, 560],
                 [10, 140, 460, 410],
                 [10, 120, 490, 450],
                 [10, 90, 540, 480],
                 [10, 30, 500, 410],
                 [10, 30, 570, 360],
                 [10, 30, 380, 360],
                 [90, 10, 530, 480],
                 [50, 10, 370, 500],
                 [100, 10, 530, 440],
                 [100, 10, 280, 480],
                 [100, 10, 320, 440],
                 [40, 10, 280, 430],
                 [100, 10, 100, 430],
                 [10, 70, 150, 430],
                 [10, 100, 230, 430],
                 [10, 100, 200, 500],
                 [80, 10, 200, 560],
                 [10, 40, 280, 530],
                 [50, 10, 320, 350],
                 [40, 10, 570, 350],
                 [10, 80, 620, 260],
                 [10, 90, 310, 260],
                 [10, 100, 250, 260],
                 [10, 120, 220, 260],
                 [10, 90, 180, 260],
                 [10, 130, 120, 260],
                 [10, 70, 50, 260],
                 [10, 70, 400, 260],
                 [10, 100, 440, 260],
                 [10, 120, 480, 260],
                 [10, 80, 540, 260],
                 [10, 100, 670, 260],
                 [10, 50, 700, 260],
                 [10, 120, 760, 260],
                 [70, 10, 380, 400],
                 [80, 10, 500, 400],
                 [10, 80, 50, 430],
                 [90, 10, 90, 560],
                 [40, 10, 0, 560],
                 [70, 10, 50, 510],
                 [10, 50, 80, 520],
                 [10, 50, 20, 420],
                 [10, 50, 90, 430],
                 [50, 10, 680, 410],
                 [10, 100, 700, 470],
                 [30, 10, 700, 470],
                 [730, 10, 70, 200],
                 [730, 10, 0, 160],
                 #[700, 10, 100, 400],
                 [10, 60, 100, 0],
                 [10, 70, 100, 90],
                 [10, 30, 130, 0],
                 [10, 100, 130, 60],
                 [10, 130, 160, 0],
                 [10, 90, 190, 0],
                 [10, 40, 190, 120],
                 [10, 10, 220, 0],
                 [10, 110, 220, 50],
                 [10, 0, 250, 0],
                 [10, 120, 250, 40],
                 [10, 110, 280, 0],
                 [10, 20, 280, 140],
                 [10, 50, 310, 0],
                 [10, 70, 310, 90],
                 [10, 110, 340, 0],
                 [10, 20, 340, 140],
                 [10, 120, 370, 0],
                 [10, 10, 370, 150],
                 [10, 10, 400, 0],
                 [10, 130, 400, 40],
                 [10, 70, 430, 0],
                 [10, 50, 430, 110],
                 [10, 50, 460, 0],
                 [10, 70, 460, 90],
                 [10, 40, 490, 0],
                 [10, 80, 490, 80],
                 [10, 110, 520, 0],
                 [10, 20, 520, 140],
                 [10, 10, 550, 0],
                 [10, 120, 550, 40],
                 [10, 60, 580, 0],
                 [10, 70, 580, 90],
                 [10, 0, 610, 0],
                 [10, 130, 610, 30],
                 [10, 10, 640, 0],
                 [10, 120, 640, 40],
                 [10, 50, 670, 0],
                 [10, 70, 670, 90],
                 [10, 130, 700, 0],
                 #[730, 10, 70, 450],
                 ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
 
 
def main():
    """ Main Program """
    pygame.init()
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Batman Maze")
 
    # Create the player
    player = Player()
 
    # Create all the levels
    level_list = []
    level_list.append( Level_01(player) )
 
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
 
    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
 
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
        current_level.update()
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left < 0:
            player.rect.left = 0
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
 
if __name__ == "__main__":
    main()
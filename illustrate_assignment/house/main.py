import pygame
import game
# YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
import house

# YOU SHOULD CONFIGURE THESE TO MATCH YOUR GAME
# window title bar text
TITLE = "House"
# pixels width
WINDOW_WIDTH  = 700
# pixels high
WINDOW_HEIGHT = 600
# frames per second
DESIRED_RATE  = 70


class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate ):

        game.Game.__init__( self, title, width, height, frame_rate )

        self.mGame = house.Picture( width, height )
        return

    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        x = mouse_position[ 0 ]
        y = mouse_position[ 1 ]

    def paint( self, surface ):
        self.mGame.draw( surface )

        return


def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )


if __name__ == "__main__":
    main( )

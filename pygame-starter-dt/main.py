import pygame
import game_mouse
import asteroids

class PygameApp( game_mouse.Game ):

    def __init__( self, width, height, frame_rate ):

        # title of the application is ""
        game_mouse.Game.__init__( self, "Asteroids",
                                  width,
                                  height,
                                  frame_rate )
        # create a game instance
        self.mGame = asteroids.Asteroids( width, height )
        return
        
        
    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        x = mouse_position[ 0 ]
        y = mouse_position[ 1 ]

        if pygame.K_a in keys:
            self.mGame.turnShipLeft( 5.0 )
        
        if pygame.K_d in keys:
            self.mGame.turnShipRight( 5.0 )

        if pygame.K_w in keys:
            self.mGame.accelerateShip( 2.0 )
        
        if 1 in newbuttons:
            print("button clicked")

        self.mGame.evolve( dt )

        return
    
    def paint( self, surface ):
        self.mGame.draw( surface )
        return

def main():
    pygame.font.init( )
    game = PygameApp( 700, 700, 30 )
    game.main_loop( )
    
if __name__ == "__main__":
    main()

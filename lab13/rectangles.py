import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 780
SHAPE_WIDTH = 600
SHAPE_HEIGHT = 300
BACKGROUND = (WHITE)
BORDER_THICKNESS1 = 30
BORDER_THICKNESS2 = 20
BORDER_THICKNESS3 = 10
SHAPE_FILL_COLOR = (RED)

# Always begin with initialization, sizing, and captioning
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rectangle')

# A best practice is to do the drawing in its own function
def draw_scene():
    screen.fill(BACKGROUND)  # "Clear the screen"
    the_rectangle = (
        (SCREEN_WIDTH-SHAPE_WIDTH)//2,   # Upper-left x
        (SCREEN_HEIGHT-SHAPE_HEIGHT)//2, # Upper-left y
        SHAPE_WIDTH,                     # Width
        SHAPE_HEIGHT,                    # Height
        )
    pygame.draw.rect(screen, SHAPE_FILL_COLOR, the_rectangle)  # filled
    pygame.draw.rect(screen, BLUE, the_rectangle, BORDER_THICKNESS1)  # outline 1
    pygame.draw.rect(screen, GREEN, the_rectangle, BORDER_THICKNESS2)  # outline 2
    pygame.draw.rect(screen, BLACK, the_rectangle, BORDER_THICKNESS3)  # outline 3
    pygame.display.flip()  # Put the drawing on the screen

# Draw the scene then wait for the QUIT event to come in
draw_scene()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
import pygame
import random
import math

pygame.init()

FPS = 60
WIDTH, HEIGHT = 800, 800
ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTLINE_COLOR = (187, 173, 168)
OUTLINE_THICNESS = 10
BACKGROUND_COLOR = (240, 210, 180)
FONT_COLOR = (119, 110, 101)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

# define the tiles here now
class Tile:
    COLORS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95, 59),
        (237, 208, 115),
        (237, 204, 99), 
        (236, 202, 80)
    ]
    def __init__(self, value, row, col): # to merge specific one
        self.value = value
        self.row = row
        self.col = col
        # setting x & y cordinates
        self.x = col* RECT_WIDTH
        self.y = row* RECT_HEIGHT

    def get_color(self):            # get the color we will be using in each tile.
        color_index = int(math.log2(self.value))- 1 # helps to to map the tile value to a color index.
        color = self.COLORS[color_index] # uses that index to access the corresponding color in a list of colors.
        return color


    def draw(self, window): # to draw
         
         color = self.get_color()             # This calls the get_color method to determine the color of the tile based on its value.      
         pygame.draw.rect(window, color, (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))   # this draw a rectangle on the window surface with corodinates.

         text = FONT.render(str(self.value), 1, FONT_COLOR)    # This method render the tile's value as a text surface by converting to string.
         window.blit( # The blit method in Pygame is used to draw one image onto another
             text, 
            (self.x + (RECT_WIDTH / 2 - text.get_width() / 2),
             self.y + (RECT_HEIGHT / 2 - text.get_height() / 2))
        )  # this tells at which exact point the text will be drawn on the rectangle tile. (at the middle)



# The set_pos method is used to determine the current position of a tile on a grid, based on its x and y coordinates. 
# It updates the tile's row and col attributes to reflect its current position.
    def set_pos(self,  ceil = False):   
        if ceil:
            self.row = math.ceil(self.y / RECT_HEIGHT)
            self.col = math.ceil(self.x / RECT_WIDTH)
            
        else:
            self.row = math.floor(self.y / RECT_HEIGHT)
            self.col = math.floor(self.x / RECT_WIDTH)
# Using ceil or floor ensures that the tile's position is snapped to the nearest grid cell, rather than being a fractional value. 
# This is useful in games or simulations where objects need to be aligned to a grid.
# RECT_HEIGHT and RECT_WIDTH are likely constants representing the height and width of a single grid cell or rectangle. **




# The move method is used to update the position of a tile by a specified amount. This is useful in games or simulations where objects need to move around on a grid or screen.
    def move(self, delta): 
        self.x += delta[0]   # adds the first element of the delta tuple (i.e., the change in x coordinate) to the current x coordinate.
        self.y += delta[1]   # adds the second element of the delta tuple (i.e., the change in y coordinate) to the current y coordinate.
    


# drawing the gride and border lines
def draw_grid(window):
    for row in range(ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.rect(window, OUTLINE_COLOR, (0, y, WIDTH, OUTLINE_THICNESS))

    for col in range(COLS):
        x = col * RECT_WIDTH
        pygame.draw.rect(window, OUTLINE_COLOR, (x, 0, OUTLINE_THICNESS, HEIGHT))


    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICNESS )



def draw(window, tiles): # to draw on the screen
    window.fill(BACKGROUND_COLOR) # add bg color

    for tile in tiles.values():
        tile.draw(window) # draw each tile on the window surface.

    draw_grid(window)
    pygame.display.update()



# to get a random position and check if the position is not already using. 
def get_random_pos(tiles): # here tiles is the dictioinary that holds all the used positions
    row = None
    col = None
    while True:     # This loop will continue to run until a valid, unoccupied position is found.
        row = random.randrange(0, ROWS)  # generates random numbers
        col = random.randrange(0, COLS)

# We convert the row and column indices to a string using an f-string. This creates a unique identifier for the position. 
# Then check if this identifier is not present in the tiles dictionary or set. 
# If it's not present, it means the position is available, and we can exit the loop using the break statement.
        if f"{row}{col}" not in tiles:  
            break
    return row, col


# function to move tiles with edge cases 
def move_tiles(window, tiles, clock, direction):
    updated = True
    blocks = set()

    if direction == "left":
        sort_func = lambda x:x.col
        reverse = False
        delta = (-MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col-1}")
        merge_check = lambda tile, next_tile: tile.x > next_tile.x + MOVE_VEL
        move_check = (lambda tile, next_tile: tile.x > next_tile.x + RECT_WIDTH + MOVE_VEL)
        ceil = True

    elif direction == "right":
        sort_func = lambda x:x.col
        reverse = True
        delta = (MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == COLS -1
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col+1}")
        merge_check = lambda tile, next_tile: tile.x < next_tile.x - MOVE_VEL
        move_check = (lambda tile, next_tile: tile.x + RECT_WIDTH + MOVE_VEL < next_tile.x)
        ceil = False
        
    elif direction == "up":
        sort_func = lambda x:x.row
        reverse = False
        delta = (0, -MOVE_VEL)
        boundary_check = lambda tile: tile.row == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row-1}{tile.col}")
        merge_check = lambda tile, next_tile: tile.y > next_tile.y + MOVE_VEL
        move_check = (lambda tile, next_tile: tile.y > next_tile.y + RECT_HEIGHT + MOVE_VEL)
        ceil = True
        
    elif direction == "down":
        sort_func = lambda x:x.row
        reverse = True
        delta = (0, MOVE_VEL)
        boundary_check = lambda tile: tile.row == ROWS-1
        get_next_tile = lambda tile: tiles.get(f"{tile.row + 1}{tile.col}")
        merge_check = lambda tile, next_tile: tile.y < next_tile.y - MOVE_VEL
        move_check = (lambda tile, next_tile: tile.y + RECT_HEIGHT + MOVE_VEL < next_tile.y)
        ceil = False

    while updated:
        clock.tick(FPS)
        updated = False
        sorted_tiles = sorted(tiles.values(), key=sort_func, reverse =reverse)

        for i, tile in enumerate(sorted_tiles):
            if boundary_check(tile):  # Check if the current tile is at the boundary
                continue

            next_tile = get_next_tile(tile)
            if not next_tile:
                tile.move(delta)
            elif tile.value == next_tile.value and tile not in blocks and next_tile not in blocks:
                if merge_check(tile, next_tile):
                    tile.move(delta)

                else:
                    next_tile.value *= 2
                    sorted_tiles.pop(i)
                    blocks.add(next_tile)       
                    
            elif move_check(tile, next_tile):
                tile.move(delta) 
            else:
                continue   
            
            tile.set_pos(ceil)
            updated = True 
            
        update_tiles(window, tiles, sorted_tiles)
    
    return end_move(tiles)
    
    
    
# this fucntion is used to check if the game is finished or not by counting present tiles
def end_move(tiles):
    if len(tiles) == 16: #it checks if the number of tiles on the board is 16. If it is, the game is over,
        return "Lost"
    
    #If the game is not over, the function adds a new tile to the board. It does this by:
    row, col = get_random_pos(tiles)    
    tiles[f"{row}{col}"] = Tile(random.choice([2, 4]), row, col)
    return "continue"



# The update_tiles function updates the game board by clearing the current tiles and replacing them with a new set of sorted tiles.
def update_tiles(window, tiles, sorted_tiles):
    tiles.clear()                                   # it first clear the existing tiles.
    for tile in sorted_tiles:
        tiles[f"{tile.row}{tile.col}"] = tile       # it iterates over the sorted_tiles list and adds each tile to the tiles dictionary,
    
    draw(window, tiles)
# Finally, the function calls the draw function to redraw the game board, passing the window and tiles as arguments. 
# This updates the visual representation of the game board.



# method to generate two strating tiles randomly
def generate_tiles():
    tiles = {}              # empty dict to store tiles
    for _ in range(2):
        row, col = get_random_pos(tiles)  # generate randow row and col values 
        tiles[f"{row}{col}"] = Tile(2, row, col) 

    return tiles



# main game loop
def main():
    clock = pygame.time.Clock() # it will regulate the speed of the loop
    run = True
    
    #specifying the tiles with their position and numbering text
    tiles = generate_tiles()

    while run:
        clock.tick(FPS) # it will run at a specific time frame
        for event in pygame.event.get(): # loop through all the events that have been occuered & check and handle
            if event.type == pygame.QUIT:
                run = False
                break
        # perform different key press operations according to the keyS   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_tiles(WINDOW, tiles, clock, "left")
                    
                if event.key == pygame.K_RIGHT:
                    move_tiles(WINDOW, tiles, clock, "right")
                    
                if event.key == pygame.K_UP:
                    move_tiles(WINDOW, tiles, clock, "up")
                    
                if event.key == pygame.K_DOWN:
                    move_tiles(WINDOW, tiles, clock, "down")
            
            
        draw(WINDOW, tiles)
        
    pygame.quit()

if __name__ == "__main__":
    main()


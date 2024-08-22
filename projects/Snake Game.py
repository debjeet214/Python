import pygame
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
light_blue = (173, 216, 230)
dark_blue = (0, 0, 139)
gray = (169, 169, 169)

# Display dimensions
display_width = 600
display_height = 400

# Create the display
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Clock to control the speed of the snake
clock = pygame.time.Clock()

# Snake block size and speed
snake_block = 10
snake_speed = 15

# Fonts for displaying score and messages
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
game_over_font = pygame.font.SysFont("comicsansms", 50)


def our_snake(snake_block, snake_list):
    """
    Draws the snake on the screen with alternating blue and yellow blocks.

    :param snake_block: Size of each block in the snake.
    :param snake_list: List of positions representing the snake's body.
    """
    for i, pos in enumerate(snake_list):
        color = blue if i % 2 == 0 else yellow
        pygame.draw.rect(display, color, [pos[0], pos[1], snake_block, snake_block])


def your_score(score):
    """
    Displays the current score on the screen.

    :param score: The current score based on the length of the snake.
    """
    value = score_font.render("Your Score: " + str(score), True, white)
    display.blit(value, [0, 0])


def message(msg, color, bg_color):
    """
    Displays a centered message on the screen with a background color.

    :param msg: The message text to display.
    :param color: The color of the text.
    :param bg_color: The background color for the message.
    """
    mesg = game_over_font.render(msg, True, color, bg_color)
    mesg_rect = mesg.get_rect(center=(display_width / 2, display_height / 3))
    display.blit(mesg, mesg_rect)


def draw_button(text, color, x, y, width, height, action=None):
    """
    Draws a button on the screen with shading and triggers an action on click.

    :param text: The text displayed on the button.
    :param color: The color of the button.
    :param x: The x-coordinate of the button.
    :param y: The y-coordinate of the button.
    :param width: The width of the button.
    :param height: The height of the button.
    :param action: The function to execute when the button is clicked.
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Button shading effect
    pygame.draw.rect(display, gray, [x + 5, y + 5, width, height])
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(display, light_blue, [x, y, width, height])
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(display, color, [x, y, width, height])

    # Center the button text
    button_text = font_style.render(text, True, black)
    button_rect = button_text.get_rect(center=(x + width / 2, y + height / 2))
    display.blit(button_text, button_rect)


def quit_game():
    """
    Quits the game and closes the pygame window.
    """
    pygame.quit()
    quit()


def gameLoop():
    """
    Main game loop that handles game logic, updates the display, and checks for events.
    """
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = display_width / 2
    y1 = display_height / 2

    # Initial movement of the snake
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Position of food
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            display.fill(black)
            message("Game Over", white, dark_blue)
            your_score(length_of_snake - 1)

            # Draw buttons
            draw_button("Replay", green, display_width / 4, display_height / 2, 150, 50, gameLoop)
            draw_button("Quit", red, display_width / 2 + 50, display_height / 2, 150, 50, quit_game)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check if the snake hits the boundaries
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(black)

        # Draw food
        pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])

        # Create the snake head and add it to the snake list
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for collision with itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake
        our_snake(snake_block, snake_list)

        # Display the score
        your_score(length_of_snake - 1)

        # Draw the border
        pygame.draw.rect(display, white, [0, 0, display_width, display_height], 1)

        pygame.display.update()

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


# Start the game
gameLoop()

from components import *
from utils import *


# Player's name
player = 'Aflah'

# Initialize game components
game_set = Set()
keys = Keys()
round_num = 1
answers = {}
game_timer = Timer(120)


def window_setup():
    """
    This function sets up the game window, including background image, rectangles, game prompt, labels,
    player name, and the time left display.

    It loads the background image, draws rectangles for Set 1, Set 2, and keys area, displays the game prompt,
    labels for Set 1, Set 2, and player name, and shows the time left for the game.

    """
    # Load and display the background image
    background_image = pygame.image.load("data/background.jpg")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    WIN.blit(background_image, (0, 0))

    # Define and draw rectangles
    rectangles = [SET1_RECT, SET2_RECT, KEYS_RECT]
    for rect in rectangles:
        pygame.draw.rect(WIN, WHITE, rect)

    # Display the game prompt
    prompt_lines = [
        "Count the number of differences in the two sets.",
        "Differences could be in shape, color, or written character"
    ]
    prompt_x = WIDTH / 2 - 250
    prompt_y = SET1_ORIGIN_Y - 100
    for i, line in enumerate(prompt_lines):
        prompt_text = FONT.render(line, True, WHITE)
        line_height = prompt_text.get_height()
        line_y = prompt_y + i * line_height
        WIN.blit(prompt_text, (prompt_x, line_y))

    # Draw labels
    labels = [("Set 1", SET1_ORIGIN_X), ("Set 2", SET2_ORIGIN_X)]
    player_name_x = 30
    player_name_y = 425
    for label, x in labels:
        label_text = FONT.render(label, True, WHITE)
        label_x = x + SET_WIDTH / 2 - label_text.get_width() / 2
        label_y = SET1_ORIGIN_Y - 30 if label == "Set 1" or label == "Set 2" else player_name_y
        WIN.blit(label_text, (label_x, label_y))

    # Draw player name
    player_name_text = FONT.render("Player Name: ", True, BACKGROUND)
    player_text = FONT.render(player, True, WHITE)

    player_name_x = 30
    player_name_y = 425
    player_x = player_name_x + player_name_text.get_width()  # Adjust the X position for "Aflah"

    WIN.blit(player_name_text, (player_name_x, player_name_y))
    WIN.blit(player_text, (player_x, player_name_y))

    # Display the time left
    time_left_text_1 = FONT.render("Time Left: ", True, BACKGROUND)
    time_left_text_2 = FONT.render(f"{int(game_timer.time_left())} seconds", True, WHITE)
    time_left_x = WIDTH - 130
    time_left_y = 200
    WIN.blit(time_left_text_1, (time_left_x, time_left_y))
    WIN.blit(time_left_text_2, (time_left_x, time_left_y + 25))


def drawing():
    """
    This function handles the main drawing and gameplay logic for the IQ test game.

    It sets up the game window using the `window_setup` function and executes the game logic.
    The game runs as long as the timer has not run out. It displays Set 1 initially, then Set 2,
    and records the player's answer. When the timer runs out, it displays the game over message
    along with the player's score.

    """
    global round_num, game_set, game_timer, correct_answers  # Add game_timer

    # Set up the game window and background
    window_setup()

    if not game_timer.is_time_up():  # Check if the timer has not run out
        if keys.player_answer is None:
            # Display Set 1 and apply changes
            game_set.draw_set1()
            game_set.apply_changes()
            game_set.draw_set2()
        else:
            # Record the player's answer and proceed to the next round
            answers[round_num] = (game_set.changes_applied, keys.player_answer)
            round_num += 1
            keys.player_answer = None
            game_set = Set()

        # Draw the keys and update the display
        keys.draw_keys()
        pygame.display.update()
    else:
        # Display game over message when time is up
        game_over_font = pygame.font.SysFont("Arial", 60)
        game_over_text = game_over_font.render("Time Up :)", True, (255, 0, 0))
        game_over_x = WIDTH / 2 - game_over_text.get_width() / 2
        game_over_y = HEIGHT / 2 - game_over_text.get_height()
        WIN.fill(WHITE)
        WIN.blit(game_over_text, (game_over_x, game_over_y))

        # Calculate and display the player's score
        correct_answers = 0
        for changes, answer in answers.values():
            if changes == answer:
                correct_answers += 1
        score_text = FONT.render(f"Your score is : {correct_answers} out of "
                                 f"{round_num - 1}", True, colors['blue'])
        score_x = WIDTH / 2 - 120
        score_y = HEIGHT / 2 + 100
        WIN.blit(score_text, (score_x, score_y))
        pygame.display.update()

def main():
    """
    The main function of the IQ test game.

    This function initializes the game components, sets up the game window, handles user input,
    and controls the game loop. It continues running until the player closes the game window.

    """
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                keys.check_click()

        drawing()

    pygame.quit()


if __name__ == "__main__":
    main()
    check_saving()

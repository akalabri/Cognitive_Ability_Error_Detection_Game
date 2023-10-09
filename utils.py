import csv
import time
from main import player, answers

def save_data_to_csv(player_name, answers):
    """
    Save player answers to a CSV file with the current date and time.

    Args:
        player_name (str): The name of the player.
        answers (dict): A dictionary containing player answers for each round.

    Saves the data to 'data/game_data.csv' with columns:
    'Player Name', 'Round Number', 'Correct Answer', 'Player Answer', 'Date and Time'.
    """
    current_datetime = time.strftime("%Y-%m-%d %H:%M:%S")

    # Save answers to a CSV file
    with open('data/game_data.csv', 'a', newline='') as csvfile:
        fieldnames = ['Player Name', 'Round Number', 'Correct Answer', 'Player Answer', 'Date and Time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        for round_num, (correct_answer, player_answer) in answers.items():
            writer.writerow({
                'Player Name': player_name,
                'Round Number': round_num,
                'Correct Answer': correct_answer,
                'Player Answer': player_answer,
                'Date and Time': current_datetime
            })

def check_saving():
    """
    Prompt the user to save data to a CSV file.

    Asks the user whether they want to save data and saves it if the user responds 'yes'.
    """
    saving = input('Do you want to save data? yes/no ')
    saving_check = True
    while saving_check:
        if saving.lower() in ['yes', 'no']:
            if saving == 'yes':
                save_data_to_csv(player, answers)
            saving_check = False
        else:
            print('You entered an invalid answer')
            saving = input('Do you want to save data? yes/no ')


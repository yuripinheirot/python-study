import random

chances = 0
attempts = 0
random_number = 0

config_choices = {
    1: {
        "attempts": 10,
        "message": "Great! You have selected the Easy difficulty level"
    },
    2: {
        "attempts": 5,
        "message": "Great! You have selected the Medium difficulty level"
    },
    3: {
        "attempts": 3,
        "message": "Great! You have selected the Hard difficulty level"
    }
}

def reset_config_game():
    global chances
    global attempts
    chances, attempts = 0, 0

def question_reset_game():
    answer = input("Do you want play again? (Y/N)")

    if answer not in ["Y", "N"]:
        print("Invalid value, try again\n")
        question_reset_game()
    elif answer == "Y":
        reset_config_game()
        init_game()
    else:
        print("Byeeee!")

def select_choice():
    choice = int(input("Enter your choice: "))
    global attempts

    if choice not in [1, 2, 3]:
        print("Invalid choice, please try again...\n")
        select_choice()
    else:
        print(config_choices[choice]["message"] + "\n")
        attempts = config_choices[choice]["attempts"]

def generate_random_number():
    global random_number
    random_number = random.randint(0,100)

def question_user():
    answer = int(input("Enter your guess: "))

    if not isinstance(answer, int):
        print("Invalid value, please try again...\n")
        question_user()
    else:
        return answer

def predict_number():
    global random_number
    current_attempts = 0

    while current_attempts < attempts:
        answer = question_user()

        if answer > random_number:
            print(f"Incorrect! The number is less than {answer} \n")
        elif answer < random_number:
            print(f"Incorrect! The number is greater than {answer} \n")
        else:
            print(f"Congratulations! You guessed the correct number in {current_attempts} attempts. \n")
            return question_reset_game()

        current_attempts = current_attempts+1

    print("Oh no, Game over! :(")
    question_reset_game()



def init_game():
    welcome_message = """
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    You have 5 chances to guess the correct number.
    
    Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
    """
    print(welcome_message)
    select_choice()
    generate_random_number()
    predict_number()

init_game()



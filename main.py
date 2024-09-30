import random


def main():
    print(
        "\n  __  __       _ _   _       _ _           _   _                _____                      \n |  \\/  |     | | | (_)     | (_)         | | (_)              / ____|                     \n | \\  / |_   _| | |_ _ _ __ | |_  ___ __ _| |_ _  ___  _ __   | |  __  __ _ _ __ ___   ___ \n | |\\/| | | | | | __| | '_ \\| | |/ __/ _` | __| |/ _ \\| '_ \\  | | |_ |/ _` | '_ ` _ \\ / _ \\\n | |  | | |_| | | |_| | |_) | | | (_| (_| | |_| | (_) | | | | | |__| | (_| | | | | | |  __/\n |_|  |_|\\__,_|_|\\__|_| .__/|_|_|\\___\\__,_|\\__|_|\\___/|_| |_|  \\_____|\\__,_|_| |_| |_|\\___|\n                      | |                                                                  \n                      |_|                                                                  \n")

    correct_answers = 0
    wrong_answers = 0

    for i in range(1, 11):
        number1 = random.randint(1, 10)
        number2 = random.randint(1, 10)
        print(f"Question {i} | {number1} x {number2} = ?")

        while True:
            try:
                player_guess = int(input())
                break
            except ValueError:
                print("\033[91mPlease enter a number.\033[0m")

        correct_answer = number1 * number2
        if player_guess == correct_answer:
            print("\033[92mCorrect!\033[0m")
            correct_answers += 1
        else:
            print(f"\033[91mWrong. The answer is: {correct_answer}\033[0m")
            wrong_answers += 1

    print()
    print(f"\033[96mYou've got {correct_answers} out of 10 correct\033[0m")
    if correct_answers == 10:
        print("Well done! You are now The Maths Superstar!")
    else:
        print("Good try, but be sure to keep practicing to become The Maths Superstar!")


if __name__ == "__main__":
    main()


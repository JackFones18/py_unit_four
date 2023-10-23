import random


def main():
    # Generate a random number between 1 and 10
    target_number = random.randint(1, 10)

    while True:
        try:
            # Ask the player to guess the number
            guess = int(input("Please guess my number: "))

            # Check if the guess is correct
            if guess == target_number:
                print("You got it right!")
                break
            else:
                # Calculate the absolute difference between the guess and the target number
                difference = abs(target_number - guess)
                print(f"Oh, I am sorry. My number was {target_number}. You were {difference} away from it.")
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 10.")


if __name__ == "__main__":
    main()

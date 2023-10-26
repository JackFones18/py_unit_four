import random

# Function to determine the winner
def who_wins(user, computer):
    if user == computer:
        return "It is a tie"
    elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        return "You win!"
    else:
        return "The computer wins"

def get_choices(choice):
        if choice == 1:
            return "rock"
        elif choice == 2:
            return "paper"

        elif choice == 3:
            return"scissors"
        else:
            print("invalid. do it right child")
def main():

    user_choice = int(input("Enter your choice (1 for rock, 2 for paper, 3 for scissors): "))
    computer_choice = random.randint(1, 3)

    print("You chose", get_choices(user_choice))
    print("The computer chose", get_choices(computer_choice))

    result = who_wins(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()

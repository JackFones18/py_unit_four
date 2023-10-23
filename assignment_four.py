# assignment_four.py

def get_cost(age, county):
    """
    Calculate the ticket cost based on age and county of residence.

    Parameters:
    age (int): The age of the visitor.
    county (str): The county of residence.

    Returns:
    float: The calculated ticket cost or -1 if the age is invalid.
    """
    base_price = 70.0

    if age < 0:
        return -1
    elif age < 5:
        return 0.0
    elif county == "Montgomery":
        return 60.0
    elif county == "Howard" and age < 14:
        return base_price * 0.82  # 18% discount for Howard children
    elif age >= 65:
        if county == "Prince Georges":
            return base_price * 0.215  # 50% discount + additional 7.5% discount for Prince Georges seniors
        else:
            return base_price * 0.5  # 50% discount for senior citizens
    else:
        return base_price


def main():
    print("Welcome to Adventure Park!")

    age = int(input("What is your age? "))
    county = input("What county are you from? ")

    ticket_cost = get_cost(age, county)

    if ticket_cost == -1:
        print("Invalid age. Please enter a valid age.")
    else:
        print(f"The final price is: ${ticket_cost:.2f}")


if __name__ == "__main__":
    main()

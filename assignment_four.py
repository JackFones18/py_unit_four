# Jack Fones
# 10-26-2023
# this code calculates an adventure park ticket based off of a visitor's age and county of residence.

def get_cost(age, county):
    """
    Calculate the ticket cost based on age and county of residence.
    :param age: (int) age of visitor
    :param county: (str) country of residence
    :return: (float) ticket cost or -1 if age is invalid.
    """
    base_price = 70.0

    if age < 0:
        return -1  # In case of invalid number
    elif age < 5:
        return 0.0
    elif age >= 65:
        if county == "Prince Georges":
            return base_price * 0.4625  # 50% discount + additional 7.5% of 50% discount for Prince Georges seniors
            # Initially I put .425% and was confused why I wasn't getting the right number, but it's because I was
            # doing 57.5% off of the original instead of 7.5% off of 50%.
        elif county == "Montgomery":
            return 30.0
        else:
            return base_price * 0.5  # 50% discount for senior citizens
    elif county == "Montgomery":
        return 60.0
    elif county == "Howard" and age < 14:
        return base_price * 0.82  # 18% discount for Howard children
    else:
        return base_price


def main():
    print("Welcome to Adventure Park!")

    age = int(input("What is your age? "))
    county = input("What county are you from? (options include Montgomery, Howard, and Prince Georges.): ")

    ticket_cost = get_cost(age, county)

    if ticket_cost == -1:
        print("Invalid age. Please enter a valid age.")
    else:
        print("The final price is:", round(ticket_cost, 2),
              "dollars.")  # rounds off the ticket price to 2 decimal places


if __name__ == "__main__":
    main()

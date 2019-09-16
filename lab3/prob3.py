if __name__ == "__main__":

    birth_month = int(input("enter your birth month\n"))
    birth_date = int(input("enter your birth date\n"))
    valid = True

    #insert code here to determine if the birthday is valid
    #if ...

    if valid:
        if (birth_month == 8 and birth_date <= 24) or (birth_month == 9 and birth_date <=22):
            print("you're a virgo!")

        elif (birth_month == 9 and birth_date >= 23) or (birth_month == 10 and birth_date <= 23):
            print("you're a libra!")

        elif (birth_month == 10 and birth_date > 23) or (birth_month == 11 and birth_date <= 22):
            print("your're a scorpio")

        elif (birth_month == 11 and birth_date >= 23) or (birth_month == 12 and birth_date <= 21):
            print("you're a sagittarius!")

        elif (birth_month == 12 and birth_date >= 22) or (birth_month == 1 and birth_date <= 20):
            print("you're a capricorn!")

        elif (birth_month == 1 and birth_date >= 21) or (birth_month == 2 and birth_date <= 18):
            print("you're an aquarius!")

        elif (birth_month == 2 and birth_date >= 19) or (birth_month == 3 and birth_date <= 20):
            print("you're a pisces!")

        elif (birth_month == 3 and birth_date >= 21) or (birth_month == 4 and birth_date <= 20):
            print("you're an aries!")

        elif (birth_month == 4 and birth_date >= 21) or (birth_month == 5 and birth_date <= 21):
            print("you're an taurus!")

        elif (birth_month == 5 and birth_date >= 22) or (birth_month == 6 and birth_date <= 21):
            print("you're a gemini!")

        elif (birth_month == 6 and birth_date >= 22) or (birth_month == 7 and birth_date <= 22):
            print("you're a cancer!")

        else:
            print("your're a leo!")


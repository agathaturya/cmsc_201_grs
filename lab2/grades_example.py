#grades_example                                                                          
#gets grade from user, outputs letter grade                                              

if __name__ == '__main__':
    grade = float(input("enter your grade"))

    if grade >=90:
        print("your letter grade is an A")

    elif grade >=80:
        print("your letter grade is a B")

    elif grade >=70:
        print("your letter grade is a C")

    elif grade >=60:
        print("your letter grade is a D")

    else:
        print("you failed :(")

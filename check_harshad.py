def check_harshad(number):
    try:
        num = int(number)
        num_str = str(num)
        sum_of_digits = 0
        for i in num_str:
            sum_of_digits += int(i)
        harshad_con = int(num % sum_of_digits)
        if harshad_con == 0:
            return True
        else:
            return False
        
    except ValueError:
        print("\n--Invalid Input-- (Try Again)")
        main_prog()


def main_prog():
    con = True
    while con:
        print("\n--- Program to check Harshad Number ---\n")
        usr_input = input("Input: ")
        print("Output:", check_harshad(usr_input))
        con_input = input("Do you want to run again? (y/n): ")
        if con_input == "y":
            con = True
        else:
            quit()


main_prog()


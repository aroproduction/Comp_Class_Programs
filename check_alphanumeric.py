def check_alphanumeric(string):
    num_con, str_con = False, False
    for i in string:
        try:
            int(i)
            num_con = True
        except ValueError:
            if i.isalpha():
                str_con = True
    return num_con, str_con


con = True
while con:
    usr_input = input("Input: ")
    num_and_str_cons = check_alphanumeric(usr_input)
    if num_and_str_cons == (True, True):
        print("Output: True\n")
    else:
        print("Output: False\n")
    con_input = input("Do you want to run again? (y/n): ")
    if con_input == "y":
        con = True
    else:
        con = False

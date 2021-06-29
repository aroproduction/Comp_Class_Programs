def check_pangram(string):
    str_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    stats = 0
    for i in string:
        if i.lower() in str_list:
            stats += 1
        else:
            pass
    if stats >= 26:
        return True
    else:
        return False


con = True
while con:
    usr_input = input("Input: ")
    print("Output:", check_pangram(usr_input))
    con_input = input("Do you want to run again? (y/n): ")
    if con_input == "y":
        con = True
    else:
        con = False

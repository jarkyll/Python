#!/user/bin/env python
#string of stuff


user_input = input("Enter a list of numbers between 1 and 100, put a space too \n")
num = user_input.split()

for string_nums in num:
    if not string_nums.isdigit():
        print("I fucking told you to put a digit and ", string_nums, " is not a digit")
    elif int(string_nums) < 1:
        print(string_nums, " is a number less than 1")
    elif int(string_nums) > 100:
        print(string_nums, " is a number greater than 100")
    else:
        print(string_nums, " is a valid number")
        
                

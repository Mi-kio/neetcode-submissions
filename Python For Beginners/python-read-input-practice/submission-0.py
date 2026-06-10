def add_two_numbers() -> int:
    user_input = input()
    list_of_num = user_input.split(",")
    num1  = int(list_of_num[0])
    num2  = int(list_of_num[1])
    return num1 + num2



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())

from typing import List

def read_integers() -> List[int]:
    num_input = input()
    num_list = []
    num = num_input.split(",")
    for n in num:
        num_list.append(int(n))

    return num_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

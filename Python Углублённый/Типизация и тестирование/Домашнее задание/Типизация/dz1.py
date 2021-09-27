import random
from typing import List


def list_int(some_list: List[int]) -> List[str]:
    list_str = [str(numbers) for numbers in some_list]
    return list_str


my_list = []

for _ in range(10):
    my_list.append(random.randint(1, 50))

print("Your list of integer:", my_list)

my_list_str = list_int(my_list)

print("Your list of string:", my_list_str)

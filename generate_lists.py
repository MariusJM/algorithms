import random

# unsorted_list = random.sample(range(1001), 1000)
unsorted_list = random.sample(range(6), 5)


file_name = "bubble_sort_this.txt"

with open(file_name, 'w') as file:
    for number in unsorted_list:
        file.write(f"{number}, ")
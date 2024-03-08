from timeit import default_timer as timer
import os
import time

with open("ul_10.csv", "r") as file_data:
    unsorted_list = file_data.read().split(", ")
    unsorted_integer_list = [int(x) for x in unsorted_list if x]


def bubble_sort(nums):
    # print(nums)
    start_time = timer()
    while True:
        # print(nums)
        swap_happened = False
        for i in range(len(nums)-1):
            # os.system('cls' if os.name == 'nt' else 'clear')
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                # print(nums)
                # time.sleep(0.016680567)
                swap_happened = True
        if not swap_happened:
            end_time = timer()
            time_elapsed = end_time - start_time
            formatted_time_elapsed = format(time_elapsed, '.8f')
            print(formatted_time_elapsed)
            return nums

print(unsorted_integer_list)
print(bubble_sort(unsorted_integer_list))

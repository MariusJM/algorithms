from timeit import default_timer as timer

with open("bubble_sort_this_10k.txt", "r") as file_data:
    unsorted_list = file_data.read().split(", ")
    unsorted_integer_list = [int(x) for x in unsorted_list if x]


# print(unsorted_integer_list)
# item = unsorted_integer_list.pop(1)
# unsorted_integer_list.insert(0, item)
# print(unsorted_integer_list)



def insertion_sort(unsorted_integer_list):
    start_time = timer()
    for i in range(1, len(unsorted_integer_list)):
        current_element = unsorted_integer_list[i]
        index = i - 1

        while index >= 0 and current_element < unsorted_integer_list[index]:
            unsorted_integer_list[index + 1] = unsorted_integer_list[index]
            index -= 1
        unsorted_integer_list[index + 1] = current_element
    
    end_time = timer()
    time_elapsed = end_time - start_time
    formatted_time_elapsed = format(time_elapsed, '.8f')
    print(formatted_time_elapsed)
    return unsorted_integer_list


# print(unsorted_integer_list)
# print(insertion_sort(unsorted_integer_list))
insertion_sort(unsorted_integer_list)
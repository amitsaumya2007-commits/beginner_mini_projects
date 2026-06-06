def largest_number():
    num_list = [20, 34, 31, 56, 78, 90, 12, 45, 67, 89]
    largest = num_list[0]

    for num in num_list:
        if num > largest:
            largest = num

    return largest

print(largest_number())

   

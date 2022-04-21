def maximum(*numbers):
    current_max_number = numbers[0]

    for index in range(len(numbers)):
        if numbers[index] > current_max_number:
            current_max_number = numbers[index]
    
    return current_max_number

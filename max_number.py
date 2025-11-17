def find_max(numbers):
    """Return the maximum number from a list of numbers."""
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

input_list = input("Enter list of numbers:").replace(',', ' ').split()

numbers = []
for item in input_list:
    try:
        number = float(item)
        numbers.append(number)
    except ValueError:
        pass  # Ignore non-numeric inputs


max_number = find_max(numbers)
print(f"The maximum number is: {max_number}")   

import re

def find_2020_entries(numbers):
    for first_number in numbers:
        for second_number in numbers:
            if first_number + second_number == 2020:
                return first_number * second_number

def find_2020_entries_2(numbers):
    for first_number in numbers:
        for second_number in numbers:
            for third_number in numbers:
                if first_number + second_number + third_number == 2020:
                    return first_number * second_number * third_number

def is_digit(text):
    return text.strip().isnumeric()

# run script from CLI
if __name__ == "__main__":
    print('Please enter your expense report.')
    numbers = []

    num = input()
    while(is_digit(num)):
        numbers.append(int(num.strip()))
        num = input()

    print(find_2020_entries(numbers))
    print(find_2020_entries_2(numbers))
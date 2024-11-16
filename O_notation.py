# O notation means how running time or space requirements need when the program grows as input size grows   

# time Complexity O(n)

def get_squared_number(numbers):
    squared_number = []
    for n in numbers:
        squared_number.append(n* n)

    return squared_number

numbers = [1,2,3,4,5]
square_numbers  = get_squared_number(numbers)
# Result [1,4,9,16,25]


def get_duplicate(numbers):
    duplicate_numbers = []
    for i in range(len(numbers)):
        for j in range(i+1 , len(numbers)):
         if  numbers[i] == numbers[j]:
            duplicate_numbers.append(numbers[i])
            print(numbers[i], 'duplicate')
    return duplicate_numbers
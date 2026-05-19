def remove_adjacent_duplicates(numbers):
    result = []

    for num in numbers:
        if len(result) == 0 or result[-1] != num:
            result.append(num)

    return result
data = [1,2,55,55,6,4]
output = remove_adjacent_duplicates(data)

print("Main List:", data)
print("After operation", output)

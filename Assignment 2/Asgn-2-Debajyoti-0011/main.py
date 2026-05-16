def remove_adjacent_duplicates(lst):
    result = []

    for num in lst:
        if len(result) == 0 or num != result[-1]:
            result.append(num)

    return result


numbers = [1, 2, 2, 3, 3, 3, 4, 2, 2]
print("Original list:", numbers)

new_list = remove_adjacent_duplicates(numbers)
print("Updated list:", new_list)

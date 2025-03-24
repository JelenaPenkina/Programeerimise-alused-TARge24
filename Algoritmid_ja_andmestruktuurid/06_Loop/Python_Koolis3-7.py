def decrement_all(numbers: list):
    result = numbers[::]
    for i in range(len(result)):
        result[i] -= 1
    return result


numbers = [1, 2, 3]
print(numbers)
decremented_numbers = decrement_all(numbers)
print(numbers)
print(f'{decremented_numbers=}')
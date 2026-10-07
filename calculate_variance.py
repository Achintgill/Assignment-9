def mean(numbers):
    if len(numbers) == 0:
        raise ValueError("numbers must not be empty")
    return sum(numbers) / len(numbers)


def variance(numbers):
    mean_value = mean(numbers)
    squared_diffs = [(x - mean_value) ** 2 for x in numbers]
    variance_value = sum(squared_diffs) / len(numbers)
    return variance_value


from array import array

numbers1 = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
numbers2 = array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90])
variance1 = variance(numbers1)
variance2 = variance(numbers2)
print("Variance 1: ", variance1)
print("Variance 2: ", variance2)
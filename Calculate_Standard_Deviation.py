def standard_deviation(numbers):
    if len(numbers) == 0:
        raise ValueError("numbers must not be empty")
    mean_value = sum(numbers) / len(numbers)
    squared_diffs = [(x - mean_value) ** 2 for x in numbers]
    variance_value = sum(squared_diffs) / len(numbers)
    std_dev_value = variance_value ** 0.5
    return std_dev_value
from array import array
numbers1 = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
numbers2 = array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90])
print("Standard Deviation 1: ", standard_deviation(numbers1))
print("Standard Deviation 2: ", standard_deviation(numbers2))
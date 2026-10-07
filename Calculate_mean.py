def mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean_value = total / count
    return mean_value
from array import array
numbers1 = array('i', [1, 2, 3, 4,5, 6, 7, 8, 9])
numbers2 = array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90])
mean1 = mean(numbers1)
mean2 = mean(numbers2)
print("Mean 1: ", mean1)
print("Mean 2: ", mean2)
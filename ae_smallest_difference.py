import time


def smallest_difference1(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    result = []

    arrayOneIndex = len(arrayOne) - 1
    arrayTwoIndex = len(arrayTwo) - 1

    num1 = arrayOne[arrayOneIndex]
    num2 = arrayTwo[arrayTwoIndex]

    current_min = max(arrayOne) if max(arrayOne) >= max(arrayTwo) else max(arrayTwo)

    while (arrayOneIndex >= 0):
        current = abs((arrayOne[arrayOneIndex]) - (arrayTwo[arrayTwoIndex]))
        if current < current_min:
            num1 = arrayOne[arrayOneIndex]
            num2 = arrayTwo[arrayTwoIndex]
            current_min = current
            arrayTwoIndex -= 1
        elif current > current_min and arrayTwoIndex > 0:
            arrayTwoIndex -= 1
        else:
            arrayOneIndex -= 1
            arrayTwoIndex = len(arrayTwo) - 1
    result.append(num1)
    result.append(num2)
    return result


def smallest_difference2(array1, array2):

    array1.sort()
    array2.sort()

    result = []
    index1 = 0
    index2 = 0

    smallest = float("inf")
    current = float("inf")

    while index1 < len(array1) and index2 < len(array2):
        num1 = array1[index1]
        num2 = array2[index2]
        if num1 < num2:
            current = num2 - num1
            index1 += 1
        elif num1 > num2:
            current = num1 - num2
            index2 += 1
        else:
            return [num1, num2]
        if current < smallest:
            smallest = current
            result = [num1, num2]
    return result


arrayOne = [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123]
arrayTwo = [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]

start_time1 = time.time()
print(smallest_difference1(arrayOne,arrayTwo))
print("My program took", time.time() - start_time1, "to run")

start_time2 = time.time()
print(smallest_difference2(arrayOne, arrayTwo))
print("My program took", time.time() - start_time2, "to run")

difference = start_time1 - start_time2
print(difference)
if difference > 0:
    print("smallest difference2 is faster by ", difference)
else:
    print("smallest difference1 is faster by ",  difference)
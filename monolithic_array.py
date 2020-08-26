def isMonotonic(array):
    i = 0
    j = 1
    count = 0
    while array[i] == array[j]:
        i += 1
        j += 1
    if (array[i] < array[j]):
        while j < len(array) and (array[i] < array[j] or array[i] == array[j]):
            i = j
            j += 1
            count += 1
    else:
        while j < len(array) and (array[i] > array[j] or array[i] == array[j]):
            i = j
            j += 1
            count += 1
    if count == len(array) - 1:
        result = True
    else:
        result = False
    return result


array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print(isMonotonic(array))
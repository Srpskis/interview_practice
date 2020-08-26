
def move_element_to_end(array, element):
    length = len(array)
    index = 0
    while length > 0:
        if array[index] == element:
            current_element = array.pop(index)
            array.append(current_element)
        else:
            index += 1
        length -= 1

def move_element_to_end2(array, element):
    left = 0
    right = len(array) - 1
    while left < right:
        while left < right and array[right] == element:
            right -= 1
        if array[left] == element:
            array[left], array[right] = array[right], array[left]
        left += 1

array = [1, 2, 4, 5, 6]
print(array)
move_element_to_end2(array, 3)
print(array)


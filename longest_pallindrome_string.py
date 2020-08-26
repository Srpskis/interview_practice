
def longest_palindromic_substring(string):
    longest_length = 0
    start = 0
    end = 0
    result = []

    if len(string) == 1:
        return string

    for i in range(0, len(string)):
        left = i
        right = len(string) - 1
        current_length = 0
        while left < right:
            if string[left] == string[right]:
                if string[left + 1] != string[right - 1]:
                    right -= 1
                    current_length = 0
                    continue
                else:
                    current_length += 2
                    left += 1
                    right -= 1
                    if left == right:
                        current_length += 1
            else:
                right -= 1
        if current_length > longest_length:
            longest_length = current_length
            start = i
            end = longest_length
    for i in range(start, start + end):
        result.append(string[i])
    return "".join(result)


string = "abcdefghfedcbaa"
print(longest_palindromic_substring(string))
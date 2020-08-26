

def roman_to_integer(roman):
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    results = []

    if len(roman) == 1:
        return dict[roman[0]]

    i = 0
    while i < len(roman) - 1:
        prev = roman[i]
        curr = roman[i + 1]
        if dict[prev] < dict[curr]:
            num = dict[curr] - dict[prev]
            results.append(num)
            i += 2
        elif dict[prev] >= dict[curr]:
            results.append(dict[prev])
            i += 1
        if i == len(roman) - 1:
            results.append(dict[roman[len(roman) - 1]])
    result = 0
    for each in results:
        result += each
    return result


roman1 = "MDCXCV"
print(roman_to_integer(roman1))


# Assumptions: case sensitive

def check_permutations1(string1, string2):

    if len(string1) != len(string2):
        print(string1 + " and " + string2 + " are NOT permutations")
        return False

    dict1 = {}
    dict2 = {}

    for each in string1:
        if each in dict1:
            dict1[each] += 1
        else:
            dict1[each] = 1

    for each in string2:
        if each in dict2:
            dict2[each] += 1
        else:
            dict2[each] = 1

    if dict1 == dict2:
        print(string1 + " and " + string2 + " are permutations")
        return True
    else:
        print(string1 + " and " + string2 + " are NOT permutations")
        return False


def check_permutations2(string1, string2):

    if len(string1) != len(string2):
        print(string1 + " and " + string2 + " are NOT permutations")
        return False

    dict1 = {}

    for each in string1:
        if each in dict1:
            dict1[each] += 1
        else:
            dict1[each] = 1

    for each in string2:
        if each in dict1:
            dict1[each] -= 1
        else:
            print(string1 + " and " + string2 + " are NOT permutations")
            return False

    for key, value in dict1.items():
        if value == 0:
            print(string1 + " and " + string2 + " are permutations")
            return True
        else:
            print(string1 + " and " + string2 + " are NOT permutations")
            return False


str1 = "ABCDD"
str2 = "DACBD"
str3 = "AACBD"
str4 = "AWKBB"
#
# check_permutations1(str1, str2)
# check_permutations1(str1, str3)
#
check_permutations2(str1, str2)
check_permutations2(str1, str3)
check_permutations2(str1, str4)
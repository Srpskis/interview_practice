

def one_away(str1, str2):

    dict = {}
    count = 0

    for each in str1:
        if each in dict:
            dict[each] += 1
        else:
            dict[each] = 1

    for each in str2:
        if each not in dict:
            count += 1

    if len(str1) == len(str2) and count == 1:
        return True

    if len(str1) - 1 == len(str2) and count == 0:
        return True

    if len(str1) + 1 == len(str2) and count == 1:
        return True

    return False

string1 = "pale"

string2 = "pales"
string3 = "bale"
string4 = "bake"


print(one_away(string1, string2))
print(one_away(string2, string1))
print(one_away(string1, string3))
print(one_away(string1, string4))
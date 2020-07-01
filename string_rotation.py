

def string_rotation(str1, str2):

    if len(str1) != len(str2):
        return False

    first = 0
    x = str1[first]
    new_string1 = ""
    new_string2 = ""

    for i in range(0, len(str2)):
        if str2[i] == x:
            new_string1 += str2[i]
            first += 1
            x = str1[first]
        else:
            new_string2 += str2[i]

    final_string = new_string1 + new_string2
    if final_string == str1:
        return True
    else:
        return False


str1 = "waterbottle"
str2 = "erbottlewat"
str3 = "tercattlewa"

# print(string_rotation(str1, str2))
print(string_rotation(str1, str3))
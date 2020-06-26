

def urlify1(string, length):

    list = []

    for each in string.rstrip():
        if each == " ":
            list.append("%20")
        else:
            list.append(each)

    str = "".join(list)
    return str


def urlify2(string, length):

    string = string.rstrip().replace(" ", "%20")
    print(string)



str1 = "Mr John Smith    "
print(urlify1(str1, 13))

urlify2(str1, 13)

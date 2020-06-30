# assumptions: string has only upper case or lowercase letters (a - z)

def string_compression(word):

    old_list = list(word)
    new_list = []
    count = 1

    for i in range(0, len(old_list) - 1):
        char = old_list[i]
        if old_list[i + 1] == char:
            count += 1
            if i + 1 == len(old_list) - 1:
                new_list.append(char)
                new_list.append(str(count))
        else:
            new_list.append(char)
            new_list.append(str(count))
            count = 1
            if i + 1 == len(old_list) - 1:
                new_list.append(old_list[len(old_list) - 1])
                new_list.append(str(1))
    if len(old_list) <= len(new_list):
        return "".join(old_list)
    else:
        return "".join(new_list)

str1 = "aabcccccaaa"
str2 = "aabcccccaab"
str3 = "aabbccaa"
str4 = "aabc"


print(string_compression(str1))
print(string_compression(str2))
print(string_compression(str3))
print(string_compression(str4))

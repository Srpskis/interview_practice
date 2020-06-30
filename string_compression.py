# assumptions: string has only upper case or lowercase letters (a - z)

def string_compression_old(word):

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


def string_compression_new(word):

    new_list = []
    count = 0

    for i in range(0, len(word)):
        count += 1
        if i + 1 >= len(word) or word[i + 1] != word[i]:
            new_list.append(word[i])
            new_list.append(str(count))
            count = 0

    if len(word) <= len(new_list):
        return word
    else:
        return "".join(new_list)


str1 = "aabcccccaaa"
str2 = "aabcccccaab"
str3 = "aabbccaa"
str4 = "aabc"


print(string_compression_old(str1))
print(string_compression_old(str2))
print(string_compression_old(str3))
print(string_compression_old(str4))


print(string_compression_new(str1))
print(string_compression_new(str2))
print(string_compression_new(str3))
print(string_compression_new(str4))

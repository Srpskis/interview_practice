

def palindrome_permutation(str):

    stripped = str.replace(" ", "").lower()
    dict = {}
    count = 0

    if len(stripped) >= 3:

        for each in stripped:
            if each in dict:
                dict[each] += 1
            else:
                dict[each] = 1

        for key, value in dict.items():
            if value % 2 == 1:
                count += 1

        if count > 1:
            print("Permutation of string " + str + " CAN'T be a palindrome")
            return False
        else:
            print("Permutation of string " + str + " CAN be a palindrome")
            return True

    return False


string1 = "Tact Coa"
string2 = "Tacti Coa"
string3 = "Tactoo Coa"
string4 = "Tactiow Coa"
palindrome_permutation(string1)
palindrome_permutation(string2)
palindrome_permutation(string3)
palindrome_permutation(string4)
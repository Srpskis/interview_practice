
# Assumptions: uppercase and lowercase considered different characters


def is_unique(str):
    uniques = {}
    for each in str:
        if each in uniques:
            print("String " + str + " does not contain unique characters.")
            return False
        else:
            uniques[each] = 1
    print("String " + str + " does contain unique characters.")


is_unique("Love")
is_unique("lovely")
is_unique("Lovely")

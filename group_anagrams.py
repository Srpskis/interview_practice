
def groupAnagrams(words):
    if len(words) == 0:
        return []
    sorted_words = []
    mappings = {}
    result = []
    for each in words:
        sorted_words.append("".join(sorted(each)))
    for i in range(0, len(sorted_words)):
        current = sorted_words[i]
        if current not in mappings:
            mappings[current] = []
            mappings[current].append(words[i])
        else:
            mappings[current].append(words[i])
    for key, value in mappings.items():
        result.append(value)
    return result


words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
print(groupAnagrams(words))
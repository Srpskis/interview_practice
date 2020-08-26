def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""

    min_string = min(strs)
    for i in range(0, len(min_string)):
        index_stop = i
        for each in strs:
            if each[i] == min_string[i]:
                continue
            else:
                if index_stop > 0:
                    result = ""
                    for i in range(0, index_stop):
                        result += min_string[i]
                    return result
                else:
                    return ""
    return min_string


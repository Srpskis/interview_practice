# Given an array of integers, return indices of two numbers such that they add up to the target int
# Assumptions:  Each input has exactly one solution.
#               You may not use the same element twice

def two_sum(nums, target):
    target_dict = {}
    result = []

    for i in range(0, len(nums)):
        num = target - nums[i]
        if num not in target_dict:
            target_dict[nums[i]] = i
        else:
            result.append(target_dict[num])
            result.append(i)
            return result
    return result


nums = [2,7,11,15]
target = 9

print(two_sum(nums, target))

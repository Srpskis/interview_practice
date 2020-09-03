

def remove_element(nums, val):
    if len(nums) == 0:
        return 0

    left = 0
    right = len(nums) - 1
    dups_count = 0
    while left <= right:
        if nums[left] != val:
            left += 1
        else:
            dups_count += 1
            num = nums[left]
            nums[left] = nums[right]
            nums[right] = num
            right -= 1
    while dups_count > 0:
        nums.pop()
        dups_count -= 1
    return len(nums)

nums = [4, 5]
print(remove_element(nums, 4))

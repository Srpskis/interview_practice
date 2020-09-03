

def remove_duplicates(nums):
    if len(nums) <= 1:
        return len(nums)
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    i += 1
    while i < len(nums):
        nums.pop(i)
    return len(nums)


nums1 = [0,0,1,1,1,2,2,3,3,4]
nums2 = [1,1,2]
print(remove_duplicates(nums1))
print(remove_duplicates(nums2))

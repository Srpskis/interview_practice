def merge(nums1, m, nums2, n):
    i = m - 1
    j = m + n - 1
    k = n - 1

    while (i >= 0 and k >= 0):
        if nums1[i] > nums2[k]:
            temp1 = nums1[i]
            temp2 = nums1[j]
            nums1[j] = temp1
            nums1[i] = temp2
            j -= 1
            i -= 1
        else:
            nums1[j] = nums2[k]
            j -= 1
            k -= 1
    while j >= 0:
        nums1[j] = nums2[k]
        j -= 1
        k -= 1



nums1 = [1,2,3,0,0,0]
m = 3
n = 3
nums2 = [2,5,6]
merge(nums1, m, nums2, n)
print(nums1)
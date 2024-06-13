"""
This solution is slow, the array is ordered so 
it is sufficient to compare the i-th number with the ith + 1
"""


def removeDuplicates(nums):
    """
        :type nums: List[int]
        :type val: int
        :rtype: int
    """
    lookup = dict()
    i = 0
    while i < len(nums):
        num = nums[i]
        if lookup.get(num):
            nums.pop(i)
        else:
            lookup[num] = True
            i += 1
    print(nums)
    return len(nums)


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(removeDuplicates([1, 1, 2]))

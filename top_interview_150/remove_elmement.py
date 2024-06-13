def removeElement(nums, val):
    """
        :type nums: List[int]
        :type val: int
        :rtype: int
    """
    u = 0
    i = 0

    while i < len(nums):
        num = nums[i]
        if num == val:
            nums[i] = nums[len(nums) - 1 - u]
            nums[len(nums) - 1 - u] = "_"
            u += 1
        else:
            i += 1

    return len(nums) - u


print(removeElement([3, 2, 2, 3], 3))

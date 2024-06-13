
def removeDuplicates(nums):
    i = 0
    while i < len(nums):
        curr = nums[i]
        next = None
        nnext = None

        if i + 1 < len(nums):
            next = nums[i + 1]

        if i + 2 < len(nums):
            nnext = nums[i + 2]

        if curr == next == nnext:
            nums.pop(i + 2)
        else:
            i += 1
    print(nums)


removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lookup = dict()
        # o(n)
        for i in range(0, len(nums)):
            lookup[(i + k) % (len(nums))] = nums[i]

        # o(n)
        for key in lookup:
            # o(1)
            nums[key] = lookup.get(key)


Solution().rotate([1, 2, 3], 3)

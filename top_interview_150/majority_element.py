class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occurrencies_target = len(nums) / 2
        lookup = dict()

        # o(n)
        for num in nums:
            if lookup.get(num) != None:
                # o(1)
                lookup[num] += 1
            else:
                # o(1)
                lookup[num] = 1

        # o(m) where 0 < m < n
        for el in lookup:
            if lookup.get(el) > occurrencies_target:
                return el


print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))

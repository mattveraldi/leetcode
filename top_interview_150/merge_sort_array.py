def merge(nums1, m, nums2, n):
    """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    p1 = m - 1
    p2 = n - 1
    p3 = len(nums1) - 1

    while True:
        element1 = -999
        element2 = -999

        if p1 >= 0:
            element1 = nums1[p1]
        if p2 >= 0:
            element2 = nums2[p2]

        if element2 > element1:
            nums1[p3] = element2
            p3 -= 1
            p2 -= 1
        else:
            nums1[p3] = element1
            p3 -= 1
            p1 -= 1

        if p3 < 0:
            break
    print(nums1)


# merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
# merge([0], 1, [1], 1)
merge([2, 0], 1, [1], 1)

import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        answer from youtube solution
        Use Binary Search to partition the shorter array. Because the left half of the combined arrays must equal the right half, the number of elements chosen from the short array instantly determines exactly how many elements must be taken from the long array.

        using shorter length between nums1 and nums2
        if len(nums1) <= len(nums2):
            short length = nums1
            long length = nums 2
            elise
            short = nums2
            long = nums1
        l and r = 0, len(short nums) - 1
        
        required half length = math.ceil(len(nums1) + len(nums2) / 2)
        left = 0
        while l <= r:
            mid = l + (r - l) // 2
            l from long = half length - mid
            r from long = len (long nums) - l from long
            total r = r form long + r - mid
            if len(long ) + len(short) == odd 
                if half length  == total r + 1
                return max(shortnums[mid], longnums[l from long])

            else:
                if half length ==  total r
                    return shortnums[mid] + longnums[l from long] / 2 



            else:
                if half length > total r:
                    r = mid - 1
                else:
                    l = mid + 1

        '''

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1


        half_length = (len(nums1) + len(nums2) + 1) // 2
        l, r = 0, len(nums1)
        while l <= r:
            ms = l + (r - l) // 2
            ml = half_length - ms
            leftA = nums1[ms - 1] if ms > 0 else float('-inf')
            leftB = nums2[ml - 1] if ml > 0 else float('-inf')
            rightA = nums1[ms] if ms < len(nums1) else float('inf')
            rightB =  nums2[ml] if ml < len(nums2) else float('inf')

            if leftA <= rightB and leftB <= rightA:
                if ((len(nums1) + len(nums2)) % 2) == 1:
                    return max(leftA, leftB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2

            if leftA > rightB:
                r = ms - 1
            if leftB > rightA:
                l = ms + 1

        return -1





        




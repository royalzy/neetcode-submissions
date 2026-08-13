class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        thought process
        should i first get the rotation
        or should i find target with if else?
        '''

        if not nums:
            return -1
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            lval = nums[l]
            mval = nums[mid]
            rval = nums[r]

            if target == mval:
                return mid

            if lval <= mval:
                # left side is sorted
                if target >= lval and target <= mval:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                # right side is sorted
                if target >= mval and target <= rval:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

        # if mid pointer equals target
        '''
        if target is smaller than mid
            if target is to right of mid, target must be smaller than r
                l = mid + 1
            if target is to left of mid, target must be bigger than r
                r = mid - 1

        if target is bigger than mid
            if target is right of mid, target must be bigger than r
                l = mid + 1
            if target is left of mid, target must be smaller than r
                r = mid - 1
        '''
        #     if nums[mid] == target:
        #         return mid

        #     elif target < nums[mid]:
        #         if target < nums[r]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
            
        #     else:
        #         if target > nums[r]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1

        # return -1

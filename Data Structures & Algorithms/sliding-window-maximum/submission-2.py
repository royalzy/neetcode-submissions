from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []
        
        numElements = len(nums) - k + 1
        arr = []

        # for each left pointer to numElements
        # go through each k values and find max
        # seems pretty brute force

        fifo = deque()
        # use fifo?

        for r in range(len(nums)):
            if fifo == []:
                fifo.append(r)
            
            else: 
                while fifo and nums[r] > nums[fifo[-1]]:
                    fifo.pop()

                while fifo and fifo[0] < r - k + 1:
                    fifo.popleft()
                
                fifo.append(r)


                if r >= k - 1:
                    arr.append(nums[fifo[0]])
                



        return arr






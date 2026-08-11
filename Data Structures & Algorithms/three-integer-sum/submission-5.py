class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []

        sortNums = sorted(nums)
        # seen = set()
        
        answer = []
        for fixed in range(len(sortNums)-2):
            if fixed > 0 and sortNums[fixed] == sortNums[fixed-1]:
                continue
            left = fixed + 1
            right = len(sortNums) - 1
            while left < right:
                sumNums = sortNums[left] + sortNums[right]

                if -sortNums[fixed] == sumNums:
                    # if tuple([sortNums[fixed], sortNums[left], sortNums[right]]) not in seen:
                    #     seen.add(tuple([sortNums[fixed], sortNums[left], sortNums[right]]))
                    answer.append([sortNums[fixed], sortNums[left], sortNums[right]])
                    left += 1
                    right -= 1
                    while left < right and sortNums[left] == sortNums[left - 1]:
                        left += 1
                    while left < right and sortNums[right] == sortNums[right + 1]:
                        right -= 1
                elif -sortNums[fixed] > sumNums:
                    left += 1
                    while left < right and sortNums[left] == sortNums[left - 1]:
                        left += 1
                elif -sortNums[fixed] < sumNums:
                    right -= 1
                    while left < right and sortNums[right] == sortNums[right + 1]:
                        right -= 1

        return answer
            
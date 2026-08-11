class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []

        sortNums = sorted(nums)
        seen = set()
        
        answer = []
        for fixed in range(len(sortNums)-2):

            left = fixed + 1
            right = len(sortNums) - 1
            while left < right:
                sumNums = sortNums[left] + sortNums[right]

                if -sortNums[fixed] == sumNums:
                    if tuple([sortNums[fixed], sortNums[left], sortNums[right]]) not in seen:
                        seen.add(tuple([sortNums[fixed], sortNums[left], sortNums[right]]))
                        answer.append([sortNums[fixed], sortNums[left], sortNums[right]])
                    left += 1

                elif -sortNums[fixed] > sumNums:
                    left += 1

                elif -sortNums[fixed] < sumNums:
                    right -= 1

        return answer
            





        
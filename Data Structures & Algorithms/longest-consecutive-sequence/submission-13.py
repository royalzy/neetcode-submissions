class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if nums == []:
        #     return 0
        # sortNums = list(set(sorted(nums)))
        # max_sequence = 1
        # sequence = 1

        # for i in range(1, len(sortNums)):
        #     if sortNums[i] == sortNums[i-1] + 1:
        #         sequence += 1
        #         max_sequence = max(max_sequence, sequence)
        #     else:
        #         sequence = 1
        

        # return max_sequence
        
        if nums == []:
            return 0
        max_sequence = 1
        sequence = 1

        setNums = set(nums)

        for num in setNums:
            if (num-1) not in setNums:
                current_num = num
                sequence = 1

                while (current_num + 1) in setNums:
                    current_num += 1
                    sequence +=1

            max_sequence = max(max_sequence, sequence)


        return max_sequence


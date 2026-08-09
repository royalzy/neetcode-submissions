class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_map = {}
        for i in nums:
            count_map[i] = count_map.get(i, 0) + 1
        
        count_bucket = [[] for i in range(len(nums) + 1)]
        for key, value in count_map.items():
            count_bucket[value].append(key)

        answer = []
        for i in count_bucket[::-1]:
            for j in i[::-1]:
                if len(answer) < k:
                    answer.append(j)

        return answer



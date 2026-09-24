class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        counter = sorted([[num, freq] for num, freq in count.items()], key=lambda x:x[1])
        counter = counter[len(counter)-k:len(nums)]
        #print(counter)
        return [counter[i][0] for i in range(k)]
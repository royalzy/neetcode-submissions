class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num = sorted(nums)
        
        res = []

        for i in range(len(num)-2):
            if i > 0 and num[i] == num[i-1]:
                continue
            j, k = i + 1, len(num) - 1
            while j < k:
                total_sum = num[i] + num[j] + num[k]
                if total_sum == 0:
                    res.append([num[i] , num[j] , num[k]])
                
                    while j < k and num[j+1] == num[j]:
                        j += 1
                    
                    while j < k and num[k-1] == num[k]:
                        k-= 1
                
                    j += 1
                    k -= 1
            
                elif total_sum > 0:
                    k -= 1

                else:
                    j += 1



        return res

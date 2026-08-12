from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # # sliding window
        
        # left = 0
        # ls1 = Counter(s1)
        # length = len(s1)
        
        # for right in range(len(s2)):
        #     # check if right value is in counter
        #     # if yes, -1 to counter char
        #     # if no, move left +1 until counter looks normal
        #     # if right value is not in counter
        #     # move left to right
        #     if length == right - left + 1:
        #         if sum(abs(ls1.values())) == 0:
        #             return True
        #         ls1[s2[left]] = ls1[s2[left]] + 1
        #         left += 1

        #     if s2[right] in ls1:
        #         if ls1.get(s2[right]) - 1 >= 0:
        #             ls1[s2[right]] = ls1[s2[right]] - 1
        #         else:
        #             ls1[s2[left]] = ls1[s2[left]] + 1
        #             left += 1

        #     else:
        #         ls1[s2[left]] = ls1[s2[left]] + 1
        #         left += 1

        # return sum(ls1.values()) == 0

        # left = 0
        # ls1 = Counter(s1)
        # length = len(s1)

        # for right in range(len(s2)):

        #     while s2[left] not in ls1 and left < len(s2) - 1:
        #         left += 1
        #         right = left

        #     while s2[right] not in ls1 and right < len(s2) - 1:
        #         right += 1
        #         left = right

        #     if length == right - left + 1:
        #         if set(ls1.values()) == {0}:
        #             return True
        #         ls1[s2[left]] = ls1[s2[left]] + 1
        #         left += 1
        #     elif length > right - left + 1:
        #         left += 1

        #     if s2[right] in ls1:
        #         if ls1.get(s2[right]) - 1 >= 0:
        #             ls1[s2[right]] = ls1[s2[right]] - 1

        # return False



        left = 0
        count = Counter(s1)
        
        for right in range(len(s2)):

            if s2[right] in count:
                count[s2[right]] = count[s2[right]] - 1

            else:
                if s2[left] in count:
                    count[s2[left]] = count[s2[left]] + 1
                left += 1

            while right - left + 1 > len(s1):
                if s2[left] in count:
                    count[s2[left]] = count[s2[left]] + 1
                left += 1
            if len(s1) ==  right - left + 1 and set(count.values()) == {0}:
                return True

        return False



            
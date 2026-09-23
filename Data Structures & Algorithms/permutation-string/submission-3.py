class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char = Counter(s1)
        l = 0

        for r in range(len(s2)):

            if s2[r] in char:
                char[s2[r]] -= 1
            
            while r - l + 1> len(s1):
                if s2[l] in char:
                    char[s2[l]] += 1
                l += 1
            if r - l + 1 == len(s1) and set(char.values()) == {0}:
                return True

        
        return False
                
            
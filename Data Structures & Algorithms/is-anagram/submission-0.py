class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sset = set(s)
        tset = set(t)

        sdict = {char:0 for char in sset}
        tdict = {char:0 for char in tset}

        for char in s:
            sdict[char] += 1
        
        for char in t:
            tdict[char] += 1

        if sdict != tdict:
            return False

        return True
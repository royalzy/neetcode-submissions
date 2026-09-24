class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for s in strs:
            char = "".join(sorted(s))
            count[char].append(s)

        return list(count.values())

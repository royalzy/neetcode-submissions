class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "EMPTY_LIST"
        delimiter = "|.|"
        answer = delimiter.join(strs)
        return answer

    def decode(self, s: str) -> List[str]:
        if s == "EMPTY_LIST":
            return []
        delimiter = "|.|"
        return s.split(delimiter)

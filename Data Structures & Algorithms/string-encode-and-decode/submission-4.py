class Solution:

    def encode(self, strs: List[str]) -> str:
        return "--123----123--".join(strs) if strs else "LISTISEMPTY"
    def decode(self, s: str) -> List[str]:
        return [] if s=="LISTISEMPTY" else s.split("--123----123--")

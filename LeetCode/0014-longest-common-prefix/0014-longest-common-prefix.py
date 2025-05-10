class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s1 = strs[0]
        for s in strs[1:]:
            while not s.startswith(s1):
                s1 = s1[:-1]
                if not s1:
                    return ""
        return s1
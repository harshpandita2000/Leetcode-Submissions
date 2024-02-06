class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            strs.sort()
            common_prefix = ""
            for i in range(min(len(strs[0]), len(strs[-1]))):
                if strs[0][i] == strs[-1][i]:
                    common_prefix += strs[0][i]
                else:
                    break
            return common_prefix
            return ""
        
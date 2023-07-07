class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        ans = min(strs , key = len)
        for str in strs:
            while not str.startwith(ans):
                ans = ans[:-1]
        return ans
            
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        start, end = 0, len(needle)
        while end <= len(haystack):
            if haystack[start:end] == needle:
                return start
            else:
                start += 1
                end += 1
        return -1
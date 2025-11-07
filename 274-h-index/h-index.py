class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i,v in enumerate(citations):
            if v >= i+1:
                h = i+1
            else:
                break
        return h
        
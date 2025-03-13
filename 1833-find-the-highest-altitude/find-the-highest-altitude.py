class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_num = gain[0]
        current = 0
        gain.insert(0,0)
        for i in range(len(gain)):
            current = current + gain[i]
            if current > max_num:
                max_num = current
            
        return max_num
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        operations = 0
        
        
        for num in freq:
            if freq[num] <= 0:
                continue
                
            complement = k - num

            if num == complement:
                operations += freq[num] // 2
                freq[num] = 0
            elif complement in freq and freq[complement] > 0:
                pairs = min(freq[num], freq[complement])
                operations += pairs
                freq[num] -= pairs
                freq[complement] -= pairs
        
        return operations
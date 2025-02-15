class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operations = 0

        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)  
            y = heapq.heappop(nums)  
            new_value = x * 2 + y 
            heapq.heappush(nums, new_value)  
            operations += 1

        return operations
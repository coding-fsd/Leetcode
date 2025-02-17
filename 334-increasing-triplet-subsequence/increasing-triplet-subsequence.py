class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        #n = len(nums)
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first: 
                first = num 
            elif num <= second: 
                second = num 
            else:
                return True 
        
        return False
        #for i in range(n - 2):
         #   for j in range(i + 1, n - 1):
          #      for k in range(j + 1, n):
           #         if nums[i] < nums[j] < nums[k]:
            #            return True
        
        #return False
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left, max_length, zero_count = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length - 1

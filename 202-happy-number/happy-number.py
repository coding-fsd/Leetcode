class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sum_of_squares(num):
            total = 0
            for digit in str(num):
                total += int(digit) ** 2
            return total
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum_of_squares(n)
        return True
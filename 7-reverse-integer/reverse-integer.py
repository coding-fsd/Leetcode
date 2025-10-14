import math
class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        ans = 0
        if x < 0 :
            flag = True
        num = abs(x)
        while num != 0 :
            t = num % 10
            ans = ans * 10 + t
            num = num // 10

        if flag:
            ans=-ans
        if ans < -2**31 or ans > 2**31 - 1:
            return 0
        return ans
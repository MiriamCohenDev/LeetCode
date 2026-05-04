class Solution(object):
    def reverse(self, x):
        mod = 1 
        if x < 0:
            mod = -1
            x = x * -1
        res = 0
        while x > 0:
            res *=10
            res += x %10
            x = x//10
        
        if res > (2 ** 31 -1):
            res = 0
        return res * mod


        
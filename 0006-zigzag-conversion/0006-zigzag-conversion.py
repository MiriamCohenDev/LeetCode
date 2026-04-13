class Solution(object):
    def convert(self, s, numRows):
        result = "";
        for i in range(numRows):
            jump = (numRows-1 - i)*2
            if jump==0:
                jump = (numRows-1)*2
            if numRows == 1:
                jump = 1
            index = i
            while len(s)>index:
                result += s[index]
                index = index + jump
                jump = (numRows-1)*2 - jump
                if jump==0:
                    jump = (numRows-1)*2
                if numRows == 1:
                    jump = 1
        return result
        
      
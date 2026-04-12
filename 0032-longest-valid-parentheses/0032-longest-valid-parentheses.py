class Solution(object):
    def longestValidParentheses(self, s):
        stack = []
        stack.append(-1)
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i);
            elif stack[-1]!=-1 and s[stack[-1]]=='(':
                stack.pop()
            else:
                stack.append(i)
        max_len = 0
        last = len(s)
        while stack:
            top = stack.pop()
            print(last, top)
            max_len = max(max_len, last - top-1 )
            last = top
        return max_len
            




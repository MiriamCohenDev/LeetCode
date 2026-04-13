class Solution(object):
    def trap(self, height):
        result = 0
        max_right = [0] * len(height)
        max_left = []
        max_1 = 0
        max_2 = 0
        for i in range(len(height)):
            if height[i] > max_1:
                max_1 = height[i]
            max_left.append(max_1)
        for i  in range(len(height)-1, -1, -1):
            if height[i]>max_2:
                max_2 = height[i]
            max_right[i] = max_2
        for i in range(len(height)):
            minimum = min(max_left[i], max_right[i])
            if (minimum - height[i]) > 0:
                result += (minimum - height[i])
        return result
            
                
            
            
        
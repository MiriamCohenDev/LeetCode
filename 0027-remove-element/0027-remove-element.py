class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        j = len(nums)-1
        while i<j:
            if nums[i] != val:
                i+=1
            if nums[j] ==val:
                j -= 1
            if nums[i] == val and nums[j] != val and i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i +=1
                j -=1
        i = 0
        while i<len(nums) and nums[i]!=val:
            i +=1
        return i
        
        
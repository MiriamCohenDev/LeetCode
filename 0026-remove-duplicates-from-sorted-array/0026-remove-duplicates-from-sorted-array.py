class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        index = 1
        run = 1
        while run< len(nums):
            if nums[run] > nums[index - 1]:
                nums[index] = nums[run]
                index += 1
            run += 1
        return index
                

        
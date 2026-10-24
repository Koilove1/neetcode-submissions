class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #this runs through the numbers to check for target
        for i in range (len(nums)):
            num = nums[i] 
            
            if num == target:
                return i
        
        return -1


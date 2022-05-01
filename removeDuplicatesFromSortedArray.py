class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        
        i = 0
        for x in range(1,len(nums)):
            if nums[i] != nums[x]:
                i+=1
                nums[i] = nums[x]
                
        return i + 1

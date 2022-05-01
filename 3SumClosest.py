class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        d= []
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):

            l = i + 1
            r = len(nums) -1
            
            while(l < r):
                threeSums = nums[i] + nums[l] + nums[r]
                
                if threeSums > target:
                    r -=1
                else:
                    l+=1
                if (abs(closest - target) > abs(threeSums - target)):
                    closest = threeSums
        return closest

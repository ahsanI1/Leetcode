class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            
            l = i +1
            r = len(nums) - 1
            while(l<r):
                threeSums = nums[i] + nums[l] + nums[r]
                if threeSums > 0:
                    r-=1
                elif threeSums < 0:
                    l+=1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while(nums[l] == nums[l-1] and l < r):
                        l+=1

        return ans

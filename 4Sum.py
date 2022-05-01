class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        output = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for x in range(i+1, len(nums)):
                if x != i + 1 and nums[x] == nums[x-1]:
                    continue
                l = x + 1
                r = len(nums) -1
                
                while(l < r):
                    theSum = nums[i] + nums[x] + nums[l] + nums[r]
                    
                    if theSum < target:
                        l+=1
                    elif theSum > target:
                        r-=1
                    else:
                        output.append([nums[i], nums[x], nums[l], nums[r]])
                        l+=1
                        while(l < r and nums[l] == nums[l-1]):
                            l+=1
        return output

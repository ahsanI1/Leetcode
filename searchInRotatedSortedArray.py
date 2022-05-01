class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        #Find the index of the minimum value in the list
        #So we know which side to search
        while(left < right):
            midpoint = left + floor((right-left)/2)
            
            #Doesn't make sense if the midpoint is greater that the rightest most index
            if nums[midpoint] > nums[right]:
                left = midpoint + 1
            else:
                right = midpoint
                
        start = left
        left = 0
        right = len(nums) - 1
        
        #This code let's us know which side to start given the minimum value index
        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start
        
        
        while(left <= right):
            midpoint = left + floor((right-left)/2)
            
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                right = midpoint -1
            else:
                left = midpoint + 1
        return -1

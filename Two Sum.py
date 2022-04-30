class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        num_dict = {}
        
        for i in range(len(nums)):
            num_dict[nums[i]] = i
            
        for i in range(len(nums)):
            second = target - nums[i]
            if second in num_dict:
                if num_dict[second] != i:
                    return [i, num_dict[second]]
            
        return -1

from typing import List

nums = [2,11,7,15]
target = 9

class Solution:
    # My Solution -> Runtime 2000ms
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    output.extend([i, j])
                    break
                
        return output
    
    # Solution AI -> Runtime 0ms
    def twoSum2(self, nums: List[int], target: int) -> List[int] | None:
        seen = {}  # maps number to its index
        for i, num in enumerate(nums):
            expected_value = target - num
            if expected_value in seen:
                print (seen)
                return [seen[expected_value], i]
            seen[num] = i
        
            
sol = Solution()
        
output = sol.twoSum2(nums, target)
print (output)
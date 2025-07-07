from typing import List

nums = [2,11,7,15]
target = 9

class Solution:
    # Solution 1 -> Runtime 2000ms
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    output.extend([i, j])
                    break
                
        return output
    
    # Solution 2 -> Runtime 487ms
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        output = []

        for num in nums:
            expected_value = target - num
            if expected_value in nums:
                if expected_value == num and len(nums) != len(set(nums)):
                    i = nums.index(num)
                    nums.remove(num)
                    j = nums.index(expected_value) + 1
                    output.extend([i,j])
                    break
                elif expected_value != num:
                    output.extend([nums.index(num), nums.index(expected_value)])
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
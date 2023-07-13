from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int):
        if ( len(nums) > 10**4 and len(nums) <2 ):
            return None
        if ( 10**9 < target and target < -10**9):
            return None
    
        for i,e in enumerate(nums):
            second_number = target - e
            if second_number in nums:
                second_number_location = nums.index(second_number)
                if (second_number_location == i):
                    continue
                return [i, second_number_location]
        return None
            
solution_object = Solution()
print(solution_object.twoSum([1,2,3,4], 6))
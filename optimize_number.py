class Solution:
    def get_sum_two_numbers(self, array: list[int], number: int) -> int:
        left = 0 
        right = len(array) - 1
        for i in range(len(array)):
            summed = array[left] + array[right]
            if summed == number:
                return array[left], array[right]
            elif summed > number:
                right -= 1
            else:
                left += 1
        return None

solution = Solution()
print(solution.get_sum_two_numbers([1,2,3,4,5,6,7,8,9,10,10], 20))
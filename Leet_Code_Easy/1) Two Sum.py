"""
Question 1:  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1: Input : nums =[2,7,11,15], target = 9
OUTPUT : [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0,1].

Example 2: Input: nums = [3,2,4], target = 6
OUTPUT : [1,2]

Example 3: Input: nums= [3,3], target = 6
Output : [0,1]

Constraints:
* 2 <= nums.length <= 10^4
* -10^9  <= nums[i] <= 10^5
* -10^5   <= target <= 10^9
* ONLY ONE VALID ANSWER EXISTS
"""

class Solution:
    def twoSum(self, nums, target):
        """
        nums: contains the list of the integers
        target: is the target value, for which we do need to find 2 integer whose sum makes it equivalent to
        target value.
        return: the list of indices of that 2 integer values.
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
## the run time complexity in here is O(n^2)/Quadratic

"""
# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test case 1 - nums: {nums1}, target: {target1} -> Indices: {solution.twoSum(nums1, target1)}")

    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Test case 2 - nums: {nums2}, target: {target2} -> Indices: {solution.twoSum(nums2, target2)}")

    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Test case 3 - nums: {nums3}, target: {target3} -> Indices: {solution.twoSum(nums3, target3)}")

    # Test case 4
    nums4 = [3,3,3,4]
    target4 = 7
    print(solution.twoSum(nums4,target4))
    
    """
## OR we can do this in O(n) ie linear time complexity as well.
class Solutions:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_to_index = {}

        for i, num in enumerate(nums):
            left_over = target - num
            if left_over in nums_to_index:
                return [nums_to_index[left_over],i]
            nums_to_index[num] = i
        return []

#this takes Linear run time complexity............
# Overone takes O(n^2)/ quadratic run time complexity.....

if __name__ == "__main__":
    solutions = Solutions()

    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test case 1 - nums: {nums1}, target: {target1} -> Indices: {solutions.twoSum(nums1, target1)}")

    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Test case 2 - nums: {nums2}, target: {target2} -> Indices: {solutions.twoSum(nums2, target2)}")

"""
LeetCode Problem #1: Two Sum
Difficulty: Easy

Problem:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

Link: https://leetcode.com/problems/two-sum/

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Hash table approach for O(n) time complexity.
        
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(n) - hash table storage
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List containing indices of two numbers that add up to target
        """
        # Dictionary to store {value: index}
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists in our hash table
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number and its index
            seen[num] = i
        
        # No solution found (though problem guarantees one exists)
        return []


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    print("Test 1 passed: [2,7,11,15], target=9 -> [0,1]")
    
    # Test case 2
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    print("Test 2 passed: [3,2,4], target=6 -> [1,2]")
    
    # Test case 3
    assert solution.twoSum([3, 3], 6) == [0, 1]
    print("Test 3 passed: [3,3], target=6 -> [0,1]")
    
    print("\nAll tests passed! ✓")

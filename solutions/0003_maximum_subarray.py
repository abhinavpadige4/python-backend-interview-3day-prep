"""
0003_maximum_subarray.py
Problem: Maximum Subarray
Difficulty: Easy
LeetCode: https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Time Complexity: O(n) - We traverse the array once
Space Complexity: O(1) - We use only constant extra space
"""

from typing import List

def max_sub_array(nums: List[int]) -> int:
    """
    Find the contiguous subarray with the largest sum.
    
    Args:
        nums: List of integers
        
    Returns:
        The maximum sum of a contiguous subarray
    """
    if not nums:
        return 0
    
    # Initialize current sum and max sum to the first element
    current_sum = max_sum = nums[0]
    
    # Iterate through the array starting from the second element
    for num in nums[1:]:
        # Either extend the current subarray or start a new one
        current_sum = max(num, current_sum + num)
        # Update max_sum if current_sum is greater
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result1 = max_sub_array(nums1)
    print(f"Test 1: nums={nums1}")
    print(f"Result: {result1} (Expected: 6)")
    assert result1 == 6
    
    # Test case 2
    nums2 = [1]
    result2 = max_sub_array(nums2)
    print(f"\nTest 2: nums={nums2}")
    print(f"Result: {result2} (Expected: 1)")
    assert result2 == 1
    
    # Test case 3
    nums3 = [5, 4, -1, 7, 8]
    result3 = max_sub_array(nums3)
    print(f"\nTest 3: nums={nums3}")
    print(f"Result: {result3} (Expected: 23)")
    assert result3 == 23
    
    # Additional test case: all negative numbers
    nums4 = [-2, -1, -3]
    result4 = max_sub_array(nums4)
    print(f"\nTest 4: nums={nums4}")
    print(f"Result: {result4} (Expected: -1)")
    assert result4 == -1
    
    print("\n✅ All tests passed!")
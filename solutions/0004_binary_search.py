"""
0004_binary_search.py
Problem: Binary Search
Difficulty: Easy
LeetCode: https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique.
- nums is sorted in ascending order.

Time Complexity: O(log n) - Binary search halves the search space each time
Space Complexity: O(1) - We use only constant extra space
"""

from typing import List

def search(nums: List[int], target: int) -> int:
    """
    Search for target in a sorted array using binary search.
    
    Args:
        nums: Sorted list of integers
        target: Integer to search for
        
    Returns:
        Index of target if found, otherwise -1
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Prevents potential overflow
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    result1 = search(nums1, target1)
    print(f"Test 1: nums={nums1}, target={target1}")
    print(f"Result: {result1} (Expected: 4)")
    assert result1 == 4
    
    # Test case 2
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    result2 = search(nums2, target2)
    print(f"\nTest 2: nums={nums2}, target={target2}")
    print(f"Result: {result2} (Expected: -1)")
    assert result2 == -1
    
    # Test case 3: target at beginning
    nums3 = [1, 2, 3, 4, 5]
    target3 = 1
    result3 = search(nums3, target3)
    print(f"\nTest 3: nums={nums3}, target={target3}")
    print(f"Result: {result3} (Expected: 0)")
    assert result3 == 0
    
    # Test case 4: target at end
    nums4 = [1, 2, 3, 4, 5]
    target4 = 5
    result4 = search(nums4, target4)
    print(f"\nTest 4: nums={nums4}, target={target4}")
    print(f"Result: {result4} (Expected: 4)")
    assert result4 == 4
    
    # Test case 5: single element array
    nums5 = [5]
    target5 = 5
    result5 = search(nums5, target5)
    print(f"\nTest 5: nums={nums5}, target={target5}")
    print(f"Result: {result5} (Expected: 0)")
    assert result5 == 0
    
    print("\n✅ All tests passed!")
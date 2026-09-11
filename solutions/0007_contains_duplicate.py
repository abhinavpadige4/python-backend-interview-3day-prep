"""
0007_contains_duplicate.py
Problem: Contains Duplicate
Difficulty: Easy
LeetCode: https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Time Complexity: O(n) - We traverse the array once
Space Complexity: O(n) - We store up to n elements in the set
"""

from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    """
    Check if the array contains any duplicate elements.
    
    Args:
        nums: List of integers
        
    Returns:
        True if any value appears at least twice, False otherwise
    """
    # Use a set to track seen elements
    seen = set()
    
    for num in nums:
        if num in seen:
            return True  # Duplicate found
        seen.add(num)
    
    return False  # No duplicates found

# Alternative approach: sorting (O(n log n) time, O(1) space)
def contains_duplicate_sort(nums: List[int]) -> bool:
    """
    Check if the array contains any duplicate elements using sorting.
    
    Args:
        nums: List of integers
        
    Returns:
        True if any value appears at least twice, False otherwise
    """
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 1]
    result1 = contains_duplicate(nums1)
    print(f"Test 1: nums={nums1}")
    print(f"Result: {result1} (Expected: True)")
    assert result1 == True
    
    # Test case 2
    nums2 = [1, 2, 3, 4]
    result2 = contains_duplicate(nums2)
    print(f"\nTest 2: nums={nums2}")
    print(f"Result: {result2} (Expected: False)")
    assert result2 == False
    
    # Test case 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result3 = contains_duplicate(nums3)
    print(f"\nTest 3: nums={nums3}")
    print(f"Result: {result3} (Expected: True)")
    assert result3 == True
    
    # Test case 4: empty array
    nums4 = []
    result4 = contains_duplicate(nums4)
    print(f"\nTest 4: nums={nums4}")
    print(f"Result: {result4} (Expected: False)")
    assert result4 == False
    
    # Test case 5: single element
    nums5 = [1]
    result5 = contains_duplicate(nums5)
    print(f"\nTest 5: nums={nums5}")
    print(f"Result: {result5} (Expected: False)")
    assert result5 == False
    
    print("\n✅ All tests passed!")
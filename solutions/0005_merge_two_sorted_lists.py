"""
0005_merge_two_sorted_lists.py
Problem: Merge Two Sorted Lists
Difficulty: Easy
LeetCode: https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

Time Complexity: O(n + m) - We traverse each list once
Space Complexity: O(1) - We use only constant extra space (in-place merging)
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists into one sorted list.
    
    Args:
        list1: Head of first sorted linked list
        list2: Head of second sorted linked list
        
    Returns:
        Head of the merged sorted linked list
    """
    # Create a dummy node to serve as the start of our result list
    dummy = ListNode()
    current = dummy
    
    # Traverse both lists until we reach the end of one
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach the remaining elements (if any)
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    
    return dummy.next

# Helper functions for testing
def create_linked_list(arr):
    """Create a linked list from an array and return its head."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Convert a linked list to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = merge_two_lists(list1, list2)
    result = linked_list_to_list(merged)
    print(f"Test 1: list1=[1,2,4], list2=[1,3,4]")
    print(f"Result: {result} (Expected: [1,1,2,3,4,4])")
    assert result == [1, 1, 2, 3, 4, 4]
    
    # Test case 2
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = merge_two_lists(list1, list2)
    result = linked_list_to_list(merged)
    print(f"\nTest 2: list1=[], list2=[]")
    print(f"Result: {result} (Expected: [])")
    assert result == []
    
    # Test case 3
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = merge_two_lists(list1, list2)
    result = linked_list_to_list(merged)
    print(f"\nTest 3: list1=[], list2=[0]")
    print(f"Result: {result} (Expected: [0])")
    assert result == [0]
    
    # Test case 4: one list empty
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([])
    merged = merge_two_lists(list1, list2)
    result = linked_list_to_list(merged)
    print(f"\nTest 4: list1=[1,2,3], list2=[]")
    print(f"Result: {result} (Expected: [1,2,3])")
    assert result == [1, 2, 3]
    
    print("\n✅ All tests passed!")
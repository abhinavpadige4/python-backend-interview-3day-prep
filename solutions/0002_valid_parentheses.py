"""
0002_valid_parentheses.py
Problem: Valid Parentheses
Difficulty: Easy
LeetCode: https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.

Time Complexity: O(n) - We traverse the string once
Space Complexity: O(n) - We use a stack that can grow up to n/2
"""

def is_valid(s: str) -> bool:
    """
    Determine if a string of parentheses is valid.
    
    Args:
        s: String containing only parentheses characters
        
    Returns:
        True if the string is valid, False otherwise
    """
    # Stack to keep track of opening brackets
    stack = []
    
    # Mapping of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        # If it's an opening bracket, push to stack
        if char in bracket_map.values():
            stack.append(char)
        # If it's a closing bracket
        elif char in bracket_map:
            # If stack is empty or top doesn't match, invalid
            if not stack or stack[-1] != bracket_map[char]:
                return False
            # Pop the matching opening bracket
            stack.pop()
        # Ignore any other characters (though problem says only brackets)
    
    # If stack is empty, all brackets were properly closed
    return len(stack) == 0

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "()"
    result1 = is_valid(s1)
    print(f"Test 1: s='{s1}'")
    print(f"Result: {result1} (Expected: True)")
    assert result1 == True
    
    # Test case 2
    s2 = "()[]{}"
    result2 = is_valid(s2)
    print(f"\nTest 2: s='{s2}'")
    print(f"Result: {result2} (Expected: True)")
    assert result2 == True
    
    # Test case 3
    s3 = "(]"
    result3 = is_valid(s3)
    print(f"\nTest 3: s='{s3}'")
    print(f"Result: {result3} (Expected: False)")
    assert result3 == False
    
    # Test case 4
    s4 = "([)]"
    result4 = is_valid(s4)
    print(f"\nTest 4: s='{s4}'")
    print(f"Result: {result4} (Expected: False)")
    assert result4 == False
    
    # Test case 5
    s5 = "{[]}"
    result5 = is_valid(s5)
    print(f"\nTest 5: s='{s5}'")
    print(f"Result: {result5} (Expected: True)")
    assert result5 == True
    
    print("\n✅ All tests passed!")
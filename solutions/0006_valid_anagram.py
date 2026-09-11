"""
0006_valid_anagram.py
Problem: Valid Anagram
Difficulty: Easy
LeetCode: https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.

Time Complexity: O(n) - We traverse both strings once
Space Complexity: O(1) - We use a fixed-size array (26 for English letters) or O(n) for hash map approach
"""

from typing import Dict

def is_anagram(s: str, t: str) -> bool:
    """
    Check if t is an anagram of s.
    
    Args:
        s: First string
        t: Second string
        
    Returns:
        True if t is an anagram of s, False otherwise
    """
    # If lengths are different, they can't be anagrams
    if len(s) != len(t):
        return False
    
    # Approach 1: Using hash map (dictionary)
    char_count: Dict[str, int] = {}
    
    # Count characters in s
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Subtract counts for characters in t
    for char in t:
        if char not in char_count:
            return False  # Character in t not found in s
        char_count[char] -= 1
        if char_count[char] < 0:
            return False  # More occurrences in t than in s
    
    # Check if all counts are zero
    return all(count == 0 for count in char_count.values())

# Alternative approach using sorting (O(n log n) time, O(1) space if we ignore sorting space)
def is_anagram_sort(s: str, t: str) -> bool:
    """
    Check if t is an anagram of s using sorting.
    
    Args:
        s: First string
        t: Second string
        
    Returns:
        True if t is an anagram of s, False otherwise
    """
    return sorted(s) == sorted(t)

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "anagram"
    t1 = "nagaram"
    result1 = is_anagram(s1, t1)
    print(f"Test 1: s='{s1}', t='{t1}'")
    print(f"Result: {result1} (Expected: True)")
    assert result1 == True
    
    # Test case 2
    s2 = "rat"
    t2 = "car"
    result2 = is_anagram(s2, t2)
    print(f"\nTest 2: s='{s2}', t='{t2}'")
    print(f"Result: {result2} (Expected: False)")
    assert result2 == False
    
    # Test case 3: empty strings
    s3 = ""
    t3 = ""
    result3 = is_anagram(s3, t3)
    print(f"\nTest 3: s='{s3}', t='{t3}'")
    print(f"Result: {result3} (Expected: True)")
    assert result3 == True
    
    # Test case 4: single character
    s4 = "a"
    t4 = "a"
    result4 = is_anagram(s4, t4)
    print(f"\nTest 4: s='{s4}', t='{t4}'")
    print(f"Result: {result4} (Expected: True)")
    assert result4 == True
    
    # Test case 5: different lengths
    s5 = "a"
    t5 = "ab"
    result5 = is_anagram(s5, t5)
    print(f"\nTest 5: s='{s5}', t='{t5}'")
    print(f"Result: {result5} (Expected: False)")
    assert result5 == False
    
    print("\n✅ All tests passed!")
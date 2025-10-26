# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.



class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_string = ''.join(ch.lower() for ch in s if ch.isalnum())
        return new_string == new_string[::-1]

        # new_string = ""
        # if len(s)>0 and s!=" ": 
        #     for ch in s:
        #         if ch.isalnum():
        #             new_string += ch

        # print(new_string)
        # if new_string.lower()==new_string[::-1].lower():
        #     return True
        # else:
        #     return False

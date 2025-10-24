# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.
# Step-by-Step Explanation
# Understanding the problem
# The goal is to find the longest common prefix among all strings in a list. For example, in ["flower", "flow", "flight"], the longest common prefix is "fl". If there’s no common prefix, we return an empty string "".

# Initial setup
# We first take the first string in the list as our starting point. This is stored in the variable first. We also store its length in first_len.

# first = strs[0]
# first_len = len(first)
# This makes sense because the longest possible prefix can’t be longer than the first string itself.

# Iterating through all strings
# We loop through each string in the list using:

# for str in strs[1:]:
# For each string, we check if the current prefix (first) still matches the beginning of that string.

# Trimming the prefix
# Inside the loop, we use a while loop to keep shortening the prefix until it matches the start of the current string:

# while first != str[:first_len]:
#     first_len -= 1
#     if first_len == 0:
#         return ""
#     first = first[:first_len]
# str[:first_len] takes the first first_len characters of the current string.
# If it doesn’t match first, we reduce first_len by 1 and cut the prefix shorter.
# If the prefix becomes empty, we return "" since there’s no common prefix.
# Updating the prefix
# After checking each string, we update first to the shortened prefix that still matches.

# Returning the result
# Once the loop finishes, first holds the longest common prefix shared by all strings. We return it as the final result.

# Example walkthrough
# Input: ["flower", "flow", "flight"]

# Start with first = "flower"
# Compare with "flow" → common prefix becomes "flow"
# Compare with "flight" → common prefix becomes "fl"
# Return "fl"
# Complexity

# Time Complexity: O(S), where S is the total number of characters across all strings.
# Space Complexity: O(1), since we only use a few variables.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        first = strs[0]
        first_len = len(first)
        print(first)

        for str in strs[1:]:
            print(str)
            while first != str[0:first_len]:
                first_len-=1
                if first_len==0:
                    return ""
                first = first[0:first_len]
        print(first)
        return first

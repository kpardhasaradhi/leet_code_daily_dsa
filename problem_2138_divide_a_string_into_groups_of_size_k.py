# A string s can be partitioned into groups of size k using the following procedure:

# The first group consists of the first k characters of the string, the second group consists of the next k characters of the string, and so on. Each element can be a part of exactly one group.
# For the last group, if the string does not have k characters remaining, a character fill is used to complete the group.
# Note that the partition is done so that after removing the fill character from the last group (if it exists) and concatenating all the groups in order, the resultant string should be s.

# Given the string s, the size of each group k and the character fill, return a string array denoting the composition of every group s has been divided into, using the above procedure.

 

# Example 1:

# Input: s = "abcdefghi", k = 3, fill = "x"
# Output: ["abc","def","ghi"]
# Explanation:
# The first 3 characters "abc" form the first group.
# The next 3 characters "def" form the second group.
# The last 3 characters "ghi" form the third group.
# Since all groups can be completely filled by characters from the string, we do not need to use fill.
# Thus, the groups formed are "abc", "def", and "ghi".
# Example 2:

# Input: s = "abcdefghij", k = 3, fill = "x"
# Output: ["abc","def","ghi","jxx"]
# Explanation:
# Similar to the previous example, we are forming the first three groups "abc", "def", and "ghi".
# For the last group, we can only use the character 'j' from the string. To complete this group, we add 'x' twice.
# Thus, the 4 groups formed are "abc", "def", "ghi", and "jxx".

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        start = 0
        end = k
        str_list = []
        rem_len = len(s[start:end])
        rem_str = ""
        fills = ""
        print(rem_len)
        if len(s)>k:
            while rem_len==k:
                str_list.append(s[start:end])
                start = end
                end = end + k
                rem_len = len(s[start:end])
                rem_str = s[start:end]
            else:
                if rem_len>0:
                    fills_len = k-rem_len
                    for i in range(fills_len):
                        fills+=fill
                    
                    rem_str = rem_str+fills
                    str_list.append(rem_str)
        elif k-len(s)>0:
            fills_len = k-len(s)
            for i in range(fills_len):
                fills+=fill
            
            s = s+fills
            str_list.append(s)
        elif k-len(s)==0:
            str_list.append(s)

        return str_list

# Step 1: Initialize variables
# You start by setting up a few variables:

# start = 0 and end = k define the window size for slicing the string.
# str_list = [] is an empty list that will store all the divided groups.
# You also calculate rem_len = len(s[start:end]) and rem_str = s[start:end] to handle the first chunk.
# fills = "" is initialized to store any extra fill characters if needed.
# Step 2: Check if the string length is greater than or equal to k
# If len(s) >= k, you enter a loop that slices the string in chunks of size k.

# Inside the while loop, you append each substring (s[start:end]) to str_list.
# Then you move the window forward by setting start = end and end += k.
# This continues until you reach the end of the string.
# If the last chunk is smaller than k, you calculate how many characters are missing and fill them using the fill character. You then append this padded chunk to str_list.

# Step 3: Handle edge cases
# If the string length is less than k, you directly pad the entire string with the required number of fill characters.

# You calculate how many fills are needed (fills_len = k - len(s)),
# Then you append the padded string to str_list.
# Step 4: Return the result
# Finally, you return str_list, which contains all the divided and padded groups.



# result = []
#         for i in range(0, len(s), k):
#             chunk = s[i:i+k]
#             if len(chunk) < k:
#                 chunk += fill * (k - len(chunk))
#             result.append(chunk)
#         return result


# The loop for i in range(0, len(s), k) automatically moves in steps of k, so you don’t need to manually track start and end.
# The padding logic is simplified to one line using string multiplication.
# This version is easier to read, runs faster, and avoids unnecessary variables.

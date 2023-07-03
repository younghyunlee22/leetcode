#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        result_list = []
        for char in s:
            if char.isalnum():
                result_list.append(char.lower())
        return result_list == result_list[::-1]
        
# @lc code=end


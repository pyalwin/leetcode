"""
Leetcode Challenge

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way. 
"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Create a list of which character is capital from given word
        ascii_codes = [True if ( 65 <= ord(ch) and ord(ch) <= 90 ) else False for ch in word]
        
        # Check if all are capital, or all are lowercase or only first letter is capital
        # Inbuilt all function works like Boolean AND, while the any works as Boolean OR
        if (all(ascii_codes)) \
           or (not any(ascii_codes)) \
           or (ascii_codes[0] and not any(ascii_codes[1:])):
            return True
        return False

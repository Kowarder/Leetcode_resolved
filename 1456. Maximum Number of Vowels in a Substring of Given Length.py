#Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
#Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vol = set('aeiou')
        count = 0
        for i in range(k):
            if s[i] in vol:
                count += 1
        maxn = count

        for i in range(k, len(s)):
            if s[i] in vol:
                count += 1
            if s[i-k] in vol:
                count -= 1
            maxn = max(count, maxn)
        return maxn

# in this problem, first i count the number of vowels in the first slide window, and slide the window to the end of s.
# each time slide, one element add and one element remove, if the new one is vowel + 1, if the remove one is vowel -1. using i - k to make sure the remove element's locate
# and each slide compare the max number of vowels.

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

 

#Example 1:

#Input: word1 = "abc", word2 = "pqr"
#Output: "apbqcr"
#Explanation: The merged string will be merged as so:
#word1:  a   b   c
#word2:    p   q   r
#merged: a p b q c r
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        l = min(len(word1), len(word2))
        for i in range(l):
            result.append(word1[i])
            result.append(word2[i])
        result.append(word1[l:])
        result.append(word2[l:])
        return (''.join(result))
# firt i set a list to store the result, and get the minimum length of two strings, result append the minimum length of the word, and append the rest part of the other words

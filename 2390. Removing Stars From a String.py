#You are given a string s, which contains stars *.

#In one operation, you can:

#Choose a star in s.
#Remove the closest non-star character to its left, as well as remove the star itself.
#Return the string after all stars have been removed.

#Note:

#The input will be generated such that the operation is always possible.
#It can be shown that the resulting string will always be unique.
class Solution:
    def removeStars(self, s: str) -> str:
        word = []
        for i in range(len(s)):
            if s[i] != '*':
                word.append(s[i])
            else:
                i += 1
                word.pop()
        return (''.join(word))
# this problem i use an easy method, using a list to store the rs=esult
# if the element isn't * add it, if meet * delete the end of list and skip this element to the next

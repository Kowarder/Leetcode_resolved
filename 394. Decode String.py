#Given an encoded string, return its decoded string.

#The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

#You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

#The test cases are generated so that the length of the output will never exceed 105.
class Solution:
    def decodeString(self, s: str) -> str:
        solution = []
        for char in s:
            if char != ']':
                solution.append(char)
            else:
                curr = ''
                while solution[-1] != '[':
                    curr = solution.pop() + curr
                solution.pop()

                curr_num = ''
                while solution and solution[-1].isdigit():
                    curr_num = solution.pop() + curr_num
                curr = int(curr_num) * curr
                solution.append(curr)
        return (''.join(solution))

# in this problem, each time meet ], recode the element before the ] until meet [, then recore the number of this element
# using number X string to get each []'s result of repeat

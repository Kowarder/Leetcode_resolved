# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        pairs, l, r = 0, 0, len(nums)-1
        while l < r:
            s = nums[l] + nums[r]
            if s > k:
                r -= 1
            elif s < k:
                l += 1
            else:
                pairs += 1
                l += 1
                r -= 1
        return pairs

# in the problem, first sort the list, and compare the value of the sum of first one and last one, if smaller means the first one is too small need to add one...
# if equals to k, pairs + 1 and delete these two elements(left + 1, right - 1)

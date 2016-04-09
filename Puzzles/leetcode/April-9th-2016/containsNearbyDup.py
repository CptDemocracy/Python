"""
[ref.href] leetcode.com/problems/contains-duplicate-ii
"
  Given an array of integers and an integer k, find out whether 
  there are two distinct indices i and j in the array such that 
  nums[i] = nums[j] and the difference between i and j is at most k.
"
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dups = {}
        i = 0
        for n in nums:
            if n in dups:
                j = dups[n]
                if i - j <= k:
                    return True
            dups[n] = i
            i += 1
        return False

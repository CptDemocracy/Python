"""
[ref.href] leetcode.com/problems/majority-element
"
  Given an array of size n, find the majority element. The majority element is the element that 
  appears more than ⌊ n/2 ⌋ times.
  
  You may assume that the array is non-empty and the majority element always exist in the array.
  
  Credits:
  Special thanks to @ts for adding this problem and creating all test cases.
"
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numdict = {}
        ln = len(nums)
        for num in nums:
            if num in numdict:
                numdict[num] += 1
            else:
                numdict[num] = 1
            if numdict[num] > ln // 2:
                return num
        return 0

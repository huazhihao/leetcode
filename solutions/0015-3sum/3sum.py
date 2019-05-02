# -*- coding:utf-8 -*-


# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
#


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        #print(nums)
        l = len(nums)
        if l > 2 and nums[0] == 0 and nums[l-1] == 0:
            return [(0,0,0)]
        for i in range(0, l - 2):
            j = i + 1
            k = l - 1
                
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                #print(i,j,k,s)
                if s == 0:
                    results.append((nums[i],nums[j],nums[k]))
                if s <= 0:
                    j += 1
                elif s > 0:
                    k -= 1
                
        return list(set(results))

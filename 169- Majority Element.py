'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

 '''
class Solution(object):
    def majorityElement(self, nums):
        d={}
        for i in set(nums):
            d[i]=nums.count(i)
        return (d.keys()[d.values().index(max(d.values()))])
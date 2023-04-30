# this  is the two sum problem with a reference of
# 1. Two Sum in leet code , its an easy one  with a
#  time complexity of O(n) and a space complexity of O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}            
        for i,num in enumerate(nums):
            n = target - num 
            if n not in h:
                h[num] = i
            else:
                 return[h[n], i]

print(h)
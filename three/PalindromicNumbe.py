# -*- coding: utf-8 -*-
"""
@Time ： 2024/10/12 17:47
@Auth ： Wudapeng
@File ：PalindromicNumbe.py
@IDE ：PyCharm
"""


class PalindromicNumbe(object):
    def oneSolution(self, nums: list[int]):
       numLen=len(nums)
       if numLen%2==0:
           for i in range(numLen//2):
               if nums[i]!=nums[-1-i]:
                   return False
       return True

    def twoSolution(self, nums: list[int]):
        tep=nums[::-1]
        return True if tep==nums else False

    def threeSolution(self, nums: list[int]):
        tep=list(reversed(nums))
        return True if tep==nums else False


if __name__ == '__main__':
    palindromicNumbe=PalindromicNumbe()
    nums=[1,2,2,3,2,1]
    # print(palindromicNumbe.oneSolution(nums))
    print(palindromicNumbe.threeSolution(nums))

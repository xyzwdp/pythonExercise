# -*- coding: utf-8 -*-
"""
@Time ： 2024/10/12 16:51
@Auth ： Wudapeng
@File ：TwoNumXOR.py
@IDE ：PyCharm
"""

class TwoNumXOR(object):
    def oneXoR(self,nums):
        resList=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]==nums[i]:
                    resList.append(nums[j])
                    break
        if not resList:
            resList.append(0)
        return resList


if __name__ == '__main__':
    nums=[1,2,3,4,4,1]
    twoNumXOR=TwoNumXOR()
    print(twoNumXOR.oneXoR(nums))
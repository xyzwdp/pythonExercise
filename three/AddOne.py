# -*- coding: utf-8 -*-
"""
@Time ： 2024/10/18 11:09
@Auth ： Wudapeng
@File ：AddOne.py
@IDE ：PyCharm
"""
"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
"""


class AddOne(object):
    def oneSolution(self, nums: list[int]):
        temp = nums[-1] + 1
        if temp > 9:
            nums[-1] = 1
            nums.append(0)
            return nums
        nums[-1] = temp
        return nums


if __name__ == '__main__':
    addOne = AddOne()
    nums = [1, 3, 5, 9]
    print(addOne.oneSolution(nums))

# -*- coding: utf-8 -*-
"""
@Time ： 2024/10/17 16:50
@Auth ： Wudapeng
@File ：SearchInsert.py
@IDE ：PyCharm
"""

"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
"""


class SearchInsert(object):
    def oneSolution(self, nums: list[int], target: int):
        if target in nums:
            return nums.index(target)
        nums.append(target)
        return nums


if __name__ == '__main__':
    searchInsert = SearchInsert()
    nums = [1, 3, 5, 7, 4]
    target = 9
    print(searchInsert.oneSolution(nums, target))

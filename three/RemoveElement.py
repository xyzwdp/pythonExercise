# -*- coding: utf-8 -*-
"""
@Time ： 2024/10/14 11:14
@Auth ： Wudapeng
@File ：RemoveElement.py
@IDE ：PyCharm
"""
"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。

假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：

更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
"""

class RemoveElement(object):
    def oneSolution(self, nums:list, val):
        k = nums.count(val)
        i = 1
        while i <= k:
            nums.remove(val)
            nums.append('_')
            i += 1
        return k, nums
    def twoSolution(self, nums:list, val):
        a=0
        b=0
        while a<len(nums):
            if nums[a]!=val:
                nums[b]=nums[a]
                b+=1
            a+=1
        return b,nums


if __name__ == '__main__':
    removeElement = RemoveElement()
    nums = [1, 3, 4, 5, 4]
    val = 4
    # print(f"总计有：{removeElement.oneSolution(nums, val)[0]} 相等的val")
    # print(f"处理后的列表为：{removeElement.oneSolution(nums, val)[1]}")
    print(removeElement.twoSolution(nums,val))

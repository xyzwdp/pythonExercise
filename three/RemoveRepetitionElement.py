# -*- coding: utf-8 -*-
"""
@Time ： 2024/10/14 15:13
@Auth ： Wudapeng
@File ：RemoveRepetitionElement.py
@IDE ：PyCharm
"""
"""
删除列表中重复元素
"""


class RemoveRepetitionElement(object):
    def oneSolution(self, nums: list):
        resNums = []
        for i in nums:
            if i not in resNums:
                resNums.append(i)

        return resNums

    def twoSolution(self, nums: list):
        resNums = list(set(nums))
        return resNums

    def threeSolution(self, nums: list):
        """
        双指针解决办法
        :param nums:
        :return:
        """
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow



if __name__ == "__main__":
    removeRepetitionElement = RemoveRepetitionElement()
    nums = [1, 1, 1, 2, 2, 7]
    # print(removeRepetitionElement.oneSolution(nums))
    # print(removeRepetitionElement.twoSolution(nums))
    print(removeRepetitionElement.threeSolution(nums))

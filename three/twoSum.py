# -*- coding: utf-8 -*-
"""
@Time ： 2024/9/9 15:35
@Auth ： Wudapeng
@File ：twoSum.py
@IDE ：PyCharm
"""


class TwoSum(object):
    def twoSum1(self, nums, target):
        """
        给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标
        你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素
        :param nums:
        :param target:
        :return:
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    print("符合要求元素索引为：[{},{}]".format(i, j))
        return

    def twoSum2(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            """遍历比较num_dict字典中某个键是否与complement相等，相等则打印对应的值"""
            if complement in num_dict:
                print(num_dict[complement], i)
                # return [num_dict[complement], i]
            num_dict[num] = i
        print(num_dict)
        return

    def a(self):
        a = {1: 2, "wo": "ni"}
        if "ni" in a:
            print("是")
        else:
            print("no")

    def twoSum3(self, l1, l2):
        """ 列表倒序处理,使用reverse在原列表中修改 """
        l1.reverse()
        l2.reverse()
        """列表数字提取出来组成整数"""
        num1 = 0
        for digit in l1:
            num1 = num1 * 10 + digit
        """使用int(''.join(map(str, l2)))方法把列表中数字提取出来变成整数"""
        num2 = int(''.join(map(str, l2)))
        # print(map(str, l2))
        # print(''.join(map(str, l2)))
        # print(num2)
        rs = num1 + num2
        """列表推导公式把字符串数字一个个添加到列表"""
        tg = [int(x) for x in str(rs)]
        """使用切片方式列表倒序处理"""
        rsList = tg[::-1]
        print(rsList)


if __name__ == '__main__':
    twoSum = TwoSum()
    nums = [2, 1, 7, 6, 9, 8, 3]
    num2 = [9, 9, 9, 9, 9, 9, 9]
    num1 = [9, 9, 9, 9]
    target = 9
    # twoSum.twoSum1(nums, target)
    # twoSum.twoSum2(nums, target)
    # twoSum.a()
    twoSum.twoSum3(num1, num2)

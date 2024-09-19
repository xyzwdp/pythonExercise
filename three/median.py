# -*- coding: utf-8 -*-
"""
@Time ： 2024/9/10 18:22
@Auth ： Wudapeng
@File ：median.py
@IDE ：PyCharm
"""


class Median(object):
    def median(self, nums1: list, nums2: list):
        """
        24
        :param nums1:
        :param nums2:
        :return:
        """
        """合并数组"""
        nums = nums1 + nums2
        n = len(nums)
        """冒泡法对列表数值大小排序"""
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        """插入排序法对列表进行快速排序"""

        """使用sort方法对列表大小进行排序"""
        # nums.sort()

        """使用sorted对列表进行排序生成新的列表"""
        # newNums=sorted(nums)

        # 判断列表长度是偶数还是奇数
        if n % 2 == 0:
            medianNum = (nums[n / 2] + nums[(n / 2) - 1]) / 2
            print(nums)
            print(medianNum)
        else:
            medianNum = nums[n // 2]
            print(nums)
            print(medianNum)


if __name__ == '__main__':
    nums1 = [2, 4, 5, 1, 6, 9, 2]
    nums2 = [1, 6, 9, 3, 2, 1]
    median = Median()
    median.median(nums1, nums2)

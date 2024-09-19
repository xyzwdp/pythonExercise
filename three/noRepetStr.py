# -*- coding: utf-8 -*-
"""
@Time ： 2024/9/10 15:20
@Auth ： Wudapeng
@File ：noRepetStr.py
@IDE ：PyCharm
"""


class Solution(object):
    def noRepetStr(self,s):
        """
        给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串的长度。
        使用滑动窗口算法解决
        :param s:
        :return:
        """
        char_index_map = {}
        max_length = 0
        start = 0

        for end in range(len(s)):
            """判断字符串最新的是否有与前面重复值"""
            if s[end] in char_index_map:
                """更新起始位置为重复字符上一次出现的位置的后一位"""
                start = max(start, char_index_map[s[end]] + 1)
                print(start)
            """把字符串中值作为字典的键，索引作为值存储"""
            char_index_map[s[end]] = end
            print(char_index_map)
            """在遍历过程中，不断更新最长子串的长度。"""
            max_length = max(max_length, end - start + 1)

        print(max_length)


if __name__ == '__main__':
    solution = Solution()
    s = "pppppp"
    solution.noRepetStr(s)

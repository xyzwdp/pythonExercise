# -*- coding: utf-8 -*-
"""
@Time ： 2024/10/17 17:32
@Auth ： Wudapeng
@File ：FinalWordWength.py
@IDE ：PyCharm
"""
"""
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
单词 是指仅由字母组成、不包含任何空格字符的最大子字符串.
"""


class FinalWordWength(object):
    def oneSolution(self, strs: str):
        temp = strs[::-1]
        i = 0
        while i < len(temp):
            if temp[i]:
                j = i
                while i < len(temp):
                    print(temp[i])
                    if not temp[i]:
                        return i
                    i += 1

            i += 1
        return False

    def twoSolution(self, strs: str):
        # strs.strip()
        s=strs.split()
        return len(s[-1])



if __name__ == '__main__':
    finalWordWength = FinalWordWength()
    strs = "aa ss fsf dcfc "
    # print(finalWordWength.oneSolution(strs))
    print(finalWordWength.twoSolution(strs))

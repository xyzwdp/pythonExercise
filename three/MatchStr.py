# -*- coding: utf-8 -*-
"""
@Time ： 2024/10/15 20:29
@Auth ： Wudapeng
@File ：MatchStr.py
@IDE ：PyCharm
"""


class MatchStr(object):
    def oneSolution(self, str1: str, str2: str):
        index = 0
        while index < len(str1) - len(str2) + 1:
            if str1[index] == str2[0]:
                if str1[index:len(str2) + index] == str2:
                    return True
            index += 1
        return False
    def twoSolution(self, str1: str, str2: str):

        pass


if __name__ == "__main__":
    matchStr = MatchStr()
    str1 = "sssssssa"
    str2 = "a"
    print(matchStr.oneSolution(str1, str2))

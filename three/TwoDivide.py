# -*- coding: utf-8 -*-
"""
@Time ： 2024/10/16 11:16
@Auth ： Wudapeng
@File ：TwoDivide.py
@IDE ：PyCharm
"""


class TwoDivide(object):
    def oneSolution(self, num1, num2):
        res = num1 // num2
        if res < 0:
            return res + 1
        return res


if __name__ == "__main__":
    twoDivide = TwoDivide()
    num1 = 0
    num2 = 2
    print(twoDivide.oneSolution(num1, num2))

# -*- coding: utf-8 -*-
"""
@Time ： 2024/10/15 18:16
@Auth ： Wudapeng
@File ：ValidBracket.py
@IDE ：PyCharm
"""

class ValidBracket(object):
    def oneSolution(self,strs:str):
        if len(strs)%2!=0:
            return False
        leftBracket=["(","[","{"]
        i=0
        while i<len(strs)/2:
            if strs[0] not in leftBracket:
                return False
            elif strs[0]==leftBracket:
                pass
        pass

    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack



if __name__ == '__main__':
    validBracket=ValidBracket()
    strs="[]()"
    print(validBracket.isValid(strs))


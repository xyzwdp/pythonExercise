# -*- coding: utf-8 -*-
"""
@Time ： 2024/10/18 15:10
@Auth ： Wudapeng
@File ：BinaryComput.py
@IDE ：PyCharm
"""
class BinaryComput(object):
    # def oneSolution(self,num1:str,num2:str):
    #     maxlen=max(len(str(num1)),len(str(num2)))
    #     i=0
    #     snum1=str(num1)
    #     snum2=str(num2)
    #     res = ""
    #     while i<maxlen:
    #         scale = 0
    #         temp=num2[i-1]+num1[i-1]+scale
    #         if temp>=2:
    #             res[i-1]=1
    #             scale=temp-1
    #         res[i-1]=temp
    #     print(res)
    def twoSolution(self,num1,num2):
        return '{0:b}'.format(int(num1, 2) + int(num2, 2))






if __name__ == '__main__':
    binaryComput=BinaryComput()
    num1=0b111001
    num2=0b111
    # binaryComput.oneSolution(num1, num2)
    binaryComput.twoSolution(num1, num2)

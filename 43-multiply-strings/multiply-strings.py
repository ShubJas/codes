class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        

        if '0' in [num1,num2]:
            return '0'

        n1 = len(num1)
        n2 = len(num2)

        num1, num2 = num1[::-1], num2[::-1]

        result = [0] * (n1 + n2)


        for i1 in range(n1):
            for i2 in range(n2):


                result[i1+i2] += int(num1[i1]) * int(num2[i2])
                result[i1 + i2 + 1] += result[i1+i2] // 10
                result[i1+i2] %= 10

        result = result[::-1]
        start = 0
        while result[start] == 0:
            start +=1
        result = map(str,result[start:])
        return ''.join(result)  




# class Solution:
#     def multiply(self, num1: str, num2: str) -> str:
        
#         return str(int(num1)*int(num2))
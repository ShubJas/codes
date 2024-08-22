class Solution:
    def findComplement(self, num: int) -> int:

        binary = bin(num)[2:]
        # binary = list(binary)
        result = []
        # print(binary)


        for ch in binary:
            if ch=='1':
                result.append('0')
            else:
                result.append('1')
        
        result = ''.join(result)
        print(result)

        return int(result,2)
class Solution:
    def findComplement(self, num: int) -> int:

        binary = bin(num)[2:]
        binary = list(binary)
        # print(binary)


        for i in range(len(binary)):
            if binary[i]=='1':
                binary[i] = '0'
            else:
                binary[i] = '1'
        
        binary = ''.join(binary)
        # print(binary)

        return int(binary,2)
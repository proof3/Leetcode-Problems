class Solution:
    def reverseBits(self, n: int) -> int:
        new_n = 0
        i = 0
        while n > 0:
            new_n += int(n % 2) * pow(2,31 - i)
            n = int(n/2)
            i+=1
            
        return new_n

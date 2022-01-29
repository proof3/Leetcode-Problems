class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i > -1 or j > -1:
            char_a = int(a[i]) if i > -1 else 0
            char_b = int(b[j]) if j > -1 else 0
            add = char_a + char_b + carry
            carry = 1 if add > 1 else 0  
                
            res =  "1" + res if add == 3 or add == 1 else "0" + res
            
            i -= 1
            j -= 1
            
        if carry != 0:
            res = str(carry) + res 
                
        return res
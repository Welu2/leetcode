class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            a=[]
            for i in s:
                if i =='0':
                    a.append("1")
                else:
                    a.append("0")
            return "".join(reversed(a))
        def Kth_bit(n,k):
            if n == 1:
                return "0"
            else:
                value="0"
                count=2
                while count <= n:
                    value= value+"1"+invert(value)
                    count+=1

                return value[k-1]

        return Kth_bit(n,k)
       
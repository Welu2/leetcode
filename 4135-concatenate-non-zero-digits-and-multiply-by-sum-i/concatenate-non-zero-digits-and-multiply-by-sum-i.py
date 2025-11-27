class Solution:
    def sumAndMultiply(self, n: int) -> int:
        ar=["0"]
        t=0
        for i in str(n):
            if i != "0":
                t+=int(i)
                ar.append(i)

        return int("".join(ar))*t

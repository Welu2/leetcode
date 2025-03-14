class Solution:
    def tribonacci(self, n: int) -> int:
        def T(n):
            if n ==1 or n==2:
                return 1
            if n == 0:
                return 0
            first=0
            sec=1
            third=1
            for i in range(3,n+1):
                first,sec,third=sec,third,(first+sec+third)

            return third
        return T(n)
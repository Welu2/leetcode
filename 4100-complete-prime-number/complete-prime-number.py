class Solution:
    def is_prime(self, n: int) -> bool:
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def completePrime(self, num: int) -> bool:
        s = str(num)
        length = len(s)

        # Check all prefixes and suffixes
        for i in range(1, length + 1):
            prefix = int(s[:i])
            suffix = int(s[length - i:])

            if not self.is_prime(prefix) or not self.is_prime(suffix):
                return False

        return True

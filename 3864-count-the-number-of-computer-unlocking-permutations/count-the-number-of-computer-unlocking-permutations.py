class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        freq=Counter(complexity)
        n=len(complexity )
        print(n)
        def factorial(n):
            if n == 1:
                return 1
            return n *factorial(n-1)

        if freq[complexity[0]] > 1 or  complexity[0] > min(complexity ):
            return 0
        else:
            return factorial(n-1) % (10**9+7)
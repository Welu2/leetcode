class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        total=0
        l=1
        while l <= len(happiness) and k >0:
            if l == 1:
                total+=happiness[-l]
                k-=1
            else:
                if happiness[-l]-(l-1) < 0:
                    break
                else:
                    total+=happiness[-l]-(l-1)
                    k-=1
            l+=1
        return total

class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        d=defaultdict(list)
        l=[]
        for i in nums:
            k=bin(i)[2:]

            l.append(int(k[::-1]))
            d[int(k[::-1])].append(i)
        l.sort()
        ans=[]
        seen=set()
        
        for j in l:
            if j not in seen:
                for u in sorted(d[j]):
                    ans.append(u)
            seen.add(j)

        return ans

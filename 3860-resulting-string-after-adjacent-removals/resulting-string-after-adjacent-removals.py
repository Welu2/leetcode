class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            
            if stack and abs(ord(stack[-1]) - ord(s[i])) == 1:
                stack.pop()
                continue
            elif stack and (stack[-1] == "z" and s[i] == "a"):
                stack.pop()
                continue
            elif stack and (stack[-1] == "a" and s[i] == "z"):
                stack.pop()
                continue

            stack.append(s[i])

        return "".join(stack) 
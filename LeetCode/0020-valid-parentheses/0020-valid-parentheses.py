class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        a = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in a.values():
                stack.append(c)
            elif c in a:
                if not stack or stack[-1] != a[c]:
                    return False
                stack.pop()
            else:
                return False
        return not stack
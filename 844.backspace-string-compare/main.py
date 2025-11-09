class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def trim(stack, c):
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
            
            return stack
        
        return reduce(trim, s, []) == reduce(trim, t, [])
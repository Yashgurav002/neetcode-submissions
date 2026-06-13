class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        cTOo={")":"(","]":"[","}":"{"}

        for c in s:
            if c in cTOo:
                if stack and stack[-1]==cTOo[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        
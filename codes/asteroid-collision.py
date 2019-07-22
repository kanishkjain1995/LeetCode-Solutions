class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for aster in asteroids:
            if stack == []:
                stack.append(aster)
            elif aster<0:
                while len(stack)>0 and stack[-1] > 0 and abs(aster) > abs(stack[-1]):
                    stack.pop()
                if stack == [] or stack[-1]<0:
                    stack.append(aster)
                elif stack[-1]+aster == 0:
                    stack.pop()
                    
            else:
                stack.append(aster)
        return stack

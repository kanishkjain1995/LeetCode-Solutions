class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slot = 1
        preorder = preorder.split(",")
        for s in preorder:
            if slot == 0:
                return False
            if s == '#':
                slot-=1
            else:
                slot+=1
        return slot==0

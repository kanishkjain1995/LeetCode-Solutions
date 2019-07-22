class Solution(object):
    def candy(self, rat):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n=len(rat)
        if n==1:
            return 1
        num=[1]*n
        for i in xrange(1,n):
            if rat[i]>rat[i-1]:
                num[i]=num[i-1]+1
        for i in xrange(n-1,0,-1):
            if rat[i-1]>rat[i]:
                num[i-1]=max(num[i]+1,num[i-1])
        return sum(num)

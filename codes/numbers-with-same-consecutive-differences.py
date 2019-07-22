class Solution:
    def numsSameConsecDiff(self, N, K):
        result = []
        if N == 1:
            return [x for x in range(0,10)]
        def insert(num,n,k,result):
            if n == 0:
                if num not in result:
                    result.append(num)
                return
            else:
                d = num%10
                if d+k < 10:
                    insert(10*num + (d+k),n-1,k,result)
                if d-k >= 0:
                    insert(10*num + (d-k),n-1,k,result)
                
        for d in range(1,10):
            insert(d,N-1,K,result)
        return result

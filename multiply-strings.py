class Solution:
    def multiply(self, a, b):
        flag_a, flag_b = 0, 0
        if a[0] == "-":
            flag_a = 1
            a = a[1:]
        if b[0] == "-":
            flag_b = 1
            b = b[1:]
        l1,l2 = len(a),len(b)
        result = 0
        memo = [0]*10
        for i in range(len(memo)):
            sum_ = 0
            carry = 0
            k = 0
            for j in range(l2-1,-1,-1):
                mul = int(b[j])*i
                sum_ = sum_ + (10**k)*(mul%10 + carry)
                carry = mul//10
                k += 1
            sum_ += (10**k)*carry
            memo[i] = sum_
        for i in range(l1-1,-1,-1):
            result += (10**(l1-1-i))*memo[int(a[i])]
        if flag_a == flag_b:
            return str(result)
        else:
            return str(-1*result)

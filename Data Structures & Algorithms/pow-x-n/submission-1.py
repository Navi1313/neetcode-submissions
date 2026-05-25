class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow1(base , expo):
            if expo == 0:
                return 1.0
            half = pow1(base , expo//2)

            if expo % 2 == 0 :
                return half*half
            else:
                return half*half*base

        return pow1(x, n)  if n >=0 else 1.0/pow1(x , -n)          
            
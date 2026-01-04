class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        result=0
        for num in nums:
            d=set()
            for i in range(1,int(num**0.5)+1):
                if num%i==0:
                    d.add(i)
                    d.add(num//i)
                if len(d)>4:
                    break
            if len(d)==4:
                result+=sum(d)
        return result
            

            
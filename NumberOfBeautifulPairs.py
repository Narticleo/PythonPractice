class Solution(object):
    def gcd(self,m,n):
        if n==0:
            return m
        else:
            return self.gcd(n,m%n)
        
    def countBeautifulPairs(self, nums):
        pairs = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if self.gcd(int(str(nums[i])[0]),nums[j]%10) == 1:
                    print(nums[i],nums[j])
                    pairs+=1
        return pairs


nums = [31,25,72,79,74]
solution = Solution()
print(solution.countBeautifulPairs(nums))
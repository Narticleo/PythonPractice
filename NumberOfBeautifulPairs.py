import math 
class Solution(object):   
    def countBeautifulPairs(self, nums):
        pairs = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if math.gcd(int(str(nums[i])[0]),nums[j]%10) == 1:
                    print(nums[i],nums[j])
                    pairs+=1
        return pairs

nums = [31,25,72,79,74]
solution = Solution()
print(solution.countBeautifulPairs(nums))

class Solution(object):
    def countSeniors(self, details):
        nums = 0
        for i in range(0,len(details)):
            if int(details[i][11:13]) > 60 :
                nums+=1
        return nums
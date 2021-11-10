from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.CalculatePeak(nums,0,len(nums)-1)
    def CalculatePeak(self,nums:List[int],start:int,end:int)->int:
        if(start>end):
            return None
        midpoint=start+int((end-start)/2)
        print(nums[midpoint])
        if(midpoint-1>=0 and nums[midpoint]<nums[midpoint-1]):
            print("Going left")
            return self.CalculatePeak(nums,start,midpoint-1)
        elif(midpoint+1<len(nums) and nums[midpoint]<nums[midpoint+1]):
            print("Going right")
            return self.CalculatePeak(nums,midpoint+1,end)
        else:
            print("Found", midpoint)
            return midpoint
sol=Solution()
print(sol.findPeakElement([1]))

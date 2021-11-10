from typing import List


class Solution:
    def findPeakElement(self, nums: List[List[int]]) -> int:
        return self.Calculate2DPeak(nums, 0, len(nums[0])-1)

    def Calculate1DPeak(self, nums: List[List[int]], start: int, end: int, col: int) -> int:
        if(start > end):
            return None
        midpoint = int((start+end)/2)
        print(midpoint, col)
        if(midpoint-1 >= 0 and nums[midpoint][col] < nums[midpoint-1][col]):
            print("Going top 1D")
            return self.Calculate1DPeak(nums, start, midpoint-1, col)
        elif(midpoint+1 < len(nums) and nums[midpoint][col] < nums[midpoint+1][col]):
            print("Going bottom 1D")
            return self.Calculate1DPeak(nums, midpoint+1, end, col)
        else:
            print("Found 1D", midpoint)
            return midpoint

    def Calculate2DPeak(self, nums: List[List[int]], start: int, end: int) -> int:
        if(start > end):
            return None
        midpoint = int((start+end)/2)
        print(midpoint)
        xMax = self.Calculate1DPeak(nums, 0, len(nums)-1, midpoint)
        if(midpoint-1 >= 0 and nums[xMax][midpoint] < nums[xMax][midpoint-1]):
            print("Going left")
            return self.Calculate2DPeak(nums, start, midpoint-1)
        elif(midpoint+1 < len(nums[0]) and nums[xMax][midpoint] < nums[xMax][midpoint+1]):
            print("Going right")
            return self.Calculate2DPeak(nums, midpoint+1, end)
        else:
            print("Found", xMax, midpoint)
            return [xMax, midpoint]


sol = Solution()
print(sol.findPeakElement([[36, 15, 44, 21, 50], [50, 4, 15, 3, 21], [
      26, 18, 5, 14, 37], [46, 21, 14, 42, 32], [26, 42, 30, 10, 17]]))

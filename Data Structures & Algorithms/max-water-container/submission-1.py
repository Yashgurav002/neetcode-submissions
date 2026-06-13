class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r= 0,len(heights)-1
        res=0

        while l<r:
            area=(r-l)*min(heights[r],heights[l]) #minimum height of both left and right
            res= max(area,res)
            if heights[l] < heights[r]:
                l+=1
            elif heights[l]> heights[r]:
                r-=1
            else:
                r-=1

        return res
        
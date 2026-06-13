class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=r # not to zero as we should have atleast one sol

        while l<=r:
            k=(l+r)//2
            #now check at this k how many hours will it take to 
            # eat the bananas
            hours=0
            for p in piles:
                hours+=math.ceil(p/k)
            if hours<=h:
                res=min(res,k)
                r=k-1
            else:
                l=k+1
        return res
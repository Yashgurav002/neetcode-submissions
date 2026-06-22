class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count = {}
        res = []

        for n in nums:
            count[n] = count.get(n,0) + 1


        for n in count:
            if count[n] > len(nums)//3:
                res.append(n)

        return res
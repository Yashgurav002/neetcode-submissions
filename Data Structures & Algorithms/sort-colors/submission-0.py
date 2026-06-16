class Solution:
    def sortColors(self, nums: List[int]) -> None:

        count=[0] *3

        for n in nums:
            count[n]+=1

        index=0

        for i in range(count[0]):
            nums[index]=0
            index+=1
        for i in range(count[1]):
            nums[index]=1
            index+=1
        for i in range(count[2]):
            nums[index]=2
            index+=1
        """
        Do not return anything, modify nums in-place instead.
        """
        
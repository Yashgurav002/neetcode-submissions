class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap ={} #Value: Index

        for i,n in enumerate(nums):
            diff= target - n # if difference is already present in hashmap
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return 

        
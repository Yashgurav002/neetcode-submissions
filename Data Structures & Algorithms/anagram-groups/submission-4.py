class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}

        for s in strs:
            count =[0]*26 # count array with 26 zeros

            for char in s:
                index= ord(char)- ord('a') # ascii value
                count[index]+=1

            key=tuple(count) # key is tuple of count [1,0,0,0,0,0,0,1.....]

            if key not in groups:
                groups[key]=[]

            groups[key].append(s)

        return list(groups.values())
        
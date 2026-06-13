class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1Count = {}
        window = {}

        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1


        l = 0

        for r in range(len(s2)):

            # add right character
            window[s2[r]] = window.get(s2[r], 0) + 1


            # keep window size same as s1
            if r - l + 1 > len(s1):

                window[s2[l]] -= 1

                if window[s2[l]] == 0:
                    del window[s2[l]]

                l += 1


            # compare
            if window == s1Count:
                return True


        return False
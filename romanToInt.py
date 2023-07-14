class Solution:
    def romanToInt(self, s: str):
        dictionary = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        
        s = list(s)
        summed_value = 0
        for i,key in enumerate(s):   
            if (i+1 < len(s) and dictionary[key] < dictionary[s[i+1]]):
                summed_value -= dictionary[key]
            else:
                summed_value += dictionary[key]
        return summed_value

solution = Solution()
'''
Created on: Saturday, September 01, 2018
@author: Jedi Liu
'''


class Solution1:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        n = num
        roman = ""
        div = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = [
            "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV",
            "I"
        ]
        while n != 0:
            for i in range(len(div)):
                d = div[i]
                times = n // d
                if times != 0:
                    roman = roman + (times) * romans[i]
                    n = n - d * times
        return roman


s = Solution1()
print(s.intToRoman(1234))

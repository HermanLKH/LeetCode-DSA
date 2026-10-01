class Solution:
    def intToRoman(self, num: int) -> str:
        conversions = {
            1:    'I',
            4:    'IV',
            5:    'V',
            9:    'IX',
            10:   'X',
            40:   'XL',
            50:   'L',
            90:   'XC',
            100:  'C',
            400:  'CD',
            500:  'D',
            900:  'CM',
            1000: 'M'
        }
        x = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        roman_num = ''

        while x:
            while num >= x[-1]:
                num -= x[-1]
                roman_num += conversions[x[-1]]
            else:
                x.pop()
                
        return roman_num


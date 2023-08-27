class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        sym = [(1,'I'),(4,'IV'),(5,'V'),(9,'IX'),
               (10,'X'),(40,'XL'),(50,'L'),(90,'XC'),
               (100, 'C'),(400,'CD'),(500, 'D'),(900, 'CM'),
               (1000, 'M')]
        
        i = len(sym)-1
        res = []
        while num:
            quo = num // sym[i][0]
            res.append(sym[i][1]*quo)
            num = num % sym[i][0]
            i -= 1
        return ''.join(res)
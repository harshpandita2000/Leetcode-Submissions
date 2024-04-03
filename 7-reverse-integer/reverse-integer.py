class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        neg = x < 0
        if neg:
            x = -x

        reversed_x = 0
        while x != 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10

        if neg:
            reversed_x = -reversed_x

        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        else:
            return reversed_x
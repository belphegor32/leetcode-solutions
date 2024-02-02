class Solution(object):
    def sequentialDigits(self, low, high):
        res = []
        # max and min len of the number
        start_digit = len(str(low))
        end_digit = len(str(high))

        for digit in range(start_digit, end_digit + 1):

            # iterate thru all possible starting digets
            # if the starting digit + len of number that we need to make is > 10, it means we cant create a number
            
            for start in range(1, 9):
                if start + digit > 10:
                    break
                num = start
                newDigit = start

                for i in range(digit - 1):
                    num = num * 10
                    newDigit += 1
                    num += newDigit

                if num >= low and num <= high:
                    res.append(num)

        return res 
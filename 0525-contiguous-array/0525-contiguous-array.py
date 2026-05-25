def findMaxLength(nums):
        sum = 0
        freq = {}
        longcont = 0
        for i,num in enumerate(nums):
            if num == 0:
                k = -1
            else:
                k = 1
            sum = sum+k
            if sum == 0:
                cont = i+1
                longcont = max(cont,longcont)
            if sum in freq:
                cont = i- freq[sum]
                longcont = max(cont,longcont)
            else:
                freq[sum] = i
        return longcont

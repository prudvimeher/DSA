def runningSum(nums):
        sum = 0
        output = []
        for num in nums:
          sum +=num
          output.append(sum)
        return output
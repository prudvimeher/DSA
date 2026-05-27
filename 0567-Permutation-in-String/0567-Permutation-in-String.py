from collections import Counter
def checkInclusion(s1, s2):
        if len(s1) > len(s2):
            return False

        freqs1 = Counter(s1)
        freqs2 = Counter()

        required = len(freqs1)
        matched = 0
        left = 0
        window_size = len(s1)

        for right in range(len(s2)):
            char = s2[right]
            freqs2[char] += 1

            if char in freqs1:
                if freqs2[char] == freqs1[char]:
                    matched += 1
                elif freqs2[char] == freqs1[char] + 1:
                    matched -= 1

            if right - left + 1 > window_size:
                leftchar = s2[left]

                if leftchar in freqs1:
                    if freqs2[leftchar] == freqs1[leftchar]:
                        matched -= 1

                freqs2[leftchar] -= 1

                if leftchar in freqs1:
                    if freqs2[leftchar] == freqs1[leftchar]:
                        matched += 1

                left += 1

            if matched == required:
                return True

        return False
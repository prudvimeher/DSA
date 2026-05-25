from collections import Counter
def minWindow(s, t):
        if not t:
            return ""

        freqt = Counter(t)              # target requirements
        required = len(freqt)           # distinct conditions to satisfy

        window_freq = {}
        matched = 0

        left = 0

        best_len = float('inf')
        best_start = 0

        for right in range(len(s)):
            char = s[right]

            if char in freqt:
                window_freq[char] = window_freq.get(char, 0) + 1

                if window_freq[char] == freqt[char]:
                    matched += 1

            while matched == required:
                current_len = right - left + 1

                if current_len < best_len:
                    best_len = current_len
                    best_start = left

                left_char = s[left]

                if left_char in freqt:
                    window_freq[left_char] -= 1

                    if window_freq[left_char] < freqt[left_char]:
                        matched -= 1

                left += 1

        if best_len == float('inf'):
            return ""

        return s[best_start:best_start + best_len]
print(minWindow("ADOBECODEBANC", "ABC"))
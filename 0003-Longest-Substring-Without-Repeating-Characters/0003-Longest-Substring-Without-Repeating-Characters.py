def lengthOfLongestSubstring(s):
    st = set()
    i = 0
    max_length = 0
    for j in range(len(s)):
        while s[j] in st:
            st.remove(s[i])
            i = i+1
        st.add(s[j])
        length = j-i+1
        max_length = max(max_length,length)
    return max_length
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
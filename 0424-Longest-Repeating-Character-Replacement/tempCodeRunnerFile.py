def characterReplacement(s, k) :
    mostfreq = 0
    freq = {}
    l = 0
    maxwindow = 0
    for r in range(len(s)):
        if s[r] in freq:
            freq[s[r]] += 1
        else: 
            freq[s[r]] = 1
        mostfreq = max(freq[s[r]],mostfreq)
        windowsize = r-l+1
        diff = windowsize-mostfreq
        while diff > k:
            freq[s[l]] -=1
            l = l+1
            windowsize = r-l+1
            diff = windowsize-mostfreq  
        else :
            maxwindow = max(windowsize,maxwindow)
    return maxwindow   
print(characterReplacement("AABABBA", 1))      
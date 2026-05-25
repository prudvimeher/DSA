# Minimum Window Substring

## Approach

This solution uses the **Sliding Window** technique with two pointers (`left`, `right`) and frequency maps.

- `freqt` stores required character counts from `t`
- `window_freq` stores character counts inside the current window
- `matched` tracks how many character requirements are satisfied

We expand the window using `right`.  
Once all required characters are present (`matched == required`), we shrink the window from the left to find the minimum valid substring.

---

# Key Logic

## Store target frequencies

```python
freqt = Counter(t)
required = len(freqt)
```

## Expand window

```python
for right in range(len(s)):
```

## Update frequency

```python
window_freq[char] = window_freq.get(char, 0) + 1
```

## Valid window

```python
if window_freq[char] == freqt[char]:
    matched += 1
```

## Shrink window

```python
while matched == required:
```

Update answer and move `left` pointer to minimize the window.

---

# Time Complexity

```python
O(n)
```

# Space Complexity

```python
O(k)
```

Where `k` is the number of distinct characters in `t`.

---

# Example

```python
Input:
s = "ADOBECODEBANC"
t = "ABC"

Output:
"BANC"
```
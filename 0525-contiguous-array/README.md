# Contiguous Array — Approach (Short)

## 🧠 Core Idea

Convert:

* `1 → +1`
* `0 → -1`

Now the problem becomes:

> Find the longest subarray with **sum = 0**

---

## 💡 Key Observation

If the same prefix sum appears at two indices:

```
prefix_sum[i] == prefix_sum[j]
```

Then:

```
subarray (i+1 → j) has sum = 0
```

---

## ⚙️ Method

* Keep a running `sum`
* Use a hash map:

  ```
  sum → first index where it appeared
  ```
* At each index:

  * If `sum == 0` → valid from start
  * If `sum seen before` → compute length
  * If not seen → store index

---

## ⚠️ Important

* Store only the **first occurrence** of sum
* Length = `current_index - previous_index`

---

## ⏱️ Complexity

* Time: `O(n)`
* Space: `O(n)`

---

## 🎯 Takeaway

> Convert equality → sum
> Track prefix sum
> Repeated state ⇒ valid subarray

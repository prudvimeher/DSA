## 🧠 Core Idea

Use a **running cumulative sum**.

Instead of recalculating the sum from the beginning for every position, keep a running total as we traverse the array once.

Each new element contributes to the previous total, so we can build the answer incrementally.

---

## 💡 Key Observation

For any index `i`:

```text
runningSum[i] = runningSum[i-1] + nums[i]
```

This means:

* previous computation can be reused
* no repeated summation is needed
* one pass is enough

---

## ⚙️ Method

1. Initialize a variable to store the cumulative sum.
2. Create an output list.
3. Traverse the input array from left to right.
4. Add the current number to the cumulative sum.
5. Append the updated sum to the output list.
6. Return the final output list.

---

## ⚠️ Important

The key idea is **incremental computation**.

Avoid this inefficient approach:

* For each index, summing all previous elements again

That would repeatedly recompute work.

Also:
Avoid using `sum` as a variable name in production code since it shadows Python’s built-in `sum()` function.

A better name would be:

```python
running_sum
```

---

## ⏱️ Complexity

* Time: **O(n)**
  Each element is processed exactly once.

* Space: **O(n)**
  Extra output array stores the running sums.

---

## 🎯 Takeaway

This is a classic example of:

> Reuse previous computation instead of recomputing from scratch.

This pattern appears in:

* Prefix Sum
* Dynamic Programming
* Streaming computations

The mental model:
**carry forward state as you iterate.**

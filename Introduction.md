# Introduction

Data Structures are building blocks or raw material for any software program.

One cannot become a good programmer without sound understaing of the data structure.

**Data Structures** are containers storing data in a specific memory layout such as linear , tree-like layout, book-stack, queue-like layout.

# Big **O** Notation

It is a way to measure how running time or space requirement for your program grow as input size grows.

### 🔑 Two Key Points

**1 🔑** : Keep the fastest growing term.

**2 🔑** : Drop the constant

**Example :**

Say, time complexity of a program is = $ a \* n^2 + b $

We will only consider the fastest growing term, $n^2$, in the above equation and we will drop the constants which are `a` and `b`.

Hence, time complexity = O($ n^2$) for $ a \* n^2 + b $

**Note: O(1) is refered as constant time complexity**

There is one more important concept like time complexity. It is space complexity.

Space complexity is measured in a similar way to time complexity. While time complexity represents how the execution time of an algorithm grows as the input size increases, space complexity represents how the memory requirement of an algorithm grows with respect to the input size.

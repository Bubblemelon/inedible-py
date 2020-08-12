# The Python Language Paradigms

When it comes to using Python, I get the sense of freedom that I don't get with Java, C, or C++. However, with such
freedom comes the dilemma of having too many choices, or in the way that Schwartz phrases it as, "the paradox of choice".

In my endeavor to narrow down the best approaches for solving various types of problems, I sought out to understand
programming paradigms.

These are my notes that I compiled together from a myriad of sources.

### [Imperative](#Imperative)

- [Computation order is crucial][9] i.e. when variables are referred to or changed.
- Different consequences result from different sequences of instruction.
  - This is based on the current values of variables when a instruction is executed.
- This paradigm closely resembles the machine itself.
- [Stateful programming model][10] e.g. each instruction step can represent a state of the program.
- The "how-to-solve" approach".
- Centered around the mutation of state or data in memory location.

For example:
```python
numbers = [1,2,3,4,5]
sum = 0
for n in numbers:
    sum += n
print sum
# 15
```
`sum`'s state which initially stored the numeric value `0` is now mutated to `15`.
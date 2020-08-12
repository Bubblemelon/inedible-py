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

### [Functional](#Functional)

- [Primary means of computing is by applying functions to given parameters][2].
- Evaluates mathematical functions based on [lambda calculus][10].
  - A computational expression that uses function abstraction and applies variable binding and substitution.
- Function application and reduction model of computation.
- Functions can be treated as data e.g. as parameters, input, where functions can return functions, and be built upon.
- Promotes stateless functions.
  - However, Python is an [impure functional language][10]
    - It's possible to maintain state and side effects may be unavoidable.
- Independent of evaluation order.
  - e.g. preferable for parallel computation, concurrent execution, recursion, etc.
  - This complements Imperative programming.
- A subtype of [declarative](#Declarative) programming.

For example:
```python
numbers = [1,2,3,4,5]
sum = functools.reduce(lambda x,y: x + y, numbers)
print sum
# 15
```
The anonymous function i.e. `lambda` which is defined/declared under `sum`, evaluates to `15`. Functional programming always returns a new expression, in this case `15` is returned as a new expression.
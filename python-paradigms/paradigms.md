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

### [Procedural](#Procedural)
- Procedures are subroutines, routines or function calls.
  - They contain a series of computation steps.
- [Subtype][10] of [imperative programming](#Imperative).
- Derived from structured programming.

### Object-Oriented (OO)

- Use of abstract data types to problem solve.
- The key abstractions become the objects.
  - An object is a tangible entity exhibiting some well-defined behavior.
  - Objects do things that we ask by sending them messages (calling functions).
- Real-world objects are each viewed as separate entities having their own state which is modified only by built in procedures, called methods.
- The use of encapsulation as modules which contain both local environments and methods.
  - Communication with an object is done by message passing.
- Objects are modeled in classes and inherit methods and attributes.
- Modelling a program into classes allows for modularity.
- Inheritance allows code to be reused and extended without the need to change existing source code.
- [Subtype][2] of [structured programming](#Structured).

## Other Language Paradigms

Python indirectly encompasses theses paradigms below, except Logical programming.

### [Declarative](#Declarative)

- The "what-to-solve" approach.
- [Expresses logic without describing control flow][10].

### [Logical](#Logical)

- [Rule-based][2].
- A set of rules and facts (or formal propositions) are specified.
- Implementation infers (or figures out) the results using logical statements.
- Takes a [declarative](#Declarative) approach to [problem-solving][9].

#### Languages:
- Prolog: stands for "[Programming in logic][3]".

<!-- ### [Structured](#Structured) -->

## [How to Choose a Paradigm](#How-to-Choose-a-Paradigm)

Words of Advice from Professor Tao at UCLA:
> Problem solving requires placing partial progress as a crucial stepping stone to fully solving the problem.
>
> If the "first solution attempt is able to solve some portion of the problem, one needs to then look to combine that argument with techniques that can solve complementary portions of the problem in order to reach the final solution".
>
> Failures are crucial advances needed to solve the full problem. Resolve at least some of the difficulties so that focus can be placed on the remaining issues that needed resolution.
>
> *[Importance of Partial Progress][4]*


Hence, usually there isn't a one size fits all solution. Think of the available programming paradigms as a set of tools; each with its own advantage.

Since problem solving often involves more than one approach. It is better to understand what each approach or paradigm is good for, then use a combination of one or more rather than constraining the solution to only one approach.

### Paradigms Overlap

Programming paradigms usually overlap.

![Venn Diagram of Imperative, Structured, Procedural Programing.](/python-paradigms/imperative-structured-procedural.jpg)

Doing a quick Google search for images of "[programming paradigms][8]", you will find the ubiquitous diagram that shows
two branches diverging into imperative and declarative programming. It seems to mean that the two branches are isolated
from each other. The following challenges this idea, indicating that these two branches do indeed overlap.

Take for example, structured programming is used to elaborate algorithms within and from methods for OO and as well as procedural programming. OO is distinguishable from procedural programming by the concept of classes. Structured
programming is also a necessary methodology for functional programming, and "modular decomposition and stepwise refinement
are as applicable to functional as to procedural programming" ([Michaelson][6]).

![Venn Diagram of Structured, Procedural, OO and Functional Programming.](/python-paradigms/structured-procedural-oo-functional.png)

> "This suggests that structured programming is a subset of procedural programming, which is a subset of both OO and functional programming " ([Michaelson][6]).

<!-- ![Peter Van Roy's Taxonomy of Programming Languages]() -->

### Last Thoughts

As mentioned in [How to Choose a Paradigm](#How-to-Choose-a-Paradigm), it is possible to use more than one paradigm if a language supports it. And by contrast, certain problems or conditions would make it preferable to exclusively code in
just one paradigm.

It is also important to consider the purpose of a particular programming language i.e. how it was developed into a
language, and perhaps even consider if it's a interpreted or compiled language.

Python is one great example of a multi-paradigm language, as well as Javascript, C++, Rust, and many others.
While Smalltalk is a purely OO and Haskell is purely functional.
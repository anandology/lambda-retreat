# Introduction to Scheme

## Introduction

Scheme is a very simple language. Let's start with a simple example.

This tutorial contains live code snippets, you can click the run button to execute it. You can also change the code and run again.

```{.scheme .feather}
(+ 1 2)
```

You may be wondering what is this weird syntax. This is prefix notation.

### The Prefix Notation

Mathematics is quite ambiguous. Look at the following mathematical expressions.

```
1 + 2
sin 30
5!
```

The first expression `1 + 2` is specified in the _infix_ notation, where the operator is in the center with arguments on the both sides.

The second expression `sin 30` uses _prefix_ notation, where the function `sin` is specified first, followed by the arguments.

And the last expression `5!` is specified in the _postfix_ notation.

While it may be acceptible to have such ambiguity in mathematics, but is hard for computers to deal with. To make things simple, Scheme only supports prefix notation.

The prefix notation have a couple of more advantages as well.

It is possible to call functions/operations with multiple arguments.

```{.scheme .feather}
(+ 1 2 3 4 5)
```

Or a single argument.

```{.scheme .feather}
(+ 1)
```

Or no arguments at all.

```{.scheme .feather}
(+)
```

What do you think would be the output of the following expression.

```{.scheme .feather}
(*)
```

### Comments

In scheme comments starts with `;` character.

```{.scheme .feather}
; Let's compute the sum of first first five numbers
(+ 1 2 3 4 5)
```

## The Elements of Programming

According to SICP, every language provides means for combining simple ideas to form more complex ones and every powerful language has three mechanisms for accomplishing this:

* primitive expressions
* means of combination
* means of abstration

### Primitive Expressions

When dealing with numbers, the primitive expressions are literal numbers and the primitive procedures (functions) that operate on them.

For example `100` is an expression representing a number.

```{.scheme .feather}
100
```

And `+` is a primitive expression representing the function to compute sum of numbers.

```{.scheme .feather}
+
```

### Means of combination

We can combine the primitive expressions to form more complex ones.

```{.scheme .feather}
(+ 3 4)
```

And use those expressions in other expressions.

```{.scheme .feather}
(* (+ 2 8) (+ 3 4))
```

Often, it is handy to pretty-print the long expressions.

```{.scheme .feather}
(*
  (+ 2 8)
  (+ 3 4))
```

### Means of Abstraction

Abstraction is a process by which compound elements can be named and manipulated as units.

In scheme, we name things using `define`.

```{.scheme .feather}
(define size 2)
```

Running the above example, makes the interpreter associate a value `2` with name _size_. We call _size_, a variable with it's value as `2`.

Once we define a variable, we can use it in other expressions.

```{.scheme .feather}
(define size 2)

(+ size 3)
```

## Functions

Functions, also called as Procedures in Scheme and SICP are specified using the `define` construct.

```{.scheme .feather}
(define (square x) (* x x))

(square 4)
```

**Problem 1**: Write a function `cube`

```{.scheme .feather}
; Write function cube here


; and compute cube of 3
(cube 3)
```

## Condtional Expressions



## Conditional Expressions
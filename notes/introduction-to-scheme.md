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

### Display

This environment displays the value of the last expression in the code when we run it. However, it is also possible to explicity display something using the `display` and `newline` functions.

```{.scheme .feather}
(display 1)
(newline)

(display 2)
(newline)

(display 3)
(newline)
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

One interesting thing about scheme is that it allows characters like -, ? etc. in the names, making it lot more readable.

```{.scheme .feather}
(define line-count 5)
(define even-number? 0)
```

Usually, the names ending with a `?` are used to define predicate functions, the functions that return true or false. We'll see them in the latter sections.

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

## Condtional Expressions and Predicates

Scheme has boolean values `#t` and `#f` for _true_ and _false_.

A boolean expression or a _predicate_, is an expression that result in boolean value. All the conditional operators can be used to construct a predicate.

```{.scheme .feather}
(> 10 5)
```

```{.scheme .feather}
(> 10 50)
```

Conditional expressions in scheme can be written using `if`.

```{.scheme .feather}
(define (min a b)
  (if (< a b) a b))

(min 3 5)
```

The general form for writing an if expression is:

```
(if <predicate> <consequent> <alternative>)
```

If the `<predicate>` is _true_, then the value of the if-expression is the value of `<consequent>`, otherwise it is the value of the `<alternative>`.

Please note that conditional expressions are _expressions_. They can be used to compose other expressions as well.

```{.scheme .feather}
(define (double-min a b)
  (* 2 (if (< a b) a b)))

(double-min 3 5)
```

### logical composition operations

In addition to primitive predicates like `<`, `>` etc., there are logical compostion operators, which enable us to create compound predicates. These are `and`, `or` and `not`.

To see how to use these, lets consider the predicate `even?` defined below.

```{.scheme .feather}
(define (even? n)
  (= (remainder n 2) 0))

(even? 4)
```

What if we want to check if both the given numbers are even?

```{.scheme .feather}
(define (both-even? a b)
  (and
    (even? a)
    (even? b)))

(both-even? 2 5)
```

What if we want to check if at least one of them is even?

```{.scheme .feather}
(define (any-even? a b)
  (or
    (even? a)
    (even? b)))

(any-even? 2 5)
```

And we can define `odd?` interms of `even?`.

```{.scheme .feather}
(define (odd? n)
  (not (even? n)))

(odd? 5)
```

### Cond

We've seen `if` expressions before, but `if` is actually a specical case of `cond`, a generic conditional expression.

```{.scheme .feather}
(define (min a b)
  (cond ((< a b) a)
        ((= a b) a)
        ((> a b) b)))

(min 3 5)
```

Another way to write this is using `else` for the last predicate, to handle the case of all earlier predicates being false.

```{.scheme .feather}
(define (min a b)
  (cond ((< a b) a)
        ((= a b) a)
        (else b)))

(min 3 5)
```

**Problem:** Write a function `min3` to compute minimum of three numbers. Can you implement it by reusing the `min` function defined earlier.

```{.scheme .feather}
(define (min a b)
  (if (> a b) a b))

(define (min3 a b c)
  ; Add your implementation here
  0
  )

(min3 3 5 7)
```
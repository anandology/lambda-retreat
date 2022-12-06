
# Problem Set 3

This problem set uses the concepts of dotted-tail notation and `apply` function. These concepts are explained below before the problems.

## Dotted-tail notation

When defining a procedure in Scheme, we can specify that a function can accept multiple arguments (variadic) using `dotted-tail` notation.

```scheme
(define (f . args) args)
```

When the procedure is called, all the arguments will be available as a list.

It is equivalant to the following in Python:

```python
def f(*args):
    return args
```

## The `apply` procedure

We can use the `apply` procedure to apply a procedure to a list of arguments.

```scheme
(define (add x y) (+ x y))

(apply add (list 3 4))
```

That would get translated as:

```scheme
(apply add (list 3 4))
(add 3 4)
7
```

This is equivalant to the following in Python.

```python
def add(x, y):
    return x+y

args = [3, 4]
result = add(*args)
print(result)
```

## Generalizing Iterative Processes

We've seen many iterative processes in the first chapter of SICP. In fact, we've converted many recursive processes to iterative processes.

Let's look at the implementation of the `fib` procedure.

```scheme
(define (fib n)
  (fib-iter 1 0 n))

(define (fib-iter a b count)
  (if (= count 0)
      b
      (fib-iter (+ a b) a (- count 1))))
```

And compare it with the implementaion of `f` in the Exercise 1.11.

```scheme
(define (f n)
  (f-iter 2 1 0 n))

(define (f-iter a b c n)
  (if (= n 0)
      c
      (f-iter (+ a (* 2 b) (* 3 c)) a b (- n 1))))
```

If you notice, even implementation of `expt-iter` follows the same pattern.

```scheme
(define (expt b n)
  (expt-iter b n 1))

(define (expt-iter b counter product)
  (if (= counter 0)
      product
      (expt-iter b
                 (- counter 1)
                 (* b product))))
```

The general pattern seems to be:

```scheme
(define (foo-iter n a b ...)
    (if (= n 0)
        <last-of-a-b-...>
        (foo-iter (- n 1) updated-values-of-a-b...> )))
```

Alyssa P. Hacker wasn't happy with this duplication and wanted to see if she can generalize it. She came up with the following idea.

The part that is changing between the implementaions is how the values are getting updated. These can be abstracted as:

```scheme
(define (fib-updater a b)
    (list (+ a b) a))

(define (f-updater a b c)
    (list (+ a (* 2 b) (* 3 c)) a b)
```

If there is a function `(repeat n args f)` that applies `f` to `args` n times.

```scheme
(repeat fib-updater 0 (list 1 0)) ; (1 0)
(repeat fib-updater 1 (list 1 0)) ; (1 1)
(repeat fib-updater 6 (list 1 0)) ; (13 8)

(repeat f-updater 0 (list 2 1 0)) ; (2 1 0)
(repeat f-updater 1 (list 2 1 0)) ; (4 2 1)
(repeat f-updater 4 (list 2 1 0)) ; (59 25 11)
```

**Problem 1:**
Implement the function `repeat` to make the examples shown above work as shown.

**Problem 2:**
Alyssa P. Hacker got really excited after seeing the elegance of the
`repeat` function and tried to use it to rewrite the `fib-iter`.

```scheme
(def (fib n)
    (fib-iter 1 0 n))

(define (fib-iter a b n)
  (last (repeat
        n
        (list a b)
        (lambda (a b) (list (+ a b) a))))
```

That seemed like a lot more code than what she started with. Determined to make it better, she came up with the following plan.

```scheme
(define (fib n)
    (iterative-process
        n
        (list 1 0)
        (lambda (a b) (list (+ a b) a))))
```

Can you help her by implementing the `iterative-process` procedure?

**Problem 3** Rewrite the procudure `f` from the Exercise 1.11 using `iterative-process`.

**Problem 4** Can you rewrite the following implementation of `expt` from Chapter 1.2 of SICP using `iterative-process`.

```scheme
(define (expt b n)
  (expt-iter b n 1))

(define (expt-iter b counter product)
  (if (= counter 0)
      product
      (expt-iter b
                 (- counter 1)
                 (* b product))))
```

**Problem 5:** Delighted with the generalization, Alyssa showed this to Ben Bitdiddle, who is not quite impressed with this implementation. He challenged her to generalize it even further so that he can define `fib` in the following way.

```scheme
(define fib
    (make-iterative-process
        (list 1 0)
        (lambda a b) (list (+ a b) a)))
```

Alyssa is thought this made the code less readable, but accepted the challenge relunctantly. Can you help her implement `make-iterative-process`?




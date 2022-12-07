**Problem 1:** Define procedure `last` that returns the last element of given non empty list.

```scheme
(last (list 1 2 3 4))
4
```

**Problem 2:** Define procedure `reverse` that takes a list as argument and returns a list with the same elements in reverse order.

```scheme
(reverse (list 1 2 3 4))
(4 3 2 1)

(reverse (list (list 1 2) (list 3 4)))
((3 4) (1 2))
```

**Problem 3:** The `map` procedure define in the Chapter 2.2 of SICP generates an recursive process, can you rewrite it as an iterative process?

Here is the implementation from the book.

```scheme
(define (map proc items)
  (if (null? items)
      nil
      (cons (proc (car items))
            (map proc (cdr items)))))
```

**Problem 4:** Define a procedure `flatten` that takes a tree as argument and returns a list whose values are all the leaves of the tree arranged in left-to-right order.

This is Excercise 2.28 from SICP.

```
(define x (list (list 1 2) (list 3 4)))

(flatten x)
(1 2 3 4)
```

**Problem 5:** Define a procedure `tree-map` that takes a proceduce and a tree as arguments and applies the function to every leaf of the tree and returns a new tree.

```scheme
(define (square-tree tree)
        (tree-map square tree))

(define x (list (list 1 2) (list 3 4)))

x
((1 2) (3 4))

(square-tree x)
((1 4) (9 16))
```

**Problem 6:** _Exercise 2.19 from SICP_

Rewrite the count-change procedure from SICP to pass the list of coins as an argument.

```scheme
(cc 100 (list 50 25 10 5 1))
292
```

Make approprite changes to the procedure to accommodate this. For your reference, the following is the original implementation of `count-change` example.

```scheme
(define (count-change amount)
  (cc amount 5))

(define (cc amount kinds-of-coins)
  (cond ((= amount 0) 1)
        ((or (< amount 0)
             (= kinds-of-coins 0))
         0)
        (else
         (+ (cc amount (- kinds-of-coins 1))
            (cc (- amount (first-denomination
                           kinds-of-coins))
                kinds-of-coins)))))

(define (first-denomination kinds-of-coins)
  (cond ((= kinds-of-coins 1) 1)
        ((= kinds-of-coins 2) 5)
        ((= kinds-of-coins 3) 10)
        ((= kinds-of-coins 4) 25)
        ((= kinds-of-coins 5) 50)))
```

**Problem 7:** _Exercise 2.33 from SICP_

Fill in the missing expressions to complete the following definitions of some basic list-manipulation operations as accumulations:

```scheme
(define (map p sequence)
  (accumulate (lambda (x y) ⟨??⟩)
              nil sequence))

(define (append seq1 seq2)
  (accumulate cons ⟨??⟩ ⟨??⟩))

(define (length sequence)
  (accumulate ⟨??⟩ 0 sequence))
```

For your reference, the `accumulate` procedure is defined as:

```scheme
(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op
                      initial
                      (cdr sequence)))))
```
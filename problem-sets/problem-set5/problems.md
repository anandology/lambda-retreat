
**Problem 1.** In the session 4, we've discussed about a procedure `simplify` to simplify symbolic expressions.

See https://notes.pipal.in/2022/lambda-retreat/session4.html or sample code.

It simplifies expressions like `(+ 0 x)` and `(* 1 x)` etc., but it does not convert expressions like `(+ (+ x x) (+ x x))` into `(* 4 x)`.

Extend the implementation of `simplify` to support that.

```
simplify(`(+ x x))
(* 2 x)

(simplify '(+ (+ x x) x))
(* 3 x)

simplify(`(* 2 (* 2 x)))
(* 4 x)
```

**Problem 2.** Write a procedure `infix-expr` to convert a symbolic expression into infix form.

It will convert the constants and variables to simple strings.

```
(infix-expr 'x)
"x"

(infix-expr '2)
"2"
```

The _sum_ expressions will be converted into infix.

```
(infix-expr '(+ x 2))
"x + 2"

(infix-expr '(+ (+ x y) 2))
"x + y + 2"
```

If the expression is a _product_, its arguments will be joined together.

```
(infix-expr '(* 2 x))
"2x"

(infix-expr '(* 2 (* x y)))
"2xy"

(infix-expr '(+ 2 (* x y)))
"2 + xy"
```

When any of the argument of a _product_ expression is a sum, that will be enclosed in parenthesis.

```
(infix-expr '(* 2 (+ x y)))
"2(x + y)"

(infix-expr '(* (+ x y) (+ x (* 2 y))))
"(x + y)(x + 2y)"
```

Hint:

You can use `format` proceduce to convert a value into a string.

```
(format "~a" 1)
"1"

(format "~a" 'x)
"x"
```

You can use the `string-append` procedure for joining multiple strings.

```
(string-append "x" " + " "y")
"x + y"
```
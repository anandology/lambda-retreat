Write an expression parser. The function should take an expr string as argument and returns that represented as a nested lists.

Please solve this problem in Python.

```
>>> parse("(+ 1 2)")
["+", 1, 2]
>>> parse("(+ 1 (* 2 3))")
["+", 1, ["*", 2, 3]]
```

Hint: You can tokenize the expression string using this simple hack (Credit: Peter Norvig).

```
>>> code = "(+ 1 (* 2 3))"
>>> code.replace("(", "( ").replace(")", " )").split()
['(', '+', '1', '(', '*', '2', '3', ')', ')']
```
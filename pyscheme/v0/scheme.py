"""Version 0 of scheme in Python.

The evaluator of this version just echos the expression.

Next Tasks:
- support numbers and primitive functions
"""
from parser import parse

global_env = {}

def evaluate(expr, env=global_env):
    # XXX: just echo the expression
    return expr

def run(code):
    env = {
        "+": lambda a, b: a+b
    }
    return evaluate(parse(code), env)

def schemestr(val):
    return val

def repl(prompt='scheme> '):
    while True:
        val = evaluate(parse(input(prompt)))
        if val is not None:
            print(schemestr(val))

def main():
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        code = open(filename).read()
        run(code)
    else:
        repl()

if __name__ == "__main__":
    main()
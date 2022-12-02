from calysto_scheme.kernel import CalystoScheme
import sys

d = {}
def set(name, value):
    d[name] = value

def do_eval(scheme, code):
    d = {}
    sys.setvar = d.__setitem__
    result = scheme.do_execute(f'(sys.setvar "-result-" {code})')
    assert result['status'] == 'ok', result
    return d['-result-']

def memoize(f):
    cache = {}
    def g(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return g

@memoize
def f(n):
    if n < 3:
        return n
    else:
        return f(n-1) + 2*f(n-2) + 3*f(n-3)

def test_ex111():
    d = {}
    sys.setvar = d.__setitem__

    scheme = CalystoScheme()
    result = scheme.do_execute('(import "sys")')
    result = scheme.do_execute(open("ex111.scm").read())

    for i in range(10):
        assert do_eval(scheme, f"(f {i})") == f(i)

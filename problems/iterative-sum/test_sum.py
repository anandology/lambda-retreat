from calysto_scheme.kernel import CalystoScheme
import sys

def do_eval(scheme, code):
    d = {}
    sys.setvar = d.__setitem__
    result = scheme.do_execute(f'(sys.setvar "-result-" {code})')
    assert result['status'] == 'ok', result
    return d['-result-']

code = """
(define (identity x) x)
(define (inc x)
    (+ x 1))
(define (cube x)
    (* x x x))

(define (sum-integers a b)
    (sum identity a inc b))

(define (sum-cubes a b)
  (sum cube a inc b))
"""

def test_sum():
    scheme = CalystoScheme()
    result = scheme.do_execute('(import "sys")')
    result = scheme.do_execute(open("sum.scm").read())
    scheme.do_execute(code)

    for a, b in [(2, 5), (2, 8), (3, 10)]:
        assert do_eval(scheme, f"(sum-integers {a} {b})") == sum(range(a, b+1))

        assert do_eval(scheme, f"(sum-cubes {a} {b})") == sum(x*x*x for x in range(a, b+1))

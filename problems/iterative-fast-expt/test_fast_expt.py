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


def test_fast_expt():
    d = {}
    sys.setvar = d.__setitem__

    scheme = CalystoScheme()
    result = scheme.do_execute('(import "sys")')
    result = scheme.do_execute(open("fast-expt.scm").read())

    for i in range(20):
        assert do_eval(scheme, f"(fast-expt 2 {i})") == 2 ** i

from calysto_scheme.kernel import CalystoScheme
import sys

def do_eval(scheme, code):
    d = {}
    sys.setvar = d.__setitem__
    result = scheme.do_execute(f'(sys.setvar "-result-" {code})')
    assert result['status'] == 'ok', result
    return d['-result-']

def assert_eval_value(scheme, code, expected_value):
    value = do_eval(scheme, code)
    assert abs(value-expected_value) < 0.001

def test_cuberoot():
    scheme = CalystoScheme()
    result = scheme.do_execute('(import "sys")')

    code = open("cuberoot.scm").read()
    result = scheme.do_execute(code)
    assert result['status'] == 'ok', result

    assert_eval_value(scheme, "(cube-root 8)", 2)
    assert_eval_value(scheme, "(cube-root 27)", 3)

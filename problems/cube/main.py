from calysto_scheme.kernel import CalystoScheme
from pathlib import Path

filename = list(Path(".").glob("*.scm"))[0]
scheme = CalystoScheme()
code = open(filename).read()
result = scheme.do_execute(code)

if result['status'] != 'ok':
    if 'traceback' in result:
        print("".join(result['traceback']))
    else:
        print("Execution failed:", result)
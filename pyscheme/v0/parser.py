"""Scheme parser.
"""

def tokenize(code):
    return code.replace("(", "( ").replace(")", " )").split()

def parse(code):
    def parse_node():
        nonlocal tokens
        current = tokens[0]
        if current == "(":
            tokens = tokens[1:]
            result = []
            while tokens[0] != ")":
                result.append(parse_node())
            tokens = tokens[1:]
            return result
        elif current.isdigit():
            tokens = tokens[1:]
            return int(current)
        else:
            tokens = tokens[1:]
            return current

    tokens = tokenize(code)
    return parse_node()

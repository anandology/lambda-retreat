from parse import parse

def test_parse_simple():
    assert parse("(+ 1 2)") == ["+", 1, 2]
    assert parse("(* 4 5)") == ["*", 4, 5]

def test_parse_nested():
    assert parse("(+ 1 (* 2 3))") == ["+", 1, ["*", 2, 3]]
    assert parse("(+ (* 2 3) (* 4 (+ 5 6)))") == ["+", ["*", 2, 3], ["*", 4, ["+", 5, 6]]]

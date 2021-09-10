from moviequotes.quote import get_quote

def test_type_get_quote():
    assert type(get_quote()[0]) == str and\
        type(get_quote()[1]) == str

def test_length_get_quote():
    assert len(get_quote()[0]) > 0 and len(get_quote()[1]) > 0

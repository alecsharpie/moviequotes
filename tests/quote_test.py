from moviequotes.quote import get_quote

def test_type_get_quote():
    assert type(get_quote()) == str

def test_length_get_quote():
    assert len(get_quote()) > 0

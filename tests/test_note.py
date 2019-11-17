from chordbook import Note


def test_note():
    c = Note()
    assert str(c) == 'C'
    assert str(c + 1) == 'C#'
    assert str(c + 2) == 'D'
    assert str(c - 1) == 'B'


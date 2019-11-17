
from chordbook import Chord



def test_parse_chord():
    c = Chord.parse('C')
    assert len(c) == 2
    assert c[0] == 'C'
    assert c[1] == 'E'
    assert c[2] == 'G'
    assert str(c) == 'C-E-G'

    assert str(Chord.parse('C')) == 'C-E-G'
    assert str(Chord.parse('C7')) == 'C-E-G-A#'
    assert str(Chord.parse('Cmaj7')) == 'C-E-G-B'
    assert str(Chord.parse('C6')) == 'C-E-G-A'
    assert str(Chord.parse('Cm')) == 'C-D#-G'
    assert str(Chord.parse('Cm7')) == 'C-D#-G-A#'
    assert str(Chord.parse('Cm/maj7')) == 'C-D#-G-B'
    assert str(Chord.parse('Cm6')) == 'C-D#-G-A'
    assert str(Chord.parse('Csus2')) == 'C-D-G'
    assert str(Chord.parse('Csus4')) == 'C-F-G'
    assert str(Chord.parse('C7sus2')) == 'C-D-G-A#'
    assert str(Chord.parse('C7sus4')) == 'C-F-G-A#'
    assert str(Chord.parse('Cdim')) == 'C-D#-F#'
    assert str(Chord.parse('Cdim7')) == 'C-D#-F#-A'
    assert str(Chord.parse('Caug')) == 'C-E-G#'
    assert str(Chord.parse('C5')) == 'C-G'
#    assert str(Chord.parse('C/5+')) == 'C-E-G#'
#    assert str(Chord.parse('C/5-')) == 'C-E-F#'
#    assert str(Chord.parse('Cadd9')) == 'C-E-G-D'
#    assert str(Chord.parse('Cadd9-')) == 'C-E-G-C#'
#    assert str(Chord.parse('Cadd9+')) == 'C-E-G-D#'
#    assert str(Chord.parse('Cadd11')) == 'C-E-G-F'
#    assert str(Chord.parse('Cadd11-')) == 'C-E-G-E'
#    assert str(Chord.parse('Cadd11+')) == 'C-E-G-F#'
#    assert str(Chord.parse('Cadd13')) == 'C-E-G-A'
#    assert str(Chord.parse('Cadd13-')) == 'C-E-G-G#'
#    assert str(Chord.parse('Cadd13+')) == 'C-E-G-A#'
#    assert str(Chord.parse('Cadd13+/5+')) == 'C-E-G#-A#'
#
    #assert str(Chord.parse('C13/5+/9+/11-')) == 'C-E-G-A#'

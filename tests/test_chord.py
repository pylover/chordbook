
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
    assert str(Chord.parse('Caug7')) == 'C-E-G#-C'
    assert str(Chord.parse('C5')) == 'C-G'
    assert str(Chord.parse('C9')) == 'C-E-G-A#-D'
    assert str(Chord.parse('C9-')) == 'C-E-G-A#-C#'
    assert str(Chord.parse('C9+')) == 'C-E-G-A#-D#'
    assert str(Chord.parse('C7add9')) == 'C-E-G-A#-D'
    assert str(Chord.parse('C7add9-')) == 'C-E-G-A#-C#'
    assert str(Chord.parse('C7add9+')) == 'C-E-G-A#-D#'
    assert str(Chord.parse('Cadd9')) == 'C-E-G-D'
    assert str(Chord.parse('Cadd9-')) == 'C-E-G-C#'
    assert str(Chord.parse('Cadd9+')) == 'C-E-G-D#'
    assert str(Chord.parse('Cmaj7add9+')) == 'C-E-G-B-D#'
    assert str(Chord.parse('Cmaj7add9-')) == 'C-E-G-B-C#'
    assert str(Chord.parse('Cadd11')) == 'C-E-G-F'
    assert str(Chord.parse('Cadd11-')) == 'C-E-G-E'
    assert str(Chord.parse('Cadd11+')) == 'C-E-G-F#'
    assert str(Chord.parse('Cadd13')) == 'C-E-G-A'
    assert str(Chord.parse('Cadd13-')) == 'C-E-G-G#'
    assert str(Chord.parse('Cadd13+')) == 'C-E-G-A#'

    assert str(Chord.parse('C/5-')) == 'C-E-F#'
    assert str(Chord.parse('C/5+')) == 'C-E-G#'

    assert str(Chord.parse('Cadd13+/5+')) == 'C-E-G#-A#'
    #assert str(Chord.parse('C13/5+/9+/11-')) == 'C-E-G-A#'

    assert str(Chord.parse('E7')) == 'E-G#-B-D'
    assert str(Chord.parse('C')) == 'C-E-G'
    assert str(Chord.parse('Cm')) == 'C-D#-G'
    assert str(Chord.parse('G')) == 'G-B-D'
    assert str(Chord.parse('G7')) == 'G-B-D-F'

    assert str(Chord.parse('E')) == 'E-G#-B'
    assert str(Chord.parse('G')) == 'G-B-D'
    assert str(Chord.parse('Am')) == 'A-C-E'
    assert str(Chord.parse('A')) == 'A-C#-E'
    assert str(Chord.parse('Adim')) == 'A-C-D#'
    assert str(Chord.parse('Aaug')) == 'A-C#-F'
    assert str(Chord.parse('A7')) == 'A-C#-E-G'
    assert str(Chord.parse('Am7')) == 'A-C-E-G'

    assert str(Chord.parse('G7')) == 'G-B-D-F'


'''
          0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2
          0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
          C   D   E F   G   A   B C   D   E F   G   A   B C
          . . . . . . . . . . . . . . . . . . . . . . . . .

C         | . . . | . . | . . . . . . . . . . . . . . . . .
Cm        | . . | . . . | . . . . . . . . . . . . . . . . .
Csus2     | . | . . . . | . . . . . . . . . . . . . . . . .
Csus4     | . . . . | . | . . . . . . . . . . . . . . . . .
Cdim      | . . | . . | . . . . . . . . . . . . . . . . . .
Caug      | . . . | . . . | . . . . . . . . . . . . . . . .
C5        | . . . . . . | . . . . . . . . . . . . . . . . .
C/5+      | . . . | . . . | . . . . . . . . . . . . . . . .
C/5-      | . . . | . | . . . . . . . . . . . . . . . . . .
----

Quad
          0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2
          0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
          C   D   E F   G   A   B C   D   E F   G   A   B C
          . . . . . . . . . . . . . . . . . . . . . . . . .
C7        | . . . | . . | . . | . . . . . . . . . . . . . .
Cmaj7     | . . . | . . | . . . | . . . . . . . . . . . . .
C6        | . . . | . . | . | . . . . . . . . . . . . . . .
Cm7       | . . | . . . | . . | . . . . . . . . . . . . . .
Cm/maj7   | . . | . . . | . . . | . . . . . . . . . . . . .
Cm6       | . . | . . . | . | . . . . . . . . . . . . . . .
C7sus2    | . | . . . . | . . | . . . . . . . . . . . . . .
C7sus4    | . . . . | . | . . | . . . . . . . . . . . . . .
Cdim7     | . . | . . | . . | . . . . . . . . . . . . . . .
Caug      | . . . | . . . | . . . | . . . . . . . . . . . .
Cm/maj7   | . . | . . . | . . . | . . . . . . . . . . . . .


Panthetonic
          0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2
          0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
          C   D   E F   G   A   B C   D   E F   G   A   B C
          . . . . . . . . . . . . . . . . . . . . . . . . .
C9        | . . . | . . | . . | . . . | . . . . . . . . . .
Cm9       | . . | . . . | . . | . . . | . . . . . . . . . .
C9-       | . . . | . . | . . | . . | . . . . . . . . . . .
C9+       | . . . | . . | . . | . . . . | . . . . . . . . .
Cadd9     | . . . | . . | . . . . . . | . . . . . . . . . .

Sixtual
          0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2
          0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
          C   D   E F   G   A   B C   D   E F   G   A   B C
          . . . . . . . . . . . . . . . . . . . . . . . . .
Cm11      | . . | . . . | . . | . . . | . . | . . . . . . .
C11       | . . . | . . | . . | . . . | . . | . . . . . . .
Cadd11    | . . . | . . | . . . . . . . . . | . . . . . . .

Seven
Cm13      | . . | . . . | . . | . . . | . . | . . . | . . .
C13       | . . . | . . | . . | . . . | . . | . . . | . . .
Cadd13    | . . . | . . | . . . . . . . . . . . . . | . . .

'''


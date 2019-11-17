
CHROMATIC = [
    'C',
    'C#',
    'D',
    'D#',
    'E',
    'F',
    'F#',
    'G',
    'G#',
    'A',
    'A#',
    'B'
]


class Note:
    c_offset = 0

    def __init__(self, v='C'):
        if isinstance(v, str):
            v = CHROMATIC.index(v.upper())
        self += v

    @property
    def note(self):
        return self.c_offset % 12

    @property
    def octave(self):
        return self.c_offset // 12

    def __iadd__(self, v):
        self.c_offset += v

    def __add__(self, v):
        return self.__class__(self.c_offset + v)

    def __isub(self, v):
        self.c_offset -= v

    def __sub__(self, v):
        return self.__class__(self.c_offset - v)

    def __str__(self):
        return CHROMATIC[self.note]

    def __eq__(self, o):
        if isinstance(o, str):
            return str(self) == o.upper()

        return self.c_offset == o


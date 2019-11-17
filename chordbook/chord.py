import re

from .note import Note


CHORD_PATTERN = re.compile(
    r'^(?P<note>[CDEFGAB]#?)'
    r'(?P<name>M|(maj)?7|6|m(6|7|/maj7)?|7?sus[24]|dim7?|aug|5)?'
#    r'(?P<add>add(9|11|13)[+-]?)?'
#    r'(?P<extra>((/5|/9|/11)[+-])*)?'
    r'$'
)


class Chord:
    def __init__(self, base, step3, step5, step7, step9, step11, step13):
        if not isinstance(base, Note):
            base = Note(base)
        self.base = base
        self.steps = [step3, step5, step7, step9, step11, step13]

    def __iter__(self):
        yield self.base
        for s in self.steps:
            if s is None:
                continue

            yield self.base + s

    def __len__(self):
        return len([s for s in self.steps if s is not None])

    def __getitem__(self, index):
        return list(self)[index]

    def __str__(self):
        return '-'.join(str(n) for n in self if n)

    @classmethod
    def parse(cls, s):
        match = CHORD_PATTERN.match(s)
        if match is None:
            raise ValueError(f'Cannot parse: {s}')

        groups = match.groupdict()
        note = groups['note']
        step3 = None
        step5 = None
        step7 = None
        step9 = None
        step11 = None
        step13 = None

        name = groups['name']
        if name == '5':
            step5 = 7

        else:
            step3 = {
                'sus2': 2,
                '7sus2': 2,
                'm': 3,
                'm6': 3,
                'm7': 3,
                'm/maj7': 3,
                'dim': 3,
                'dim7': 3,
                'M': 4,
                'sus4': 5,
                '7sus4': 5,
            }.get(name, 4)

            step5 = {
                'aug': 8,
                'dim': 6,
                'dim7': 6,
            }.get(name, 7)

            step7 = {
                '6': 9,
                'm6': 9,
                'dim7': 9,
                '7': 10,
                'm7': 10,
                '7sus2': 10,
                '7sus4': 10,
                'maj7': 11,
                'm/maj7': 11,
            }.get(name)

#        add = groups['add']
#        if add:
#            if add.startswith('add9'):
#                step4 = {
#                    'add9-':  13,
#                    'add9':   14,
#                    'add9+':  15,
#                }.get(add)
#
#            elif add.startswith('add11'):
#                step5 = {
#                    'add11-': 16,
#                    'add11':  17,
#                    'add11+': 18,
#                }.get(add)
#
#            elif add.startswith('add13'):
#                step6 = {
#                    'add13-': 20,
#                    'add13':  21,
#                    'add13+': 22,
#                }.get(add)
#
#            # TODO: only allow /5[+-]
#
#        extra = groups['extra']
#        if extra:
#            for e in extra.split('/'):
#                if e.startswith('5'):
#                    step2 = {
#                        '5-': 6,
#                        '5':  7,
#                        '5+': 8,
#                    }.get(e)
#
#                elif e.startswith('9'):
#                    step4 = {
#                        '9-': 13,
#                        '9':  14,
#                        '9+': 15,
#                    }.get(e)
#
#                elif e.startswith('11'):
#                    step5 = {
#                        '11-': 16,
#                        '11':  17,
#                        '11+': 18,
#                    }.get(e)

        return cls(note, step3, step5, step7, step9, step11, step13)
'''
          0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2
          0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
          C   D   E F   G   A   B C   D   E F   G   A   B C
          . . . . . . . . . . . . . . . . . . . . . . . . .

C         | . . . | . . | . . . . . . . . . . . . . . . . .
C7        | . . . | . . | . . | . . . . . . . . . . . . . .
Cmaj7     | . . . | . . | . . . | . . . . . . . . . . . . .
C6        | . . . | . . | . | . . . . . . . . . . . . . . .
Cm        | . . | . . . | . . . . . . . . . . . . . . . . .
Cm7       | . . | . . . | . . | . . . . . . . . . . . . . .
Cm/maj7   | . . | . . . | . . . | . . . . . . . . . . . . .
Cm6       | . . | . . . | . | . . . . . . . . . . . . . . .
Csus2     | . | . . . . | . . . . . . . . . . . . . . . . .
Csus4     | . . . . | . | . . . . . . . . . . . . . . . . .
C7sus2    | . | . . . . | . . | . . . . . . . . . . . . . .
C7sus4    | . . . . | . | . . | . . . . . . . . . . . . . .
Cdim      | . . | . . | . . . . . . . . . . . . . . . . . .
Cdim7     | . . | . . | . . | . . . . . . . . . . . . . . .
Caug      | . . . | . . . | . . . . . . . . . . . . . . . .
C5        | . . . . . . | . . . . . . . . . . . . . . . . .

----
Cadd9     | . . . | . . | . . . . . . | . . . . . . . . . .
Cadd11    | . . . | . . | . . . . . . . . . | . . . . . . .
Cadd13    | . . . | . . | . . . . . . . . . . . . . | . . .
C/5+      | . . . | . . . | . . . . . . . . . . . . . . . .
C/5-      | . . . | . | . . . . . . . . . . . . . . . . . .
Cm6       | . . | . . . | . | . . . . . . . . . . . . . . .
Cm/maj7   | . . | . . . | . . . | . . . . . . . . . . . . .

Panthetonic
Cm9       | . . | . . . | . . | . . . | . . . . . . . . . .
C9-       | . . . | . . | . . | . . | . . . . . . . . . . .
C9        | . . . | . . | . . | . . . | . . . . . . . . . .
C9+       | . . . | . . | . . | . . . . | . . . . . . . . .

Sixtual
Cm11      | . . | . . . | . . | . . . | . . | . . . . . . .
C11       | . . . | . . | . . | . . . | . . | . . . . . . .

Seven
Cm13      | . . | . . . | . . | . . . | . . | . . . | . . .
C13       | . . . | . . | . . | . . . | . . | . . . | . . .

'''


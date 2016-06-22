import unittest
import allbase.base as base
from collections import namedtuple


class TestOutputFormat(unittest.TestCase):

    def test_from_str(self):

        fix = namedtuple('fix', 'input bases err')
        tests = [
            fix(input="",
                bases=[],
                err=None),
            fix(input="a",
                bases=None,
                err="unknown base: 'a'"),
            fix(input="d",
                bases=[base.dec],
                err=None),
            fix(input="h",
                bases=[base.hex],
                err=None),
            fix(input="o",
                bases=[base.oct],
                err=None),
            fix(input="b",
                bases=[base.bin],
                err=None),
            fix(input="dd",
                bases=[base.dec,
                             base.dec],
                err=None),
            fix(input="do",
                bases=[base.dec,
                             base.oct],
                err=None),
            fix(input="od",
                bases=[base.oct,
                             base.dec],
                err=None),
            fix(input="hdob",
                bases=[base.hex,
                             base.dec,
                             base.oct,
                             base.bin],
                err=None),
            fix(input="hodbhhdoddb",
                bases=[base.hex,
                             base.oct,
                             base.dec,
                             base.bin,
                             base.hex,
                             base.hex,
                             base.dec,
                             base.oct,
                             base.dec,
                             base.dec,
                             base.bin],
                err=None),
            fix(input="hodbhhadoddb",
                bases=None,
                err="unknown base: 'a'"),
        ]

        for i, t in enumerate(tests):
            bases, err = base.from_str_list(t.input)

            template = "subtest {0}):\n\tinput={1!r}\n\t"\
                "bases\n\t\texpected={2}\n\t\tobtained={3}\n\t"\
                "error\n\t\texpected={4!r}\n\t\tobtained={5!r}"
            comment = template.format(i, t.input,
                                      t.bases, bases,
                                      t.err, err)
            self.assertEqual(bases, t.bases, comment)
            self.assertEqual(err, t.err, comment)

    def test_Base_repr(self):
        for b in base.all:
            self.assertEqual(repr(b), b.repr)

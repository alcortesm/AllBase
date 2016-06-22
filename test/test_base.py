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
                bases=[base.Bases.dec.value],
                err=None),
            fix(input="h",
                bases=[base.Bases.hex.value],
                err=None),
            fix(input="o",
                bases=[base.Bases.oct.value],
                err=None),
            fix(input="b",
                bases=[base.Bases.bin.value],
                err=None),
            fix(input="dd",
                bases=[base.Bases.dec.value,
                             base.Bases.dec.value],
                err=None),
            fix(input="do",
                bases=[base.Bases.dec.value,
                             base.Bases.oct.value],
                err=None),
            fix(input="od",
                bases=[base.Bases.oct.value,
                             base.Bases.dec.value],
                err=None),
            fix(input="hdob",
                bases=[base.Bases.hex.value,
                             base.Bases.dec.value,
                             base.Bases.oct.value,
                             base.Bases.bin.value],
                err=None),
            fix(input="hodbhhdoddb",
                bases=[base.Bases.hex.value,
                             base.Bases.oct.value,
                             base.Bases.dec.value,
                             base.Bases.bin.value,
                             base.Bases.hex.value,
                             base.Bases.hex.value,
                             base.Bases.dec.value,
                             base.Bases.oct.value,
                             base.Bases.dec.value,
                             base.Bases.dec.value,
                             base.Bases.bin.value],
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
        for b in list(base.Bases):
            self.assertEqual(repr(b.value), b.value.repr)

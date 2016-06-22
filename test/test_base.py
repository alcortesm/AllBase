import unittest
import allbase.base as base
from collections import namedtuple


class TestOutputFormat(unittest.TestCase):

    def test_from_str(self):

        fix = namedtuple('fix', 'input exp_formats exp_err')
        tests = [
            fix(input="",
                exp_formats=[],
                exp_err=None),
            fix(input="a",
                exp_formats=None,
                exp_err="unknown format: 'a'"),
            fix(input="d",
                exp_formats=[base.Bases.dec],
                exp_err=None),
            fix(input="h",
                exp_formats=[base.Bases.hex],
                exp_err=None),
            fix(input="o",
                exp_formats=[base.Bases.oct],
                exp_err=None),
            fix(input="b",
                exp_formats=[base.Bases.bin],
                exp_err=None),
            fix(input="dd",
                exp_formats=[base.Bases.dec,
                             base.Bases.dec],
                exp_err=None),
            fix(input="do",
                exp_formats=[base.Bases.dec,
                             base.Bases.oct],
                exp_err=None),
            fix(input="od",
                exp_formats=[base.Bases.oct,
                             base.Bases.dec],
                exp_err=None),
            fix(input="hdob",
                exp_formats=[base.Bases.hex,
                             base.Bases.dec,
                             base.Bases.oct,
                             base.Bases.bin],
                exp_err=None),
            fix(input="hodbhhdoddb",
                exp_formats=[base.Bases.hex,
                             base.Bases.oct,
                             base.Bases.dec,
                             base.Bases.bin,
                             base.Bases.hex,
                             base.Bases.hex,
                             base.Bases.dec,
                             base.Bases.oct,
                             base.Bases.dec,
                             base.Bases.dec,
                             base.Bases.bin],
                exp_err=None),
            fix(input="hodbhhadoddb",
                exp_formats=None,
                exp_err="unknown format: 'a'"),
        ]

        for i, t in enumerate(tests):
            formats, err = base.from_str(t.input)

            template = "subtest {0}):\n\tinput={1!r}\n\t"\
                "expected formats={2}\n\tobtained formats={3}\n\t"\
                "expected error={4!r}\n\tobtained error={5!r}"
            comment = template.format(i, t.input,
                                      t.exp_formats, formats,
                                      t.exp_err, err)
            self.assertEqual(formats, t.exp_formats, comment)
            self.assertEqual(err, t.exp_err, comment)

    def test_Bases_str(self):
        for b in list(base.Bases):
            self.assertEqual(str(b), b.value.str)

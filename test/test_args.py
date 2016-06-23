import unittest
import allbase.args as args
from collections import namedtuple
import allbase.base as base


class TestArgs(unittest.TestCase):

    def test_parse(self):

        fix = namedtuple('fix', 'input num bases valid reason')
        tests = [
            fix(
                input=[],
                num=None,
                bases=None,
                valid=False,
                reason='no input arguments'
            ),
            fix(
                input=['12'],
                num=[12],
                bases=[base.dec, base.hex, base.oct, base.bin],
                valid=True,
                reason=None
            ),
            fix(
                input=['12', '-b', 'd'],
                num=[12],
                bases=[base.dec],
                valid=True,
                reason=None
            ),
            fix(
                input=['12', '-b', 'doob'],
                num=[12],
                bases=[base.dec, base.oct, base.oct, base.bin],
                valid=True,
                reason=None
            ),
            fix(
                input=['12', '-b', 'doaob'],
                num=None,
                bases=None,
                valid=False,
                reason="unknown base: 'a'",
            ),
            fix(
                input=['asdf'],
                num=None,
                bases=None,
                valid=False,
                reason="need a positive integer, got 'asdf'"
            ),
            fix(
                input=[' '],
                num=None,
                bases=None,
                valid=False,
                reason="need a positive integer, got ' '"
            ),
            fix(
                input=['-12'],
                num=None,
                bases=None,
                valid=False,
                reason="need a positive integer, got '-12'"
            ),
            fix(
                input=['12.1'],
                num=None,
                bases=None,
                valid=False,
                reason="need a positive integer, got '12.1'"
            ),
            fix(
                input=['12.0'],
                num=None,
                bases=None,
                valid=False,
                reason="need a positive integer, got '12.0'"
            ),
            fix(
                input=['0', '1'],
                num=[0, 1],
                bases=[base.dec, base.hex, base.oct, base.bin],
                valid=True,
                reason=None
            ),
            fix(
                input=['0', '255'],
                num=[0, 255],
                bases=[base.dec, base.hex, base.oct, base.bin],
                valid=True,
                reason=None
            ),
            fix(
                input=['0', '255', '65536'],
                num=[0, 255, 65536],
                bases=[base.dec, base.hex, base.oct, base.bin],
                valid=True,
                reason=None
            ),
            fix(
                input=['15', '255', '65535', '-b', 'hd'],
                num=[0, 255, 65536],
                bases=[base.hex, base.dec],
                valid=True,
                reason=None
            ),
            fix(
                input=['15', '255', '65535', '-b', 'bo', '1'],
                num=[0, 255, 65536, 1],
                bases=[base.bin, base.oct],
                valid=True,
                reason=None
            ),
            fix(
                input=['-b', 'bo', '15', '255'],
                num=[0, 255, 65536, 1],
                bases=[base.bin, base.oct],
                valid=True,
                reason=None
            ),
        ]

        for i, t in enumerate(tests):
            num, bases, valid, reason = args.parse(t.input)

            template = "subtest {0}):\n\tinput = {1!r}\n\t"\
                "num\n\t\texpected={2}\n\t\tobtained={3}\n\t"\
                "bases\n\t\texpected={4}\n\t\tobtained={5}\n\t"\
                "valid\n\t\texpected={6}\n\t\tobtained={7}\n\t"\
                "reason\n\t\texpected={8!r}\n\t\tobtained={9!r}\n\t"
            comment = template.format(i, t.input,
                                      t.num, num,
                                      t.bases, bases,
                                      t.valid, valid,
                                      t.reason, reason)

            self.assertEqual(num, t.num, comment)
            self.assertEqual(bases, t.bases, comment)
            self.assertEqual(valid, t.valid, comment)
            self.assertEqual(reason, t.reason, comment)

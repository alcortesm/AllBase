import unittest
from allbase import tobase
from allbase import base
from collections import namedtuple


class TestToBase(unittest.TestCase):

    def test_to_base(self):

        fix = namedtuple('fix', 'nums bases expected')
        tests = [
            fix([0], [base.dec], ['0']),
            fix([1], [base.dec], ['1']),
            fix([2], [base.dec], ['2']),
            fix([7], [base.dec], ['7']),
            fix([8], [base.dec], ['8']),
            fix([15], [base.dec], ['15']),
            fix([16], [base.dec], ['16']),
            fix([255], [base.dec], ['255']),
            fix([256], [base.dec], ['256']),
            fix([(2**16)-1], [base.dec], ['65535']),
            fix([2**16], [base.dec], ['65536']),
            fix([(2**32)-1], [base.dec], ['4294967295']),
            fix([2**32], [base.dec], ['4294967296']),
            fix([(2**64)-1], [base.dec], ['18446744073709551615']),
            fix([2**64], [base.dec], ['18446744073709551616']),
            #
            fix([0], [base.bin], ['0b0']),
            fix([1], [base.bin], ['0b1']),
            fix([2], [base.bin], ['0b10']),
            fix([7], [base.bin], ['0b111']),
            fix([8], [base.bin], ['0b1000']),
            fix([15], [base.bin], ['0b1111']),
            fix([16], [base.bin], ['0b10000']),
            fix([255], [base.bin], ['0b11111111']),
            fix([256], [base.bin], ['0b100000000']),
            fix([(2**16)-1], [base.bin], ['0b1111111111111111']),
            fix([2**16], [base.bin], ['0b10000000000000000']),
            #
            fix([0], [base.oct], ['0o0']),
            fix([1], [base.oct], ['0o1']),
            fix([2], [base.oct], ['0o2']),
            fix([7], [base.oct], ['0o7']),
            fix([8], [base.oct], ['0o10']),
            fix([15], [base.oct], ['0o17']),
            fix([16], [base.oct], ['0o20']),
            fix([255], [base.oct], ['0o377']),
            fix([256], [base.oct], ['0o400']),
            fix([(2**16)-1], [base.oct], ['0o177777']),
            fix([2**16], [base.oct], ['0o200000']),
            #
            fix([0], [base.hex], ['0x0']),
            fix([1], [base.hex], ['0x1']),
            fix([2], [base.hex], ['0x2']),
            fix([7], [base.hex], ['0x7']),
            fix([8], [base.hex], ['0x8']),
            fix([15], [base.hex], ['0xf']),
            fix([16], [base.hex], ['0x10']),
            fix([255], [base.hex], ['0xff']),
            fix([256], [base.hex], ['0x100']),
            fix([(2**16)-1], [base.hex], ['0xffff']),
            fix([2**16], [base.hex], ['0x10000']),
            fix([(2**32)-1], [base.hex], ['0xffffffff']),
            fix([2**32], [base.hex], ['0x100000000']),
            fix([(2**64)-1], [base.hex], ['0xffffffffffffffff']),
            fix([2**64], [base.hex], ['0x10000000000000000']),
            #
            fix(
                [42],
                [
                    base.dec,
                    base.hex,
                    base.dec,
                    base.bin
                ],
                ['42 0x2a 42 0b101010']
            ),
            fix(
                [15, 255, 65535], [base.dec],
                ['15', '255', '65535']
            ),
            fix(
                [15, 255, 65535], [base.hex],
                ['0xf', '0xff', '0xffff']
            ),
            fix(
                [15, 255, 65535], [base.dec, base.hex],
                ['15 0xf', '255 0xff', '65535 0xffff']
            ),
            fix(
                [15, 255, 65535], [base.hex, base.dec],
                ['0xf 15', '0xff 255', '0xffff 65535']
            )
        ]

        for i, t in enumerate(tests):
            obtained = tobase.do(t.nums, t.bases)

            template = "subtest {0}):\n" \
                "\tn={1}\n" \
                "\tbases={2}\n" \
                "\tstr:\n" \
                "\t\texpected={3!r}\n" \
                "\t\tobtained={4!r}\n"
            comment = template.format(i, t.nums, t.bases, t.expected, obtained)

            self.assertEqual(obtained, t.expected, comment)

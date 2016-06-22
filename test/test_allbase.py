import unittest
from allbase import tobases
from allbase import base
from collections import namedtuple


class TestAllBase(unittest.TestCase):

    def test_to_bases(self):

        fix = namedtuple('fix', 'n bases expected')
        tests = [
            fix(0, [base.Bases.dec.value], '0'),
            fix(1, [base.Bases.dec.value], '1'),
            fix(2, [base.Bases.dec.value], '2'),
            fix(7, [base.Bases.dec.value], '7'),
            fix(8, [base.Bases.dec.value], '8'),
            fix(15, [base.Bases.dec.value], '15'),
            fix(16, [base.Bases.dec.value], '16'),
            fix(255, [base.Bases.dec.value], '255'),
            fix(256, [base.Bases.dec.value], '256'),
            fix((2**16)-1, [base.Bases.dec.value], '65535'),
            fix(2**16, [base.Bases.dec.value], '65536'),
            fix((2**32)-1, [base.Bases.dec.value], '4294967295'),
            fix(2**32, [base.Bases.dec.value], '4294967296'),
            fix((2**64)-1, [base.Bases.dec.value], '18446744073709551615'),
            fix(2**64, [base.Bases.dec.value], '18446744073709551616'),
            #
            fix(0, [base.Bases.bin.value], '0b0'),
            fix(1, [base.Bases.bin.value], '0b1'),
            fix(2, [base.Bases.bin.value], '0b10'),
            fix(7, [base.Bases.bin.value], '0b111'),
            fix(8, [base.Bases.bin.value], '0b1000'),
            fix(15, [base.Bases.bin.value], '0b1111'),
            fix(16, [base.Bases.bin.value], '0b10000'),
            fix(255, [base.Bases.bin.value], '0b11111111'),
            fix(256, [base.Bases.bin.value], '0b100000000'),
            fix((2**16)-1, [base.Bases.bin.value], '0b1111111111111111'),
            fix(2**16, [base.Bases.bin.value], '0b10000000000000000'),
            #
            fix(0, [base.Bases.oct.value], '0o0'),
            fix(1, [base.Bases.oct.value], '0o1'),
            fix(2, [base.Bases.oct.value], '0o2'),
            fix(7, [base.Bases.oct.value], '0o7'),
            fix(8, [base.Bases.oct.value], '0o10'),
            fix(15, [base.Bases.oct.value], '0o17'),
            fix(16, [base.Bases.oct.value], '0o20'),
            fix(255, [base.Bases.oct.value], '0o377'),
            fix(256, [base.Bases.oct.value], '0o400'),
            fix((2**16)-1, [base.Bases.oct.value], '0o177777'),
            fix(2**16, [base.Bases.oct.value], '0o200000'),
            #
            fix(0, [base.Bases.hex.value], '0x0'),
            fix(1, [base.Bases.hex.value], '0x1'),
            fix(2, [base.Bases.hex.value], '0x2'),
            fix(7, [base.Bases.hex.value], '0x7'),
            fix(8, [base.Bases.hex.value], '0x8'),
            fix(15, [base.Bases.hex.value], '0xf'),
            fix(16, [base.Bases.hex.value], '0x10'),
            fix(255, [base.Bases.hex.value], '0xff'),
            fix(256, [base.Bases.hex.value], '0x100'),
            fix((2**16)-1, [base.Bases.hex.value], '0xffff'),
            fix(2**16, [base.Bases.hex.value], '0x10000'),
            fix((2**32)-1, [base.Bases.hex.value], '0xffffffff'),
            fix(2**32, [base.Bases.hex.value], '0x100000000'),
            fix((2**64)-1, [base.Bases.hex.value], '0xffffffffffffffff'),
            fix(2**64, [base.Bases.hex.value], '0x10000000000000000'),
            #
            fix(
                42,
                [
                    base.Bases.dec.value,
                    base.Bases.hex.value,
                    base.Bases.dec.value,
                    base.Bases.bin.value
                ],
                '42 0x2a 42 0b101010'
            )
        ]

        for i, t in enumerate(tests):
            obtained = tobases.to_bases(t.n, t.bases)

            template = "subtest {0}):\n" \
                "\tn={1}\n" \
                "\tbases={2}\n" \
                "\tstr:\n" \
                "\t\texpected={3!r}\n" \
                "\t\tobtained={4!r}\n"
            comment = template.format(i, t.n, t.bases, t.expected, obtained)

            self.assertEqual(obtained, t.expected, comment)

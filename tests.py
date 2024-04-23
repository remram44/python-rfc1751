import unittest

import rfc1751


class TestRfc1751(unittest.TestCase):
    def test_extract(self):
        # 01011001 11001100
        #      ^-- ----^
        #      0011 1001
        self.assertEqual(
            rfc1751._extract_bits(b'\x59\xCC', 5, 8),
            0x39,
        )

    def test_encode(self):
        self.assertEqual(
            rfc1751.bytes_to_string(
                b'\xCC\xAC\x2A\xED\x59\x10\x56\xBE',
            ),
            'RASH BUSH MILK LOOK BAD BRIM',
        )

    def test_decode(self):
        self.assertEqual(
            rfc1751.string_to_bytes(
                'RASH BUSH MILK LOOK BAD BRIM',
            ),
            b'\xCC\xAC\x2A\xED\x59\x10\x56\xBE',
        )
        self.assertEqual(
            rfc1751.string_to_bytes(
                'RA5h BU5H mi1k 100k Bad Brim',
            ),
            b'\xCC\xAC\x2A\xED\x59\x10\x56\xBE',
        )

    def test_errors(self):
        with self.assertRaises(rfc1751.WrongNumberOfWordsError) as cm:
            rfc1751.string_to_bytes('rash bush')
        self.assertEqual(cm.exception.number, 2)

        with self.assertRaises(rfc1751.WrongNumberOfWordsError) as cm:
            rfc1751.string_to_bytes('rash bush milk look bad brim keno')
        self.assertEqual(cm.exception.number, 7)

        with self.assertRaises(rfc1751.WrongWordError) as cm:
            rfc1751.string_to_bytes('rash bush milk look bad Tart')
        self.assertEqual(cm.exception.word, 'Tart')

        with self.assertRaises(rfc1751.WrongNumberOfBytesError) as cm:
            rfc1751.bytes_to_string(
                b'\xCC\xAC\x2A\xED\x59',
            )
        self.assertEqual(cm.exception.number, 5)

        with self.assertRaises(rfc1751.ParityError):
            rfc1751.string_to_bytes(
                'RA5h BU5H mi1k 100k Bad Brow',
            )

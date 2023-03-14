# PsudoCode
# 1. เวลาจะเปลี่ยนเลขธรรมดาเป็นเลขโรมันต้องเช็คตัวที่น้อยกว่ามัน แล้วเอามาลบทำซ้ำจนได้คำตอบ
# 2. ดัองสร้าง list ที่เก็บข้อมูลเพื่อเปรียบว่า list ณ ปัจจุบันมีมากกว่ามั้ย ถ้ามากกว่าก็เลื่อนตัว 
# 3. ถ้าตัวใน list น้อยกว่า ก็เพิ่มตัว roman ของเลขนั้นเข้าตัวแปร แล้วลบเลขนั้นออกจากตัวเลข
# 4. ทำซ้ำจนมีตัวเลขเป็น 0
import unittest

def int_to_roman(num):
    roman_list = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                  (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                  (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    roman_parts = []
    for value, symbol in roman_list:
        while value <= num:
            roman_parts.append(symbol)
            num -= value
    return ''.join(roman_parts)

class TestIntToRoman(unittest.TestCase):
    def test_single_digit_integers(self):
        self.assertEqual(int_to_roman(1), 'I')
        self.assertEqual(int_to_roman(5), 'V')
        self.assertEqual(int_to_roman(9), 'IX')

    def test_double_digit_integers(self):
        self.assertEqual(int_to_roman(10), 'X')
        self.assertEqual(int_to_roman(42), 'XLII')
        self.assertEqual(int_to_roman(99), 'XCIX')

    def test_triple_digit_integers(self):
        self.assertEqual(int_to_roman(100), 'C')
        self.assertEqual(int_to_roman(666), 'DCLXVI')
        self.assertEqual(int_to_roman(888), 'DCCCLXXXVIII')

    def test_four_digit_integers(self):
        self.assertEqual(int_to_roman(1000), 'M')
        self.assertEqual(int_to_roman(1987), 'MCMLXXXVII')
        self.assertEqual(int_to_roman(3999), 'MMMCMXCIX')

    def test_edge_cases(self):
        self.assertEqual(int_to_roman(0), '')
        self.assertEqual(int_to_roman(4000), 'MMMM')

if __name__ == '__main__':
    unittest.main()
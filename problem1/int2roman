# PsudoCode
# 1. เวลาจะเปลี่ยนเลขธรรมดาเป็นเลขโรมันต้องเช็คตัวที่น้อยกว่ามัน แล้วเอามาลบทำซ้ำจนได้คำตอบ
# 2. ดัองสร้าง list ที่เก็บข้อมูลเพื่อเปรียบว่า list ณ ปัจจุบันมีมากกว่ามั้ย ถ้ามากกว่าก็เลื่อนตัว 
# 3. ถ้าตัวใน list น้อยกว่า ก็เพิ่มตัว roman ของเลขนั้นเข้าตัวแปร แล้วลบเลขนั้นออกจากตัวเลข
# 4. ทำซ้ำจนมีตัวเลขเป็น 0
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

def test_int_to_roman():
    # Test single digit integers
    assert int_to_roman(1) == 'I'
    assert int_to_roman(5) == 'V'
    assert int_to_roman(9) == 'IX'
    
    # Test double digit integers
    assert int_to_roman(10) == 'X'
    assert int_to_roman(42) == 'XLII'
    assert int_to_roman(99) == 'XCIX'
    
    # Test triple digit integers
    assert int_to_roman(100) == 'C'
    assert int_to_roman(666) == 'DCLXVI'
    assert int_to_roman(888) == 'DCCCLXXXVIII'
    
    # Test four digit integers
    assert int_to_roman(1000) == 'M'
    assert int_to_roman(1987) == 'MCMLXXXVII'
    assert int_to_roman(3999) == 'MMMCMXCIX'
    
    # Test edge cases
    assert int_to_roman(0) == ''
    assert int_to_roman(4000) == 'MMMM'
    
    print("if the assertionError not popup so we PASS")
    
    

test_int_to_roman()
# print(int_to_roman(3800))
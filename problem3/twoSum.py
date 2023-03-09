import unittest

def twoSum(nums: list[int], target: int) -> list[int]:
    dict_Done = {}
    for i, num in enumerate(nums):
        if target - num in dict_Done:
            return [dict_Done[target - num], i]
        dict_Done[num] = i
        #print(dict_Done)
    return []

class TestTwoSum(unittest.TestCase):
    def test_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected_output = [0, 1]
        self.assertEqual(twoSum(nums, target), expected_output)

    def test_example_2(self):
        nums = [3, 2, 4]
        target = 6
        expected_output = [1, 2]
        self.assertEqual(twoSum(nums, target), expected_output)

    def test_example_3(self):
        nums = [3, 3]
        target = 6
        expected_output = [0, 1]
        self.assertEqual(twoSum(nums, target), expected_output)
        
unittest.main()

